# Generated by Django 4.2.16 on 2024-10-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('deline', models.TimeField()),
                ('prio', models.IntegerField(null=True)),
            ],
        ),
    ]