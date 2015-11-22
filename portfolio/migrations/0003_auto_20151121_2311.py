# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0002_auto_20151121_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='revenue',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
