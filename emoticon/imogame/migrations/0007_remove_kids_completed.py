# Generated by Django 4.0.1 on 2022-05-22 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imogame', '0006_delete_game_kids_l1acc_kids_l2acc_kids_l3acc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kids',
            name='completed',
        ),
    ]
