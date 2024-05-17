from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def courses_view(request):
    return render(request, 'courses_app/courses.html', {'message': 'This is the Courses page'})

def courses_view_anonymous(request):
    return render(request, 'courses_app/courses.html', {'message': 'You have no permissions to view this page'})
