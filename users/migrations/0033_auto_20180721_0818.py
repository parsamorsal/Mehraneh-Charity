# Generated by Django 2.0.5 on 2018-07-21 03:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_auto_20180721_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benefactorupdatedfields',
            old_name='wId',
            new_name='week',
        ),
        migrations.AddField(
            model_name='benefactorupdatedfields',
            name='ability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='update',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updatedfields', to='users.BenefactorUpdatedFields'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 7, 21, 8, 17, 13, 188406)),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 7, 21, 8, 17, 13, 188406)),
        ),
    ]
