from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Student, EmployeeModel, Course, CourseDetails
from .serializers import StudentSerializer, EmployeeSerializer, CourseDetailsSerializer, CourseSerializer
from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    if request.method == 'GET':
        courseobj = CourseDetails.objects.filter(fees__gt = 1000)
        serializer = CourseDetailsSerializer(courseobj, many=True)
        return Response(serializer.data)


class CourseList(APIView):
    def get(self, request):
        courseobj = Course.objects.all()
        serializer = CourseSerializer(courseobj, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailsList(APIView):
    def get(self, request):
        courseobj = CourseDetails.objects.all()
        serializer = CourseDetailsSerializer(courseobj, many=True)
        return Response(serializer.data)

    #@action(methods=['get'], detail=False)

    def post(self, request):
        serializer = CourseDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Employee(APIView):
    def get(self, request):
        empobj = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(empobj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeUpdated(APIView):
    def get_object(self, pk):
        try:
            return EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        empobj = self.get_object(pk)
        serializeobj = EmployeeSerializer(empobj)
        return Response(serializeobj.data)

    def put(self, request, pk):
        empobj = self.get_object(pk)
        empserialize = EmployeeSerializer(empobj, data=request.data)
        if empserialize.is_valid():
            empserialize.save()
            return Response(empserialize.data, status=status.HTTP_200_OK)
        return Response(empserialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        empobj = self.get_object(pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save
            res = {'msg':'Data Created'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    return JsonResponse(serializer.errors,safe=False)'''
