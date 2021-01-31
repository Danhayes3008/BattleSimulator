# Generated by Django 3.1.5 on 2021-01-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('leadership', models.DecimalField(decimal_places=0, default='10', max_digits=2)),
                ('power', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('attackBonus', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('hp', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('armour', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('shield', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('load', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('speed', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
                ('damage', models.DecimalField(decimal_places=0, default='100', max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Warship',
            },
        ),
    ]