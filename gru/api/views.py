from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

# Create your views here.

# class AlumniList(APIView):
#     def get(self, request):
#         alumni = Alumni.objects.all()
#         serializer = AlumniSerializer(alumni, many=True)
#         return Response(serializer.data)

#---------------------------Alumni----------------------------------


@api_view(['GET'])
def alumni_get(request):
    alumni = Alumni.objects.all()
    serializer = AlumniSerializer(alumni, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def alumni_getspecific(request, pk):
    alumni = Alumni.objects.get(alumni_id=pk)
    serializer = AlumniSerializer(alumni, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def alumni_post(request, format=None):
    serializer = AlumniSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def alumni_put(request, pk):
    alumni = Alumni.objects.get(alumni_id=pk)
    serializer = AlumniSerializer(instance=alumni, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def alumni_delete(request, pk):
    alumni = Alumni.objects.get(alumni_id=pk)
    alumni.delete()
    return Response('Item successfully deleted')


#---------------------------Professor----------------------------------


@api_view(['GET'])
def professor_get(request):
    professor = Professor.objects.all()
    serializer = ProfessorSerializer(professor, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def professor_getspecific(request, pk):
    professor = Professor.objects.get(prof_id=pk)
    serializer = ProfessorSerializer(professor, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def professor_post(request, format=None):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def professor_put(request, pk):
    professor = Professor.objects.get(prof_id=pk)
    serializer = ProfessorSerializer(instance=professor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def professor_delete(request, pk):
    professor = Professor.objects.get(prof_id=pk)
    professor.delete()
    return Response('Item successfully deleted')


#---------------------------University----------------------------------


@api_view(['GET'])
def university_get(request):
    university = University.objects.all()
    serializer = UniversitySerializer(university, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def university_getspecific(request, pk):
    university = University.objects.get(name=pk)
    serializer = UniversitySerializer(university, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def university_post(request, format=None):
    serializer = UniversitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def university_put(request, pk):
    university = University.objects.get(name=pk)
    serializer = UniversitySerializer(instance=university, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def university_delete(request, pk):
    university = University.objects.get(name=pk)
    university.delete()
    return Response('Item successfully deleted')


#---------------------------Degree----------------------------------


@api_view(['GET'])
def degree_get(request):
    degree = Degree.objects.all()
    serializer = DegreeSerializer(degree, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def degree_getspecific(request, pk):
    degree = Degree.objects.get(name=pk)
    serializer = DegreeSerializer(degree, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def degree_post(request, format=None):
    serializer = DegreeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def degree_put(request, pk):
    degree = Degree.objects.get(name=pk)
    serializer = DegreeSerializer(instance=degree, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def degree_delete(request, pk):
    degree = Degree.objects.get(name=pk)
    degree.delete()
    return Response('Item successfully deleted')


#---------------------------Provides----------------------------------


@api_view(['GET'])
def provides_get(request):
    provides = Provides.objects.all()
    serializer = ProvidesSerializer(provides, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def provides_getspecific(request, pk):
    provides = Provides.objects.get(provides_id=pk)
    serializer = ProvidesSerializer(provides, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def provides_post(request, format=None):
    serializer = ProvidesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def provides_put(request, pk):
    provides = Provides.objects.get(provides_id=pk)
    serializer = ProvidesSerializer(instance=provides, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def provides_delete(request, pk):
    provides = Provides.objects.get(provides_id=pk)
    provides.delete()
    return Response('Item successfully deleted')


#---------------------------Faculty----------------------------------


@api_view(['GET'])
def faculty_get(request):
    faculty = Faculty.objects.all()
    serializer = FacultySerializer(faculty, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def faculty_getspecific(request, pk):
    faculty = Faculty.objects.get(faculty_id=pk)
    serializer = FacultySerializer(faculty, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def faculty_post(request, format=None):
    serializer = FacultySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def faculty_put(request, pk):
    faculty = Faculty.objects.get(faculty_id=pk)
    serializer = FacultySerializer(instance=faculty, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def faculty_delete(request, pk):
    faculty = Faculty.objects.get(faculty_id=pk)
    faculty.delete()
    return Response('Item successfully deleted')


#---------------------------Major----------------------------------


@api_view(['GET'])
def major_get(request):
    major = Major.objects.all()
    serializer = MajorSerializer(major, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def major_getspecific(request, pk):
    major = Major.objects.get(major_code=pk)
    serializer = MajorSerializer(major, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def major_post(request, format=None):
    serializer = MajorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def major_put(request, pk):
    major = Major.objects.get(major_code=pk)
    serializer = MajorSerializer(instance=major, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def major_delete(request, pk):
    major = Major.objects.get(major_code=pk)
    major.delete()
    return Response('Item successfully deleted')


#---------------------------EntryRequirement----------------------------------


@api_view(['GET'])
def entryRequirement_get(request):
    entryRequirement = EntryRequirement.objects.all()
    serializer = EntryRequirementSerializer(entryRequirement, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def entryRequirement_getspecific(request, pk):
    entryRequirement = EntryRequirement.objects.get(major_code=pk)
    serializer = EntryRequirementSerializer(entryRequirement, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def entryRequirement_post(request, format=None):
    serializer = EntryRequirementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def entryRequirement_put(request, pk):
    entryRequirement = EntryRequirement.objects.get(major_code=pk)
    serializer = EntryRequirementSerializer(instance=entryRequirement,
                                            data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def entryRequirement_delete(request, pk):
    entryRequirement = EntryRequirement.objects.get(major_code=pk)
    entryRequirement.delete()
    return Response('Item successfully deleted')


#---------------------------EquivalentClass----------------------------------


@api_view(['GET'])
def equivalentClass_get(request):
    equivalentClass = EquivalentClass.objects.all()
    serializer = EquivalentClassSerializer(equivalentClass, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def equivalentClass_getspecific(request, pk):
    equivalentClass = EquivalentClass.objects.get(major_code=pk)
    serializer = EquivalentClassSerializer(equivalentClass, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def equivalentClass_post(request, format=None):
    serializer = EquivalentClassSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def equivalentClass_put(request, pk):
    equivalentClass = EquivalentClass.objects.get(major_code=pk)
    serializer = EquivalentClassSerializer(instance=equivalentClass,
                                           data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def equivalentClass_delete(request, pk):
    equivalentClass = EquivalentClass.objects.get(major_code=pk)
    equivalentClass.delete()
    return Response('Item successfully deleted')


#---------------------------ExtraCurricularProgram----------------------------------


@api_view(['GET'])
def extraCurricularProgram_get(request):
    extraCurricularProgram = ExtraCurricularProgram.objects.all()
    serializer = ExtraCurricularProgramSerializer(extraCurricularProgram,
                                                  many=True)
    return Response(serializer.data)


@api_view(['GET'])
def extraCurricularProgram_getspecific(request, pk):
    extraCurricularProgram = ExtraCurricularProgram.objects.get(name=pk)
    serializer = ExtraCurricularProgramSerializer(extraCurricularProgram,
                                                  many=False)
    return Response(serializer.data)


@api_view(['POST'])
def extraCurricularProgram_post(request, format=None):
    serializer = ExtraCurricularProgramSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def extraCurricularProgram_put(request, pk):
    extraCurricularProgram = ExtraCurricularProgram.objects.get(name=pk)
    serializer = ExtraCurricularProgramSerializer(
        instance=extraCurricularProgram, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def extraCurricularProgram_delete(request, pk):
    extraCurricularProgram = ExtraCurricularProgram.objects.get(name=pk)
    extraCurricularProgram.delete()
    return Response('Item successfully deleted')


#---------------------------Award----------------------------------


@api_view(['GET'])
def award_get(request):
    award = Award.objects.all()
    serializer = AwardSerializer(award, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def award_getspecific(request, pk):
    award = Award.objects.get(award_name=pk)
    serializer = AwardSerializer(award, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def award_post(request, format=None):
    serializer = AwardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def award_put(request, pk):
    award = Award.objects.get(award_name=pk)
    serializer = AwardSerializer(instance=award, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def award_delete(request, pk):
    award = Award.objects.get(award_name=pk)
    award.delete()
    return Response('Item successfully deleted')


#---------------------------ExtracurricularOfferings----------------------------------


@api_view(['GET'])
def extracurricularOfferings_get(request):
    extracurricularOfferings = ExtracurricularOfferings.objects.all()
    serializer = ExtracurricularOfferingsSerializer(extracurricularOfferings,
                                                    many=True)
    return Response(serializer.data)


@api_view(['GET'])
def extracurricularOfferings_getspecific(request, pk):
    extracurricularOfferings = ExtracurricularOfferings.objects.get(
        excurricular_name=pk)
    serializer = ExtracurricularOfferingsSerializer(extracurricularOfferings,
                                                    many=False)
    return Response(serializer.data)


@api_view(['POST'])
def extracurricularOfferings_post(request, format=None):
    serializer = ExtracurricularOfferingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def extracurricularOfferings_put(request, pk):
    extracurricularOfferings = ExtracurricularOfferings.objects.get(
        excurricular_name=pk)
    serializer = ExtracurricularOfferingsSerializer(
        instance=extracurricularProgram, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def extracurricularOfferings_delete(request, pk):
    extracurricularOfferings = ExtracurricularOfferings.objects.get(
        excurricular_name=pk)
    extracurricularOfferings.delete()
    return Response('Item successfully deleted')


#---------------------------Staff----------------------------------


@api_view(['GET'])
def staff_get(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def staff_getspecific(request, pk):
    staff = Staff.objects.get(staff_id=pk)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def staff_post(request, format=None):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def staff_put(request, pk):
    staff = Staff.objects.get(staff_id=pk)
    serializer = StaffSerializer(instance=staff, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def staff_delete(request, pk):
    staff = Staff.objects.get(staff_id=pk)
    staff.delete()
    return Response('Item successfully deleted')


#---------------------------FieldOfStudy----------------------------------


@api_view(['GET'])
def fieldOfStudy_get(request):
    fieldOfStudy = FieldOfStudy.objects.all()
    serializer = FieldOfStudySerializer(fieldOfStudy, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fieldOfStudy_getspecific(request, pk):
    fieldOfStudy = FieldOfStudy.objects.get(for_id=pk)
    serializer = FieldOfStudySerializer(fieldOfStudy, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def fieldOfStudy_post(request, format=None):
    serializer = FieldOfStudySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def fieldOfStudy_put(request, pk):
    fieldOfStudy = FieldOfStudy.objects.get(for_id=pk)
    serializer = FieldOfStudySerializer(instance=fieldOfStudy,
                                        data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def fieldOfStudy_delete(request, pk):
    fieldOfStudy = FieldOfStudy.objects.get(for_id=pk)
    fieldOfStudy.delete()
    return Response('Item successfully deleted')


#---------------------------Course----------------------------------


@api_view(['GET'])
def course_get(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def course_getspecific(request, pk):
    course = Course.objects.get(course_code=pk)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def course_post(request, format=None):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def course_put(request, pk):
    course = Course.objects.get(course_code=pk)
    serializer = CourseSerializer(instance=course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def course_delete(request, pk):
    course = Course.objects.get(course_code=pk)
    course.delete()
    return Response('Item successfully deleted')


#---------------------------CourseTeaching----------------------------------


@api_view(['GET'])
def courseTeaching_get(request):
    courseTeaching = CourseTeaching.objects.all()
    serializer = CourseTeachingSerializer(courseTeaching, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def courseTeaching_getspecific(request, pk):
    courseTeaching = CourseTeaching.objects.get(course_code=pk)
    serializer = CourseTeachingSerializer(courseTeaching, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def courseTeaching_post(request, format=None):
    serializer = CourseTeachingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def courseTeaching_put(request, pk):
    courseTeaching = CourseTeaching.objects.get(course_code=pk)
    serializer = CourseTeachingSerializer(instance=courseTeaching,
                                          data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def courseTeaching_delete(request, pk):
    courseTeaching = CourseTeaching.objects.get(course_code=pk)
    courseTeaching.delete()
    return Response('Item successfully deleted')


#---------------------------AlumniHas----------------------------------


@api_view(['GET'])
def alumniHas_get(request):
    alumniHas = AlumniHas.objects.all()
    serializer = AlumniHasSerializer(alumniHas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def alumniHas_getspecific(request, pk):
    alumniHas = AlumniHas.objects.get(alumni_id=pk)
    serializer = AlumniHasSerializer(alumniHas, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def alumniHas_post(request, format=None):
    serializer = AlumniHasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def alumniHas_put(request, pk):
    alumniHas = AlumniHas.objects.get(alumni_id=pk)
    serializer = AlumniHasSerializer(instance=alumniHas, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def alumniHas_delete(request, pk):
    alumniHas = AlumniHas.objects.get(alumni_id=pk)
    alumniHas.delete()
    return Response('Item successfully deleted')


#---------------------------Ranking----------------------------------


@api_view(['GET'])
def ranking_get(request):
    ranking = Ranking.objects.all()
    serializer = RankingSerializer(ranking, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ranking_getspecific(request, pk):
    ranking = Ranking.objects.get(uni_code=pk)
    serializer = RankingSerializer(ranking, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ranking_post(request, format=None):
    serializer = RankingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def ranking_put(request, pk):
    ranking = Ranking.objects.get(uni_code=pk)
    serializer = RankingSerializer(instance=ranking, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def ranking_delete(request, pk):
    ranking = Ranking.objects.get(uni_code=pk)
    ranking.delete()
    return Response('Item successfully deleted')


#---------------------------GruUser----------------------------------


@api_view(['GET'])
def gruUser_get(request):
    gruUser = GruUser.objects.all()
    serializer = GruUserSerializer(gruUser, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def gruUser_getspecific(request, pk):
    gruUser = GruUser.objects.get(user_id=pk)
    serializer = GruUserSerializer(gruUser, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def gruUser_post(request, format=None):
    serializer = GruUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def gruUser_put(request, pk):
    gruUser = GruUser.objects.get(user_id=pk)
    serializer = GruUserSerializer(instance=gruUser, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def gruUser_delete(request, pk):
    gruUser = GruUser.objects.get(user_id=pk)
    gruUser.delete()
    return Response('Item successfully deleted')


#---------------------------Preference----------------------------------


@api_view(['GET'])
def preference_get(request):
    preference = Preference.objects.all()
    serializer = PreferenceSerializer(preference, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def preference_getspecific(request, pk):
    preference = Preference.objects.get(pref_id=pk)
    serializer = PreferenceSerializer(preference, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def preference_post(request, format=None):
    serializer = PreferenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def preference_put(request, pk):
    preference = Preference.objects.get(pref_id=pk)
    serializer = PreferenceSerializer(instance=preference, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def preference_delete(request, pk):
    preference = Preference.objects.get(pref_id=pk)
    preference.delete()
    return Response('Item successfully deleted')


#---------------------------PreferredUni----------------------------------


@api_view(['GET'])
def preferredUni_get(request):
    preferredUni = PreferredUni.objects.all()
    serializer = PreferredUniSerializer(preferredUni, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def preferredUni_getspecific(request, pk):
    preferredUni = PreferredUni.objects.get(pref_id=pk)
    serializer = PreferredUniSerializer(preferredUni, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def preferredUni_post(request, format=None):
    serializer = PreferredUniSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def preferredUni_put(request, pk):
    preferredUni = PreferredUni.objects.get(pref_id=pk)
    serializer = PreferredUniSerializer(instance=preferredUni,
                                        data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def preferredUni_delete(request, pk):
    preferredUni = PreferredUni.objects.get(pref_id=pk)
    preferredUni.delete()
    return Response('Item successfully deleted')


#---------------------------PreferenceContain----------------------------------


@api_view(['GET'])
def preferenceContain_get(request):
    preferenceContain = PreferenceContain.objects.all()
    serializer = PreferenceContainSerializer(preferenceContain, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def preferenceContain_getspecific(request, pk):
    preferenceContain = PreferenceContain.objects.get(pref_id=pk)
    serializer = PreferenceContainSerializer(preferenceContain, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def preferenceContain_post(request, format=None):
    serializer = PreferenceContainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def preferenceContain_put(request, pk):
    preferenceContain = PreferenceContain.objects.get(pref_id=pk)
    serializer = PreferenceContainSerializer(instance=preferenceContain,
                                             data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def preferenceContain_delete(request, pk):
    preferenceContain = PreferenceContain.objects.get(pref_id=pk)
    preferenceContain.delete()
    return Response('Item successfully deleted')


# Create your views here.
def index(request):
    return render(request, 'index.html')


def option(request):
    return render(request, 'option.html')


def profile(request):
    return render(request, 'profile.html')


def delete(request):
    context = {}
    try:
        user = User.objects.get(username=request.user.username)
        user.is_active = False
        user.save()
        context['msg'] = "Account disabled"
    except User.DoesNotExist:
        context['msg'] = "User does not exist"
    except Exception as e:
        context['msg'] = e
    return render(request, "delete.html", context=context)


class UniversityListView(generic.ListView):
    model = University

    def get_queryset(self):
        queryset = University.objects.all()
        if self.request.method == 'GET':
            filtersLoc = self.request.GET.get('filter', '')
            filterTui = self.request.GET.get('tuition', 'false')
            queryset = queryset.filter(
                location__contains=self.request.GET.get('filter', ''))
            if filterTui == 'true':
                queryset = queryset.order_by('finances')
        return queryset


class UniversityDetailView(generic.DetailView):
    model = University

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        provs = Provides.objects.filter(uni_name=self.object.name)
        fac = Faculty.objects.filter(uni_name=self.object.name)
        maj = Major.objects.filter(
            faculty_id__in=fac.values_list('faculty_id'))

        exco = ExtracurricularOfferings.objects.filter(
            uni_name=self.object.name)
        excp = ExtraCurricularProgram.objects.filter(
            name__in=exco.values_list('excurricular_name'))

        club = Club.objects.filter(name__in=excp.values_list('name'))

        sport = Sport.objects.filter(name__in=excp.values_list('name'))

        award = Award.objects.filter(name__in=sport.values_list('name'))

        alumni = Alumni.objects.filter(uni_name=self.object.name)

        context['degrees'] = Degree.objects.filter(
            name__in=provs.values_list('degree_name'))
        context['faculties'] = fac
        context['majors'] = maj
        context['clubs'] = club
        context['sports'] = sport
        context['awards'] = award
        context['alumni'] = alumni
        return context


class ProfessorListView(generic.ListView):
    model = Professor


class ProfessorDetailView(generic.DetailView):
    model = Professor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['university'] = University.objects.get(
            name=self.object.uni_name)
        context['fieldOfStudy'] = FieldOfStudy.objects.filter(
            prof_id=self.object.prof_id)
        context['faculty'] = Faculty.objects.get(
            faculty_id=self.object.faculty_id)
        return context


class RankingListView(generic.ListView):
    model = Ranking


class RankingDetailView(generic.DetailView):
    model = Ranking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['university'] = University.objects.get(
            name=self.object.uni_name)
        return context