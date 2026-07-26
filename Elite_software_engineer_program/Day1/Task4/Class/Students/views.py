from django.shortcuts import render
from .models import StudentModel
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_students(request):
    students = StudentModel.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
     serializer = StudentSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response({"message":"Student has been added succesfully"})
     else:
         return Response(serializer.errors)
     
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = StudentModel.objects.get(id=id)
    except StudentModel.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student updated successfully"})
    return Response(serializer.errors, status=400)


@api_view(['delete'])
def delete_student(request,id):
    student = StudentModel.objects.get(id=id).delete()
    return Response({"message":"Student deleted succesfully"})
    