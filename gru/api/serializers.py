from rest_framework import serializers
from .models import Alumni,Professor

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

