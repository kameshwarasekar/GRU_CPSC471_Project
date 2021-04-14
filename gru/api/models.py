# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid
from django.urls import reverse


class Alumni(models.Model):
    alumni_id = models.AutoField(primary_key=True)
    name = models.TextField()
    graduation_year = models.IntegerField()
    achievement_description = models.TextField(blank=True, null=True)
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'alumni'
        ordering = ['name']

    def __str__(self):
        return self.name


class AlumniHas(models.Model):
    alumni_id = models.AutoField(primary_key=True)
    degree_name = models.TextField()

    class Meta:
        db_table = 'alumni_has'

    def __str__(self):
        return str(self.alumni_id)


class Award(models.Model):
    sport = models.TextField()
    name = models.TextField()
    award_name = models.TextField(primary_key=True)
    year_awarded = models.IntegerField()

    class Meta:
        db_table = 'award'

    def __str__(self):
        return self.name


class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'club'

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.AutoField(primary_key=True)
    course_number = models.FloatField()
    course_name = models.TextField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.course_name + " " + str(self.course_code)


class CourseTeaching(models.Model):
    course_code = models.AutoField(primary_key=True)
    course_number = models.FloatField()
    prof_id = models.IntegerField()

    class Meta:
        db_table = 'course_teaching'

    def __str__(self):
        return str(self.course_code)


class Degree(models.Model):
    name = models.TextField(primary_key=True)
    field = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'degree'
        constraints = [
            models.UniqueConstraint(fields=['name', 'field'],
                                    name='uniqueDegree')
        ]

    def __str__(self):
        return self.name


class EntryRequirement(models.Model):
    major_code = models.AutoField(primary_key=True)
    class_name = models.TextField()
    grade = models.IntegerField()

    class Meta:
        db_table = 'entry_requirement'

    def __str__(self):
        return str(self.major_code)


class EquivalentClass(models.Model):
    major_code = models.AutoField(primary_key=True)
    class_name = models.TextField()
    name = models.TextField()
    grade = models.IntegerField()

    class Meta:
        db_table = 'equivalent_class'

    def __str__(self):
        return str(self.major_code)


class ExtraCurricularProgram(models.Model):
    name = models.TextField(primary_key=True)

    class Meta:
        db_table = 'extra_curricular_program'

    def __str__(self):
        return self.name


class ExtracurricularOfferings(models.Model):
    uni_name = models.TextField()
    excurricular_name = models.TextField(primary_key=True)

    class Meta:
        db_table = 'extracurricular_offerings'

    def __str__(self):
        return self.excurricular_name


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'faculty'

    def __str__(self):
        return self.name


class FieldOfStudy(models.Model):
    fos_id = models.IntegerField(primary_key=True)
    prof_id = models.IntegerField()
    field_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'field_of_study'

    def __str__(self):
        return str(self.fos_id)


class GruUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.TextField()
    name = models.TextField(blank=True, null=True)
    password = models.TextField()

    class Meta:
        db_table = 'gru_user'

    def __str__(self):
        return self.name


class Major(models.Model):
    major_code = models.AutoField(primary_key=True)
    major_name = models.TextField()
    no_of_years = models.IntegerField()
    degree_name = models.TextField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'major'

    def __str__(self):
        return self.major_name + " " + str(self.major_code)


class Preference(models.Model):
    pref_id = models.UUIDField(primary_key=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'preference'

    def __str__(self):
        return str(self.pref_id) + " " + str(self.user_id)


class PreferenceContain(models.Model):
    pref_id = models.UUIDField(primary_key=True)
    uni_name = models.TextField()
    user_id = models.IntegerField()

    class Meta:
        db_table = 'preference_contain'

    def __str__(self):
        return str(self.pref_id)


class PreferredUni(models.Model):
    pref_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique ID for this particular preference')
    preferred_uni_name = models.TextField(null=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'preferred_uni'

    def __str__(self):
        return str(self.pref_id)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('pref-detail', args=[str(self.pref_id)])


class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    name = models.TextField()
    uni_name = models.TextField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'professor'
        ordering = ['name']

    def __str__(self):
        return str(self.prof_id)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('professor-detail', args=[str(self.prof_id)])


class Provides(models.Model):
    provides_id = models.IntegerField(primary_key=True)
    uni_name = models.TextField(blank=True, null=True)
    degree_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provides'

    def __str__(self):
        return self.uni_name


class Ranking(models.Model):
    uni_code = models.AutoField(primary_key=True)
    best_program = models.TextField(blank=True, null=True)
    rank = models.IntegerField()
    prev_year_rank = models.IntegerField(blank=True, null=True)
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ranking'
        ordering = ['rank']

    def __str__(self):
        return self.uni_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('ranking-detail', args=[str(self.uni_code)])


class Sport(models.Model):
    sport = models.TextField()
    name = models.TextField(primary_key=True)

    class Meta:
        db_table = 'sport'

    def __str__(self):
        return self.name


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    position = models.TextField()
    name = models.TextField()
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return str(self.staff_id)


class University(models.Model):
    name = models.TextField(primary_key=True)
    location = models.TextField()
    description = models.TextField()
    impact_on_industry = models.TextField(blank=True, null=True)
    finances = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'university'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('university-detail', args=[str(self.name)])
