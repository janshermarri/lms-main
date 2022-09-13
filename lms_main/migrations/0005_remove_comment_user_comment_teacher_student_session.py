# Generated by Django 4.0.6 on 2022-09-13 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_main', '0004_teacherstudentsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='teacher_student_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='session', to='lms_main.teacherstudentsession'),
            preserve_default=False,
        ),
    ]
