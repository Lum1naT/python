# Generated by Django 3.0.8 on 2020-07-27 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_status',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dt_sent', models.DateTimeField(auto_now=True)),
                ('dt_seen', models.DateTimeField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciever', to='social_network.User')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to='social_network.User')),
            ],
        ),
    ]
