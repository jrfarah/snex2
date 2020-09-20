# Generated by Django 3.1 on 2020-09-05 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0018_auto_20200714_1832'),
        ('custom_code', '0002_auto_20200903_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_code.sciencetags')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tom_targets.target')),
            ],
        ),
    ]
