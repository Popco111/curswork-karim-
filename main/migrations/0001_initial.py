# Generated by Django 4.2.7 on 2023-12-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='task_images/')),
                ('task', models.TextField()),
            ],
            options={
                'verbose_name': 'example',
                'verbose_name_plural': 'examples',
            },
        ),
    ]
