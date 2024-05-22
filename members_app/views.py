from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInput

def input_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        UserInput.objects.create(input_text=user_input)
        return redirect('members_app:display_view')
    return render(request, 'members_app/input.html')

def display_view(request):
    user_inputs = UserInput.objects.all()
    return render(request, 'members_app/display.html', {'user_inputs': user_inputs})

def session_view(request):
    session_data = request.session.get('user_input', 'No session data')
    return HttpResponse(f'Session data: {session_data}')
