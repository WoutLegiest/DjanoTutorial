# Generated by Django 2.1.7 on 2019-02-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=400)),
                ('tutorial_content', models.TextField()),
                ('tutorial_published', models.DateTimeField(verbose_name='date publishedse')),
            ],
        ),
    ]
