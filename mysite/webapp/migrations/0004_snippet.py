# Generated by Django 3.1.4 on 2020-12-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webapp', '0003_delete_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rno', models.IntegerField()),
                ('q1', models.TextField()),
                ('q2', models.TextField()),
                ('q3', models.TextField()),
            ],
        ),
    ]