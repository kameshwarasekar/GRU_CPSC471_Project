from rest_framework import serializers
from .models import *

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'
        # fields = ('alumni_id', 'name', 
        # 'graduation_year', 'achievement_description','uni_name')    

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'   

class AlumniHasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniHas
        fields = '__all__'           

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'    
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseTeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeaching
        fields = '__all__'        

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class EntryRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryRequirement
        fields = '__all__'       

class EquivalentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquivalentClass
        fields = '__all__'  

class ExtraCurricularProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCurricularProgram
        fields = '__all__'               

class ExtracurricularOfferingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularOfferings
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'  

class FieldOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = '__all__' 

class GruUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruUser
        fields = '__all__' 

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__' 

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__' 

class PreferenceContainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceContain
        fields = '__all__' 

class PreferredUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredUni
        fields = '__all__' 

class ProvidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provides
        fields = '__all__' 

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__' 

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__' 

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__' 

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__' 