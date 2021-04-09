from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from  django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.http import Http404
from rest_framework.decorators import api_view


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
    alumni = Alumni.objects.get(alumni_id = pk)
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
    serializer = AlumniSerializer(instance = alumni, data=request.data)
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
    professor = Professor.objects.get(prof_id = pk)
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
    serializer = ProfessorSerializer(instance = professor, data=request.data)
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
    university = University.objects.get(name = pk)
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
    serializer = UniversitySerializer(instance = university, data=request.data)
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
    degree = Degree.objects.get(name = pk)
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
    degree = DegreeSerializer(instance = degree, data=request.data)
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
    provides = Provides.objects.get(provides_id = pk)
    serializer = ProvidesSerializer(provides, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def provides_post(request, format=None):
    serializer =ProvidesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def provides_put(request, pk):
    provides = Provides.objects.get(provides_id=pk)
    provides = ProvidesSerializer(instance = provides, data=request.data)
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
    faculty = Faculty.objects.get(faculty_id = pk)
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
    faculty = FacultySerializer(instance = faculty, data=request.data)
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
    major = Major.objects.get(major_code = pk)
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
    major = MajorSerializer(instance = major, data=request.data)
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

# @api_view(['GET'])
# def entryRequirement_getspecific(request, pk):
#     entryRequirement = EntryRequirement.objects.get(str(major_code+class_name)=pk)
#     serializer = EntryRequirementSerializer(entryRequirement, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def entryRequirement_post(request, format=None):
    serializer = EntryRequirementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def entryRequirement_put(request, pk):
#     entryRequirement = EntryRequirement.objects.get(major_code+class_name=pk)
#     entryRequirement = EntryRequirementSerializer(instance = entryRequirement, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def entryRequirement_delete(request, pk):
#     entryRequirement = EntryRequirement.objects.get(major_code+class_name=pk)
#     entryRequirement.delete()
#     return Response('Item successfully deleted')



#---------------------------EquivalentClass----------------------------------

@api_view(['GET'])
def equivalentClass_get(request):
    equivalentClass = EquivalentClass.objects.all()
    serializer = EquivalentClassSerializer(equivalentClass, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def equivalentClass_getspecific(request, pk):
#     equivalentClass = EquivalentClass.objects.get(str(major_code+class_name)=pk)
#     serializer = EquivalentClassSerializer(equivalentClass, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def equivalentClass_post(request, format=None):
    serializer = EquivalentClassSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def equivalentClass_put(request, pk):
#     equivalentClass = EquivalentClass.objects.get(major_code+class_name=pk)
#     equivalentClass = EquivalentClassSerializer(instance = equivalentClass, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def equivalentClass_delete(request, pk):
#     equivalentClass = EquivalentClass.objects.get(major_code+class_name=pk)
#     equivalentClass.delete()
#     return Response('Item successfully deleted')




#---------------------------ExtraCurricularProgram----------------------------------

@api_view(['GET'])
def extraCurricularProgram_get(request):
    extraCurricularProgram = ExtraCurricularProgram.objects.all()
    serializer = ExtraCurricularProgramSerializer(extraCurricularProgram, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def extraCurricularProgram_getspecific(request, pk):
    extraCurricularProgram = ExtraCurricularProgram.objects.get(name = pk)
    serializer = ExtraCurricularProgramSerializer(extraCurricularProgram, many=False)
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
    extraCurricularProgram = ExtraCurricularProgramSerializer(instance = extraCurricularProgram, data=request.data)
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

# @api_view(['GET'])
# def award_getspecific(request, pk):
#     award = Award.objects.get(str(major_code+class_name)=pk)
#     serializer = AwardSerializer(award, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def award_post(request, format=None):
    serializer = AwardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def award_put(request, pk):
#     award = Award.objects.get(major_code+class_name=pk)
#     award = AwardSerializer(instance = award, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def award_delete(request, pk):
#     award = Award.objects.get(major_code+class_name=pk)
#     award.delete()
#     return Response('Item successfully deleted')



#---------------------------ExtracurricularOfferings----------------------------------

@api_view(['GET'])
def extracurricularOfferings_get(request):
    extracurricularOfferings = ExtracurricularOfferings.objects.all()
    serializer = ExtracurricularOfferingsSerializer(extracurricularOfferings, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def extracurricularOfferings_getspecific(request, pk):
#     extracurricularOfferings = ExtracurricularOfferings.objects.get(str(major_code+class_name)=pk)
#     serializer = ExtracurricularOfferingsSerializer(extracurricularOfferings, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def extracurricularOfferings_post(request, format=None):
    serializer = ExtracurricularOfferingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def extracurricularOfferings_put(request, pk):
#     extracurricularOfferings = ExtracurricularOfferings.objects.get(major_code+class_name=pk)
#     extracurricularOfferings = ExtracurricularOfferingsSerializer(instance = extracurricularProgram, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def extracurricularOfferings_delete(request, pk):
#     extracurricularOfferings = ExtracurricularOfferings.objects.get(major_code+class_name=pk)
#     extracurricularOfferings.delete()
#     return Response('Item successfully deleted')

#---------------------------Staff----------------------------------

@api_view(['GET'])
def staff_get(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def staff_getspecific(request, pk):
    staff = Staff.objects.get(staff_id = pk)
    serializer = StaffSerializer(staff, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def staff_post(request, format=None):
    serializer =StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def staff_put(request, pk):
    staff = Staff.objects.get(staff_id=pk)
    staff = StaffSerializer(instance = staff, data=request.data)
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

# @api_view(['GET'])
# def fieldOfStudy_getspecific(request, pk):
#     fieldOfStudy = FieldOfStudy.objects.get(str(major_code+class_name)=pk)
#     serializer = FieldOfStudySerializer(fieldOfStudy, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def fieldOfStudy_post(request, format=None):
    serializer = FieldOfStudySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def fieldOfStudy_put(request, pk):
#     fieldOfStudy = FieldOfStudy.objects.get(major_code+class_name=pk)
#     fieldOfStudy = FieldOfStudySerializer(instance = fieldOfStudy, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def fieldOfStudy_delete(request, pk):
#     fieldOfStudy = FieldOfStudy.objects.get(major_code+class_name=pk)
#     fieldOfStudy.delete()
#     return Response('Item successfully deleted')


#---------------------------Course----------------------------------

@api_view(['GET'])
def course_get(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def course_getspecific(request, pk):
#     course = Course.objects.get(str(major_code+class_name)=pk)
#     serializer = CourseSerializer(course, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def course_post(request, format=None):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def course_put(request, pk):
#     course = Course.objects.get(major_code+class_name=pk)
#     course = CourseSerializer(instance = course, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def course_delete(request, pk):
#     course = Course.objects.get(major_code+class_name=pk)
#     course.delete()
#     return Response('Item successfully deleted')


#---------------------------CourseTeaching----------------------------------

@api_view(['GET'])
def courseTeaching_get(request):
    courseTeaching = CourseTeaching.objects.all()
    serializer = CourseTeachingSerializer(courseTeaching, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def courseTeaching_getspecific(request, pk):
#     courseTeaching = CourseTeaching.objects.get(str(major_code+class_name)=pk)
#     serializer = CourseTeachingSerializer(courseTeaching, many=False)
#     return Response(serializer.data)


@api_view(['POST'])
def courseTeaching_post(request, format=None):
    serializer = CourseTeachingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def courseTeaching_put(request, pk):
#     courseTeaching = CourseTeaching.objects.get(major_code+class_name=pk)
#     courseTeaching = CourseTeachingSerializer(instance = courseTeaching, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def courseTeaching_delete(request, pk):
#     courseTeaching = CourseTeaching.objects.get(major_code+class_name=pk)
#     courseTeaching.delete()
#     return Response('Item successfully deleted')















# Create your views here.
def index(request):
    # num_prof = Professor.objects.all().count()
    # num_uni = University.objects.all().count()
    # num_course = Course.objects.all().count()
    # context = {
    #     'num_prof': num_prof,
    #     'num_uni': num_uni,
    #     'num_course': num_course
    # }
    return render(request, 'index.html')


def option(request):
    # num_prof = Professor.objects.all().count()
    # num_uni = University.objects.all().count()
    # num_course = Course.objects.all().count()
    # context = {
    #     'num_prof': num_prof,
    #     'num_uni': num_uni,
    #     'num_course': num_course
    # }
    return render(request, 'option.html')


class UniversityListView(generic.ListView):
    model = University


class UniversityDetailView(generic.DetailView):
    model = University


class ProfessorListView(generic.ListView):
    model = Professor


class ProfessorDetailView(generic.DetailView):
    model = Professor


class RankingListView(generic.ListView):
    model = Ranking


class RankingDetailView(generic.DetailView):
    model = Ranking
