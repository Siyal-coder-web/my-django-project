from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Project, UserProfile

@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        project_title = request.POST.get('title')
        project_desc = request.POST.get('description')
        Project.objects.create(title=project_title, description=project_desc, user=request.user)
        return redirect('/')

    search_query = request.GET.get('search', '')
    user_projects = Project.objects.filter(user=request.user)
    
    if search_query:
        all_projects = user_projects.filter(title__icontains=search_query).order_by('-date_created')
    else:
        all_projects = user_projects.order_by('-date_created')
        
    context = {
        'projects': all_projects,
        'search_query': search_query
    }
    return render(request, 'my_app/index.html', context)

@login_required(login_url='login')
def profile_page(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        profile.bio = request.POST.get('bio')
        if request.FILES.get('profile_pic'):
            profile.profile_pic = request.FILES.get('profile_pic')
        profile.save()
        return redirect('profile')
        
    return render(request, 'my_app/profile.html', {'profile': profile})

@login_required(login_url='login')
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    project.delete()
    return redirect('/')

@login_required(login_url='login')
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    if request.method == "POST":
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.save()
        return redirect('/')
    return render(request, 'my_app/edit.html', {'project': project})

def signup_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'my_app/signup.html', {'form': form})

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'my_app/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')