"""
Django settings for your TOM project.

Originally generated by 'django-admin startproject' using Django 2.1.1.
Generated by ./manage.py tom_setup on Jan. 9, 2019, 10:20 p.m.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import logging.config
import tempfile

from lcogt_logging import LCOGTFormatter

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ks#e!w3m*y1g_=)%vmrdcyn*5dt0$)o^mq2f=vtj#myw#&amp;p3%i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('SNEX2_DEBUG', False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'guardian',
    'tom_common',
    'django_comments',
    'bootstrap4',
    'crispy_forms',
    'django_filters',
    'django_gravatar',
    'tom_targets',
    'tom_alerts',
    'tom_catalogs',
    'tom_observations',
    'tom_dataproducts',
    'custom_code',
    'gw',
    'rest_framework',
    'rest_framework.authtoken',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'tom_registration',
    'tom_scimma',
    'tom_nonlocalizedevents',
    'tom_alertstreams',
    'webpack_loader',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')

SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tom_common.middleware.Raise403Middleware',
    'tom_common.middleware.ExternalServiceMiddleware',
    'tom_common.middleware.AuthStrategyMiddleware',
    'tom_registration.middleware.RedirectAuthenticatedUsersFromRegisterMiddleware',

]

if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

ROOT_URLCONF = 'snex2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Configuration for the TOM receiving data from this TOM
DATA_SHARING = {
    'hermes': {
        'DISPLAY_NAME': os.getenv('HERMES_DISPLAY_NAME', 'Hermes'),
        'BASE_URL': os.getenv('HERMES_BASE_URL', 'https://hermes-dev.lco.global/'),
        'SCIMMA_AUTH_USERNAME': os.getenv('SCIMMA_AUTH_USERNAME', None),
        'CREDENTIAL_USERNAME': os.getenv('SCIMMA_CREDENTIAL_USERNAME', None,),
        'CREDENTIAL_PASSWORD': os.getenv('SCIMMA_CREDENTIAL_PASSWORD', None),
        'USER_TOPICS': ['hermes.test', 'tomtoolkit.test']
    },
    'tom-demo-dev': {
        'BASE_URL': os.getenv('TOM_DEMO_BASE_URL', 'http://tom-demo-dev.lco.gtn/'),
        'USERNAME': os.getenv('TOM_DEMO_USERNAME', 'set TOM_DEMO_USERNAME value in environment'),
        'PASSWORD': os.getenv('TOM_DEMO_PASSWORD', 'set TOM_DEMO_PASSWORD value in environment'),
    },
    'localhost-tom': {
        # for testing; share with yourself
        'BASE_URL': os.getenv('LOCALHOST_TOM_BASE_URL', 'http://127.0.0.1:8000/'),
        'USERNAME': os.getenv('LOCALHOST_TOM_USERNAME', 'set LOCALHOST_TOM_USERNAME value in environment'),
        'PASSWORD': os.getenv('LOCALHOST_TOM_PASSWORD', 'set LOCALHOST_TOM_PASSWORD value in environment'),
    }
}


CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'snex2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if os.environ.get('SNEX2_DB_BACKEND') == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'snex2',
            'USER': os.environ['SNEX2_DB_USER'],
            'PASSWORD': os.environ['SNEX2_DB_PASSWORD'],
            'HOST': 'snex2-db',
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            #'ENGINE': 'django.db.backends.sqlite3',
            #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            #'USER': '',
            #'PASSWORD': '',
            #'HOST': '',
            #'PORT': 5432,
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'snex2',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = 'Y-m-d H:m:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'data')
MEDIA_URL = '/data/'

# Using AWS

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRECT_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', '')
AWS_DEFAULT_ACL = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            '()': LCOGTFormatter
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}

# TOM Specific configuration
TARGET_TYPE = 'SIDEREAL'

FACILITIES = {
    'LCO': {
        'portal_url': 'https://observe.lco.global',
        'api_key': os.environ['LCO_APIKEY'],
    },
    'GEM': {
        'portal_url': {
            'GS': 'https://139.229.34.15:8443',
            'GN': 'https://128.171.88.221:8443',
        },
        'api_key': {
            'GS': '',
            'GN': '',
        },
        'user_email': '',
        'programs': {
            'GS-YYYYS-T-NNN': {
                'MM': 'Std: Some descriptive text',
                'NN': 'Rap: Some descriptive text'
            },
            'GN-YYYYS-T-NNN': {
                'QQ': 'Std: Some descriptive text',
                'PP': 'Rap: Some descriptive text',
            },
        },
    },
    'SNExGemini': {
        'portal_url': {
            'GS': 'https://139.229.34.15:8443',
            'GN': 'https://139.229.34.15:8443',
        },
        'api_key': {
            'GS': '',
            'GN': '',
        },
        'user_email': '',
        'programs': 'GS-2019A-Q-113'
    }
}

# Define extra target fields here. Types can be any of "number", "st    ring", "boolean" or "datetime"
# See https://tomtoolkit.github.io/docs/target_fields for documentat    ion on this feature
# For example:
# EXTRA_FIELDS = [
#     {'name': 'redshift', 'type': 'number'},
#     {'name': 'discoverer', 'type': 'string'}
#     {'name': 'eligible', 'type': 'boolean'},
#     {'name': 'dicovery_date', 'type': 'datetime'}
# ]
EXTRA_FIELDS = [
    {'name': 'redshift', 'type': 'number'},
    {'name': 'classification', 'type': 'string'},
    {'name': 'tweet', 'type': 'boolean'},
    {'name': 'reference', 'type': 'string', 'hidden': True},
    {'name': 'observing_run_priority', 'type': 'number', 'hidden': True},
    {'name': 'last_nondetection', 'type': 'string', 'hidden': True},
    {'name': 'first_detection', 'type': 'string', 'hidden': True},
    {'name': 'maximum', 'type': 'string', 'hidden': True},
    {'name': 'target_description', 'type': 'string', 'hidden': True}
]

# Authentication strategy can either be LOCKED (required login for all views)
# or READ_ONLY (read only access to views)
AUTH_STRATEGY = 'LOCKED'
#AUTH_STRATEGY = 'READ_ONLY'

TARGET_PERMISSIONS_ONLY = False

# URLs that should be allowed access even with AUTH_STRATEGY = LOCKED
# for example: OPEN_URLS = ['/', '/about']
OPEN_URLS = ['/snex2/tnstargets/', '/pipeline-upload/photometry-upload/']

HOOKS = {
    'target_post_save': 'custom_code.hooks.target_post_save',
    'observation_change_state': 'tom_common.hooks.observation_change_state',
    'targetextra_post_save': 'custom_code.hooks.targetextra_post_save',
    'targetname_post_save': 'custom_code.hooks.targetname_post_save',
    'sync_observation_with_snex1': 'custom_code.hooks.sync_observation_with_snex1',
    'sync_sequence_with_snex1': 'custom_code.hooks.sync_sequence_with_snex1',
    'cancel_sequence_in_snex1': 'custom_code.hooks.cancel_sequence_in_snex1',
    'update_reminder_in_snex1': 'custom_code.hooks.update_reminder_in_snex1',
    'approve_sequence_in_snex1': 'custom_code.hooks.approve_sequence_in_snex1',
    'find_images_from_snex1': 'custom_code.hooks.find_images_from_snex1',
    'change_interest_in_snex1': 'custom_code.hooks.change_interest_in_snex1',
    'sync_paper_with_snex1': 'custom_code.hooks.sync_paper_with_snex1',
    'sync_comment_with_snex1': 'custom_code.hooks.sync_comment_with_snex1',
    'cancel_gw_obs': 'gw.hooks.cancel_gw_obs',
    'ingest_gw_galaxy_into_snex1': 'gw.hooks.ingest_gw_galaxy_into_snex1',
}

BROKERS = {
    'TNS': {'api_key': os.environ['TNS_APIKEY']}
}

TOM_ALERT_CLASSES = [
    'custom_code.brokers.mars.CustomMARSBroker',
    'tom_alerts.brokers.lasair.LasairBroker',
    'tom_alerts.brokers.gaia.GaiaBroker',
    'tom_alerts.brokers.tns.TNSBroker',
    'tom_alerts.brokers.alerce.ALeRCEBroker',
    'tom_scimma.scimma.SCIMMABroker',
]

TOM_FACILITY_CLASSES = [
    'custom_code.facilities.gemini_facility.GeminiFacility',
    #'tom_observations.facilities.gemini.GEMFacility',
    'custom_code.facilities.lco_facility.SnexLCOFacility',
    #'tom_observations.facilities.soar.SOARFacility',
    'custom_code.facilities.soar_facility.SOARFacility'
]

TOM_HARVESTER_CLASSES = [
    'custom_code.harvesters.tns_harvester.TNSHarvester',
    'custom_code.harvesters.mars_harvester.MARSHarvester',
    'tom_catalogs.harvesters.simbad.SimbadHarvester',
    'tom_catalogs.harvesters.ned.NEDHarvester',
]

TOM_CADENCE_STRATEGIES = [
    'custom_code.cadences.snex_retry_failed_observations.SnexRetryFailedObservationsStrategy',
    'custom_code.cadences.snex_resume_cadence_after_failure.SnexResumeCadenceAfterFailureStrategy'
]

DATA_TYPES = (
    ('SPECTROSCOPY', 'Spectroscopy'),
    ('PHOTOMETRY', 'Photometry')
)

DATA_PRODUCT_TYPES = {
    'photometry': ('photometry', 'Photometry'),
    'fits_file': ('fits_file', 'FITS File'),
    'spectroscopy': ('spectroscopy', 'Spectroscopy'),
    'image_file': ('image_file', 'Image File')
}

DATA_PROCESSORS = {
    'photometry': 'custom_code.processors.photometry_processor.PhotometryProcessor',
    'spectroscopy': 'custom_code.processors.spectroscopy_processor.SpecProcessor',
    'fits_file': 'custom_code.processors.spectroscopy_processor.SpecProcessor',
}

#TOM_LATEX_PROCESSORS = {
#    'ObservationGroup': 'tom_publications.processors.observation_group_latex_processor.ObservationGroupLatexProcessor',
#    'TargetList': 'tom_publications.processors.target_list_latex_processor.TargetListLatexProcessor'
#}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

TARGET_CLASSIFICATIONS = [
    'Afterglow', 'Afterglow?', 'AGN', 'AGN?', 'Ca-rich', 'Ca-rich?', 'CV', 'CV?', 'Galaxy', 'ILRN', 'ILRN?', 'Junk', 'Kilonova', 'Kilonova?', 'LBV', 'LBV?', 'Nova', 'Nova?', 'SLSN-I', 'SLSN-I?', 'SLSN-II', 'SLSN-II?', 'SLSN-R', 'SLSN-R?', 'SN', 'SN I-faint', 'SN I-faint?', 'SN Ia', 'SN Ia 02cx-like', 'SN Ia 02cx-like?', 'SN Ia 02es-like', 'SN Ia 02es-like?', 'SN Ia 02ic-like', 'SN Ia 02ic-like?', 'SN Ia 91bg-like', 'SN Ia 91bg-like?', 'SN Ia 91T-like', 'SN Ia 91T-like?', 'SN Ia pec', 'SN Ia pec?', 'SN Ia?', 'SN Ib', 'SN Ib/c', 'SN Ib/c?', 'SN Ib?', 'SN Ibn', 'SN Ibn?', 'SN Ic', 'SN Ic-BL', 'SN Ic-BL?', 'SN Ic?', 'SN Icn', 'SN II', 'SN II?', 'SN IIb', 'SN IIb?', 'SN IIL', 'SN IIL?', 'SN IIn', 'SN IIn?', 'SN IIP', 'SN IIP?', 'SN?', 'Standard', 'TDE', 'TDE?', 'Unknown', 'Varstar', 'Varstar?'
]

DEFAULT_GROUPS = [
    'ANU', 'ARIES', 'CSP', 'CU Boulder', 'DLT40', 'e/PESSTO', 'ex-LCOGT', 'KIPMU', 'KMTNet', 'LBNL', 'LCOGT', 'LSQ', 'NAOC', 'Padova', 'QUB', 'SAAO', 'SIRAH', 'Skymapper', 'Tel Aviv U', 'U Penn', 'UC Berkeley', 'US GSP', 'UT Austin'
]

X_FRAME_OPTIONS = 'ALLOWALL'

HINTS_ENABLED = False
HINT_LEVEL = 20

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    #'django.contrib.auth.hashers.Argon2PasswordHasher',
    #'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

CSRF_TRUSTED_ORIGINS = ['https://test.supernova.exchange']

TOM_REGISTRATION = {
    'REGISTRATION_AUTHENTICATION_BACKEND': 'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'REGISTRATION_REDIRECT_PATTERN': 'home',
    'SEND_APPROVAL_EMAILS': True
}

MANAGERS = [
    ('SNEx Secure', 'sne@lco.global')
]

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'snex@lco.global'

EMAIL_HOST_PASSWORD = str(os.environ['SNEX_EMAIL_PASSWORD'])

DATA_UPLOAD_MAX_MEMORY_SIZE = 7000000

PLOTLY_DASH = {
    'cache_arguments': False,
    #'cache_timeout_initial_arguments': 120,
}

VUE_FRONTEND_DIR_TOM_NONLOCAL = os.path.join(STATIC_ROOT, 'tom_nonlocalizedevents/vue')
WEBPACK_LOADER = {
    'TOM_NONLOCALIZEDEVENTS': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'tom_nonlocalizedevents/vue/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'static/tom_nonlocalizedevents/vue/webpack-stats.json'),
        #'STATS_FILE': os.path.join(VUE_FRONTEND_DIR_TOM_NONLOCAL, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

TOM_API_URL = os.getenv('TOM_API_URL', 'http://127.0.0.1:8000')
HERMES_API_URL = os.getenv('HERMES_API_URL', 'https://hermes.lco.global')

SAVE_TEST_ALERTS = True

ALERT_STREAMS = [
    {
        'ACTIVE': True,
        'NAME': 'custom_code.alertstreams.hopskotch.CustomHopskotchAlertStream',
        'OPTIONS': {
            'URL': 'kafka://kafka.scimma.org/',
            'USERNAME': os.getenv('SCIMMA_AUTH_USERNAME', ''),
            'PASSWORD': os.getenv('SCIMMA_AUTH_PASSWORD', ''),
            # Group ID must be prefixed with SCiMMA SCRAM credential username to open the SCiMMA kafka stream
            'GROUP_ID': os.getenv('SCIMMA_AUTH_USERNAME', '') + '-' + os.getenv('HOPSKOTCH_GROUP_ID', 'hermes-dev'),
            'TOPIC_HANDLERS': {
                'hermes.*': 'custom_code.alertstreams.hopskotch.alert_logger',
                'tomtoolkit.test': 'custom_code.alertstreams.hopskotch.alert_logger',
                #'igwn.gwalert': 'tom_nonlocalizedevents.alertstream_handlers.igwn_event_handler.handle_igwn_message',
                'igwn.gwalert': 'gw.gw_event_handler.handle_igwn_message_with_galaxies',
            },
        },
    },
    {
        'ACTIVE': False,
        'NAME': 'tom_alertstreams.alertstreams.gcn.GCNClassicAlertStream',
        # The keys of the OPTIONS dictionary become (lower-case) properties of the AlertStream instance.
        'OPTIONS': {
            # see https://github.com/nasa-gcn/gcn-kafka-python#to-use for configuration details.
            'GCN_CLASSIC_CLIENT_ID': os.getenv('GCN_CLASSIC_CLIENT_ID', None),
            'GCN_CLASSIC_CLIENT_SECRET': os.getenv('GCN_CLASSIC_CLIENT_SECRET', None),
            'DOMAIN': 'gcn.nasa.gov',  # optional, defaults to 'gcn.nasa.gov'
            'CONFIG': {  # optional
                # 'group.id': 'tom_alertstreams-my-custom-group-id',
                # 'auto.offset.reset': 'earliest',
                # 'enable.auto.commit': False
            },
            'TOPIC_HANDLERS': {
                'gcn.classic.text.LVC_INITIAL': 'gw.gw_event_handler.handle_message',#'tom_nonlocalizedevents.alertstream_handlers.gcn_event_handler.handle_message',
                'gcn.classic.text.LVC_PRELIMINARY': 'gw.gw_event_handler.handle_message',#'tom_nonlocalizedevents.alertstream_handlers.gcn_event_handler.handle_message',
                'gcn.classic.text.LVC_RETRACTION': 'gw.gw_event_handler.handle_retraction_with_galaxies',#'tom_nonlocalizedevents.alertstream_handlers.gcn_event_handler.handle_retraction',
            },
        },
    }
]

if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    DEBUG_TOOLBAR_CONFIG = {
        'RESULTS_CACHE_SIZE': 200,
    }

try:
    from local_settings import * # noqa
except ImportError:
    pass
