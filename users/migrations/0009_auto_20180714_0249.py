# Generated by Django 2.0.5 on 2018-07-13 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180714_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='benefactor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ben', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='operator',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='org', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='payment',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='rateId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rate', to='users.Rate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='wId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='weekly', to='users.WeeklySchedule'),
            preserve_default=False,
        ),
    ]
