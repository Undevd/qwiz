# Generated by Django 2.0.1 on 2018-06-16 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_room_questions_m2m_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('CURRENT', 'Current'), ('COMPLETE', 'Complete')], default='PENDING', max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Question')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Room')),
            ],
            options={
                'db_table': 'quiz_room_questions',
            },
        ),
        migrations.AlterUniqueTogether(
            name='roomquestions',
            unique_together={('room', 'question')},
        ),
    ]
