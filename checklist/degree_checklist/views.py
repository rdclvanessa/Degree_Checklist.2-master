from django.shortcuts import render, redirect
from .forms import CourseModelForm
from .models import DegreeType, Course, ProCourse
from .utils import courses
from django.contrib import messages

def course_form(request):
    # first, is this a returned (filled) form?
    if request.method == 'POST':
        # if it is, then take the information from the page and populate the Django form object
        form = CourseModelForm(request.POST)
        # is the data clean?
        if form.is_valid():
            #if yes, save to database
            form.save()
            messages.success(request, "Saved the course...")
        else:
            # couldn't save the data
            messages.error(request, "Failed to save...")


        return redirect("/course_form")

    # not a POST, but a GET
    else:
        # make an empty form object
        form = CourseModelForm()
        # get all Course objects from database
        courses = Course.objects.all()
        procourses = ProCourse.objects.all()
        return render(request, "courses_form.html", {"form": form, "courses": courses})
