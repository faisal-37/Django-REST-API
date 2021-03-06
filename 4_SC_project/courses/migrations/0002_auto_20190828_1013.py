# Generated by Django 2.2.1 on 2019-08-28 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190828_1013'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('s_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='students.SStudent', verbose_name='Student')),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
