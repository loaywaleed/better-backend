# Generated by Django 4.2 on 2024-05-29 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0005_communityhabit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityhabit',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to='communities.community'),
        ),
    ]
