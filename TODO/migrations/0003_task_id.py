# Generated by Django 5.1.2 on 2024-10-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0002_task_delete_add_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
