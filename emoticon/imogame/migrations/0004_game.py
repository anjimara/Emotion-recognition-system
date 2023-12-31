# Generated by Django 4.0.1 on 2022-05-22 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imogame', '0003_kids_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('l1acc', models.CharField(blank=True, max_length=255, null=True)),
                ('l2acc', models.CharField(blank=True, max_length=255, null=True)),
                ('l3acc', models.CharField(blank=True, max_length=255, null=True)),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
