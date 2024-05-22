from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def courses_view(request):
    return render(request, 'courses_app/courses.html')

def no_permission_view(request):
    return render(request, 'courses_app/no_permission.html')
