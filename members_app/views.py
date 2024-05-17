from django.shortcuts import render, redirect
from .forms import InputForm

def input_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['age'] = form.cleaned_data['age']
            return redirect('display')
    else:
        form = InputForm()
    return render(request, 'members_app/input.html', {'form': form})

def display_view(request):
    name = request.session.get('name')
    age = request.session.get('age')
    return render(request, 'members_app/display.html', {'name': name, 'age': age})

def session_view(request):
    return render(request, 'members_app/session.html', {
        'session_items': request.session.items()
    })
