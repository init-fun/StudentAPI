from django.http.multipartparser import BoundaryIter
from django.shortcuts import render
import io
import requests
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body

        # convert the data into a byte stream
        json_stream = io.BytesIO(json_data)

        # change json stream to native data type
        python_data = JSONParser().parse(json_stream)

        # converting python data to complex obj
        complex_data = StudentSerializer(data=python_data)

        # validating and saving it into the backend
        if complex_data.is_valid():
            complex_data.save()
            res = {"msg": "data inserted"}
            json_msg = JSONRenderer().render(res)
            return HttpResponse(json_msg, content_type="application/json")

        res = JSONRenderer().render(complex_data.errors)
        json_msg = JSONRenderer().render(res)
        return HttpResponse(json_msg, content_type="application/json")


def student_api(request):
    if request.method == "GET":
        json_data = request.body
        # convert the request data into a byte stream
        json_stream = io.BytesIO(json_data)

        # convert json_stream to python data type
        python_data = JSONParser().parse(json_stream)
        # extract the id
        id = python_data.get("id", None)
        if id:
            # get the requested object
            stu = Student.objects.get(id=id)
            # now we got the object
            serializer = StudentSerializer(stu)
            # serialize it
            # convert it back to JSON
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
