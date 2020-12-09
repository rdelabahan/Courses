from django.shortcuts import render, redirect
from some_app.models import Course, Description, Comment
from django.contrib import messages

def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request,'index.html',context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        course = Course.objects.create(
            course_name=request.POST['course_name']
        )
        desc = Description.objects.create(
            description=request.POST['description']
            )
        course.description = desc
        course.save()
        return redirect("/")


def remove(request, course_id):
    context = {
        "course": Course.objects.get(id = course_id)
    }
        
    return render(request,"remove.html",context)

def delete(request, course_id):
    del_course = Course.objects.get(id = course_id)
    del_course.delete()
    return redirect("/")

def comment(request, course_id):
    context = {
        "course": Course.objects.get(id = course_id)
    }
    return render(request,"comment.html",context)

def add_comment(request, course_id):
    errors = Comment.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/courses/{course_id}/comments")
    else:
        Comment.objects.create(
            content = request.POST['content'],
            course = Course.objects.get(id = course_id)
        )
        return redirect(f"/courses/{course_id}/comments")

def delete_comment(request, course_id, comment_id):
    del_comment = Comment.objects.get(id = comment_id)
    del_comment.delete()
    return redirect(f"/courses/{course_id}/comments")
