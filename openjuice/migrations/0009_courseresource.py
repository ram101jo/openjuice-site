# Generated by Django 3.0.2 on 2020-02-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openjuice', '0008_bookresource'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('topics', models.ManyToManyField(to='openjuice.Topic')),
            ],
            options={
                'unique_together': {('title', 'organization')},
            },
        ),
    ]
