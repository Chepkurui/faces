# from django.shortcuts import render
from django.shortcuts import render, redirect
from web.forms import RegisterForm
from django.contrib import messages
from apis.facelogic import FaceRecognition
from apis.models import UserProfile

facerecognition = FaceRecognition()

# Create your views here.
def start_page(request):
    return render(request, 'auth/start.html')

def register(request):
    
    # Save the details in case it was a post request
    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully Registerd!')
            addFace(request.POST['face_id'])
            return redirect('/')
        else:
            messages.error(request, "Account Register Failed!")

    # Otheriwse display the form
    form = RegisterForm()
    context = {
        'title' : 'Registration Form',
        'form' : form
    }
    return render(request, 'auth/register.html', context)

def addFace(face_id):
    face_id = face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/')

def login(request):
    face_id = facerecognition.recognizeFace()
    print(face_id)
    return redirect('/welcome/'+ str(face_id))

def welcome(request, face_id):
    face_id = int(face_id)
    print(face_id)
    data = {
        'user': UserProfile.objects.get(face_id= face_id)
    }

    return render(request, 'pages/profile.html', data)