# Generated by Django 3.2.7 on 2021-09-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210911_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='type',
            field=models.IntegerField(choices=[(1, 'Действующее законодательство'), (2, 'Проеткы')], null=True),
        ),
    ]