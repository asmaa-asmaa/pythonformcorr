
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage
def index(request):
    return HttpResponse("welcome to home page!")


@csrf_exempt
def submit_data(request):
    if request.method == 'POST':
       try:
           data = json.loads(request.body)
           name = data.get("name")
           email = data.get("email")
           msg = data.get("msg")
           print(data)
           ContactMessage.objects.create(name=name, email=email, msg=msg)
           return JsonResponse({"message": "Data received successfully", "data": data}, status=200)    
       except json.JSONDecodeError:
           return JsonResponse({'error': "Invalid JSON format"}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def serve_vue(request):
    return render(request, 'index.html')

# @api_view(['GET','POST'])
# def submit_data(request):
#     if request.method == 'POST':

#         data = request.data
#         name = data.get("name")
#         email = data.get("email")
#         msg = data.get("message")
#         print(data
#               )

        # name = request.POST.get("name")
        # email = request.POST.get("email")
        # msg = request.POST.get("msg")
        # print("name:", name, "email:", email)
        # if name and email:
        #  submission = Submission(name=name, email=email, msg=msg)
        #  submission.save()


        # return Response({"message":
        #           "data received", "data": data}) 
        
    #      return JsonResponse({"message":
    #               "data saved successfully"}, status=201) 
    #     else:
    #        return JsonResponse({"error":
    #               "missing name or email"}, status=400) 

    # return JsonResponse({"error":
    #               "invalid request method"}, status=400) 

   # if request.method == 'GET':
      #  return Response({'message':"GET method is active"})
# def submit_form(request):
#     data = request.data

#     Submission.objects.create(name=data['name'], email=data['email'])
#     return Response({"message":
#                   "Form submitted successfully"})   

# @api_view(['GET']) 
# def get_submissions(request):
#    submissions= Submission.objects.values()
#    return Response(list(submissions))
