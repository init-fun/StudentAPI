from functools import partial
from django.http.multipartparser import BoundaryIter
from django.shortcuts import render
import io
from rest_framework import HTTP_HEADER_ENCODING, serializers
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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

    if request.method == "POST":
        # get the json body
        json_body = request.body
        # convert the json stream
        json_stream = io.BytesIO(json_body)
        # convert to python native data type
        python_data = JSONParser().parse(json_stream)

        # convert to complex data obj
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data saved successfully!"}
            json_msg = JSONRenderer().render(res)
            return HttpResponse(json_msg, content_type="application/json")

        json_msg = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_msg, content_type="application/json")

    if request.method == "PUT":
        json_body = request.body
        json_stream = io.BytesIO(json_body)
        python_data = JSONParser().parse(json_stream)
        id = python_data.get("id", None)
        stu = Student.objects.get(id=id)
        # partial update
        serializer = StudentSerializer(stu, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {
                "msg": "Data updated",
            }

            json_msg = JSONRenderer().render(res)
            return HttpResponse(json_msg, content_type="application/json")

        json_msg = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_msg, content_type="application/json")

    if request.method == "DELETE":
        json_body = request.body
        json_stream = io.BytesIO(json_body)
        python_data = JSONParser().parse(json_stream)
        id = python_data.get("id", None)
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {
            "msg": "Object deleted successfully!!!!",
        }
        json_msg = JSONRenderer().render(res)
        return HttpResponse(json_msg, content_type="application/json")
