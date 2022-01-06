from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def mainPage(request):
    posts = Post.objects.all()
    context = {
        "context": posts
    }
    return render(request, "mainapp/index.html", context)


def register_user(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form': form}
    return render(request, 'mainapp/registration.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, "ERROR")

        context = {}

        return render(request, 'mainapp/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')



def mainpage(request):
    return render(request, "mainapp/index.html")

def createPost(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("post_table")
    else:
        form = PostCreateForm()

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_post.html", context)


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form  = PostCreateForm(instance=post)
    if request.method == "POST":
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('post_table')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_post.html", context)



def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_table') 
    context = {
        'post': post
    }
    return render(request, 'mainapp/delete_post.html', context)

def postTable(request):
    post = Post.objects.all()
    context = {
        "post": post
    }
    return render(request, "mainapp/post_table.html", context)   





def createMentor(request):
    form = MentorCreateForm()
    if request.method == "POST":
        form = MentorCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("mentors_table")
    else:
        form = MentorCreateForm()

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_mentor.html", context)

def updateMentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    form  = MentorCreateForm(instance=mentor)
    if request.method == "POST":
        form = MentorCreateForm(request.POST, instance=mentor)
        if form.is_valid:
            form.save()
            return redirect('mentors_table')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_mentor.html", context)



def deleteMentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == "POST":
        mentor.delete()
        return redirect('mentors_table') 
    context = {
        'mentor': mentor
    }
    return render(request, 'mainapp/delete_mentor.html', context)

    

def mentorsTable(request):
    mentors = Mentor.objects.all()
    context = {
        "mentors": mentors
    }
    return render(request, "mainapp/mentors_table.html", context)

def create_students(request):
    form = StudentCreateForm()
    if request.method == "POST":
        form = StudentCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("students_table")
    else:
        form = StudentCreateForm()

    context = {
        "form": form
    }
    return render(request, "mainapp/create_students.html", context)


def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentCreateForm(instance=student)
    if request.method == "POST":
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect('students_table')

    context = {
        "form": form
    }

    return render(request, "mainapp/create_students.html", context)


def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('students_table')
    context = {
        'student': student
    }
    return render(request, 'mainapp/delete_student.html', context)




def students_table(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "mainapp/students_table.html", context)


def groups_table(request):
    groups = Group.objects.all()
    context = {
        "groups": groups
    }
    return render(request, "mainapp/groups_table.html", context)


def createGroup(request):
    form = GroupCreateForm()
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("groups_table")
    else:
        form = GroupCreateForm()

    context = {
        "form": form
    }
    return render(request, "mainapp/create_group.html", context)


def updateGroup(request, pk):
    group = Group.objects.get(id=pk)
    form = GroupCreateForm(instance=group)
    if request.method == "POST":
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid:
            form.save()
            return redirect('groups_table')

    context = {
        "form": form
    }

    return render(request, "mainapp/create_group.html", context)


def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect('groups_table')
    context = {
        'group': group
    }
    return render(request, 'mainapp/delete_group.html', context)
    


