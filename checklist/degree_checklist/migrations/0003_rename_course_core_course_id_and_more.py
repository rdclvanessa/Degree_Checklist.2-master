# Generated by Django 4.2.7 on 2023-11-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0002_remove_program_course_core_corecode_core_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='core',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='core',
            old_name='degreeType',
            new_name='degreeType_id',
        ),
        migrations.RenameField(
            model_name='procourse',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='procourse',
            old_name='program',
            new_name='program_id',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='core',
            new_name='core_id',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='courses',
            new_name='courses_id',
        ),
        migrations.AddField(
            model_name='degreerequirements',
            name='isCore',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degreerequirements',
            name='isDegree',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degreerequirements',
            name='isProgram',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procourse',
            name='isCore',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procourse',
            name='isDegree',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procourse',
            name='isProgram',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]