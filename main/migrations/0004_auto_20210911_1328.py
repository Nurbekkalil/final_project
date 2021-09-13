# Generated by Django 3.2.7 on 2021-09-11 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_law_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritelaws',
            name='laws',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.law'),
        ),
        migrations.AlterField(
            model_name='favouritepublication',
            name='publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.publication'),
        ),
    ]