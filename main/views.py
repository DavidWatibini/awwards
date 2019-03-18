from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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

    # index_images = Image.objects.all()
    # forms=CommentForm()
    # comments = Comments.objects.all()
    # all_profile = Profile.objects.all()
    return render(request,'home.html',locals())
