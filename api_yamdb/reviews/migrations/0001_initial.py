# Generated by Django 2.2.16 on 2021-09-08 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='category')),
                ('slug', models.SlugField(unique=True, verbose_name='category slug')),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='genre')),
                ('slug', models.SlugField(unique=True, verbose_name='genre slug')),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='title')),
                ('year', models.IntegerField(verbose_name='year of issue')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='category title')),
                ('genre', models.ManyToManyField(related_name='titles', to='reviews.Genre', verbose_name='genre title')),
            ],
            options={
                'ordering': ('-year',),
            },
        ),
    ]
