import json
import logging
from datetime import datetime
from astropy.time import Time
from custom_code.models import TNSTarget


logger = logging.getLogger(__name__)


class TNSTargetQuery:

    def __init__(self, mag_lower, days_since_nondet, days_since_discovery, magrise, *args, **kwargs):
        self.mag_lower = mag_lower
        self.days_since_nondet = days_since_nondet
        self.days_since_discovery = days_since_discovery
        self.magrise = magrise

        self.candidates, self.tnsnames, self.coords, self.rises = self.get_candidates(self)
        self.det, self.nondet = self.get_photometry(self)


    def get_candidates(self, *args, **kwargs):
        jdnow = Time(datetime.utcnow()).jd
        jdmin = jdnow - self.days_since_discovery
        tnstargets = TNSTargets.objects.filter(disc_jd > jdmin)

        tnsnames = []
        tns_name_dict = {}
        coords = {}
        rises = {}
        for t in tnstargets:
            all_phot = json.loads(t.all_phot)
            lnd_jd = t.lnd_jd
            if not t.lnd_maglim:
                continue

            jds = [all_phot[obs]['jd'] for obs in all_phot]
            if not jds:
                continue
            
            most_recent_jd = max(jds)
            recent_phot = [all_phot[obs] for obs in all_phot if all_phot[obs]['jd'] == most_recent_jd][0]
            most_recent_mag = float(recent_phot['flux'])

            if most_recent_mag < self.mag_lower and lnd_jd > jdnow - self.days_since_nondet and t.lnd_maglim - most_recent_mag > self.magrise:
                tnsnames.append(t.name)
                tns_name_dict[t.name] = t.name # Artefact of how the ingestion works
                coords[t.name] = [t.ra, r.dec]
                rises[t.name] = float(t.lnd_maglim) - most_recent_mag

        return tnsnames, tns_name_dict, coords, rises


    def get_photometry(self, *args, **kwargs):
        phot = {}
        nondet = {}
        for name in self.candidates:
            current_phot = {}
            current_nondet = {}

            t = TNSTarget.objects.get(name=name)
            all_phot = json.loads(t.all_phot)
            for ind, phot in all_phot.items():
                filt = phot['filters']['name']
                if phot.get('flux', ''):
                    fluxerr = phot.get('fluxerr', 0)
                    current_phot.setdefault(filt, {})
                    current_phot[filt][str(phot['jd']-2400000.5)] = [phot['flux'], fluxerr]
                else:
                    current_nondet.setdefault(filt, {})
                    current_nondet[filt][str(phot['jd']-2400000.5)] = phot['limflux']

            phot[name] = current_phot
            nondet[name] = current_nondet

        return phot, nondet