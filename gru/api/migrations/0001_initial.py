# Generated by Django 3.1.7 on 2021-04-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('alumni_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('graduation_year', models.IntegerField()),
                ('achievement_description', models.TextField(blank=True, null=True)),
                ('uni_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'alumni',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AlumniHas',
            fields=[
                ('alumni_id', models.AutoField(primary_key=True, serialize=False)),
                ('degree_name', models.TextField()),
            ],
            options={
                'db_table': 'alumni_has',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.TextField()),
                ('name', models.TextField()),
                ('award_name', models.TextField()),
                ('year_awarded', models.IntegerField()),
            ],
            options={
                'db_table': 'award',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'club',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.AutoField(primary_key=True, serialize=False)),
                ('course_number', models.FloatField()),
                ('course_name', models.TextField(blank=True, null=True)),
                ('faculty_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseTeaching',
            fields=[
                ('course_code', models.AutoField(primary_key=True, serialize=False)),
                ('course_number', models.FloatField()),
                ('prof_id', models.IntegerField()),
            ],
            options={
                'db_table': 'course_teaching',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('field', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'degree',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EntryRequirement',
            fields=[
                ('major_code', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.TextField()),
                ('grade', models.IntegerField()),
            ],
            options={
                'db_table': 'entry_requirement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EquivalentClass',
            fields=[
                ('major_code', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.TextField()),
                ('name', models.TextField()),
                ('grade', models.IntegerField()),
            ],
            options={
                'db_table': 'equivalent_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExtracurricularOfferings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_name', models.TextField()),
                ('excurricular_name', models.TextField()),
            ],
            options={
                'db_table': 'extracurricular_offerings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExtraCurricularProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'extra_curricular_program',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('uni_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faculty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('prof_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.TextField()),
            ],
            options={
                'db_table': 'field_of_study',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GruUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('name', models.TextField(blank=True, null=True)),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'gru_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major_code', models.AutoField(primary_key=True, serialize=False)),
                ('major_name', models.TextField()),
                ('no_of_years', models.IntegerField()),
                ('degree_name', models.TextField(blank=True, null=True)),
                ('faculty_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'major',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('pref_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'preference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreferenceContain',
            fields=[
                ('pref_id', models.AutoField(primary_key=True, serialize=False)),
                ('uni_name', models.TextField()),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'preference_contain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreferredUni',
            fields=[
                ('pref_id', models.AutoField(primary_key=True, serialize=False)),
                ('preferred_uni_name', models.TextField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'preferred_uni',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('prof_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('name', models.TextField()),
                ('uni_name', models.TextField(blank=True, null=True)),
                ('faculty_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_name', models.TextField(blank=True, null=True)),
                ('degree_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'provides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('uni_code', models.AutoField(primary_key=True, serialize=False)),
                ('best_program', models.TextField(blank=True, null=True)),
                ('rank', models.IntegerField()),
                ('prev_year_rank', models.IntegerField(blank=True, null=True)),
                ('uni_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ranking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.TextField()),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'sport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.TextField()),
                ('name', models.TextField()),
                ('uni_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('impact_on_industry', models.TextField(blank=True, null=True)),
                ('finances', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'university',
                'managed': False,
            },
        ),
    ]