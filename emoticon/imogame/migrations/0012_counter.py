# Generated by Django 4.0.1 on 2022-05-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imogame', '0011_level2_rename_angryvid_level1_disgust_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
