from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RegistrationForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login, logout

from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.info(request, 'Please check your email to activate your account.')
            return redirect('register')
        else:
            return HttpResponse('Error', status=400)
    else:
        form = RegistrationForm()
        return render(request,'register.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful')
                    return render(request,'dashboard.html', {'user': request.user})
                    #return redirect('dashboard')
                else:
                    messages.error(request, 'Incorrect username or password')
                    return redirect('/')
            else:
                messages.error(request, 'Incorrect username or password')
                return redirect('/')
        else:
            return render(request,'login.html', {'form': form})
    else:
        return redirect('dashboard')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()


        return render(request,'dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': groups})
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('/')


def home(request):
    posts = Post.objects.all()
    return render(request,'home.html', {'posts': posts})


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                des = form.cleaned_data['content']
                post = Post(title=title, content=des)
                post.save()
                form = PostForm()
                return redirect('dashboard')
        form = PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return redirect('login')


def edit_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(id=id)
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                #title = form.cleaned_data['title']
                return redirect('dashboard')
        else:
            post = Post.objects.get(id=id)
            form = PostForm(instance=post)
            return render(request,'update_post.html',{'form':form})
    else:
        return redirect('login')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(id=id)
            post.delete()
            return redirect('dashboard')
    else:
        return redirect('login')