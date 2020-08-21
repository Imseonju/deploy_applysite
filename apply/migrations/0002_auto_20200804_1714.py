# Generated by Django 3.0.8 on 2020-08-04 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=500, null=True)),
                ('makeweb', models.CharField(blank=True, max_length=300, null=True)),
                ('solution', models.CharField(blank=True, max_length=300, null=True)),
                ('gain', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Apply',
        ),
    ]