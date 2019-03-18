from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.
#first page - signup page
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

#landing page - home page
def home_index(request):

    index_path = Image.objects.all()
    # forms=CommentForm()
    # comments = Comments.objects.all()
    # my_profile = Profile.objects.all()
    return render(request,'home.html',locals())

#profile page
def profile_path(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()

        images = Image.objects.all()
        my_profile = Profile.objects.all()
    return render(request,'profile.html', locals())

def update(request):
    all_profile = Profile.objects.all()
    profile = Profile.objects.get(user_id = request.user)
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form  = ProfileForm()

    return render(request,'new_profile.html', locals())
