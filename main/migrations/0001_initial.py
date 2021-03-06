# Generated by Django 3.2.7 on 2021-09-11 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteLaws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('short_description', models.CharField(max_length=1000)),
                ('full_description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=main.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('favourite_publication', models.IntegerField(choices=[(1, 'Публикации NCO'), (2, 'Другие публикации')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('favourite_laws', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.favouritelaws')),
            ],
        ),
        migrations.CreateModel(
            name='ImageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.upload_to)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.news')),
            ],
        ),
        migrations.CreateModel(
            name='FavouritePublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.news')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.news')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favouritelaws',
            name='laws',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.news'),
        ),
        migrations.AddField(
            model_name='favouritelaws',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
