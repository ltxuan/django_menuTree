# Generated by Django 4.1 on 2024-01-04 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_catagory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.catagory'),
        ),
    ]
