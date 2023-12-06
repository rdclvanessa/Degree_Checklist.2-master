# Generated by Django 4.2.6 on 2023-11-01 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='course',
        ),
        migrations.AddField(
            model_name='core',
            name='coreCode',
            field=models.IntegerField(help_text='Course Credit Hours.', null=True),
        ),
        migrations.AddField(
            model_name='core',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.course'),
        ),
        migrations.CreateModel(
            name='ProCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.course')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.program')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='courses',
            field=models.ManyToManyField(through='degree_checklist.ProCourse', to='degree_checklist.course'),
        ),
    ]