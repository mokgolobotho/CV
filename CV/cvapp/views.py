from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import File, Cv
import pandas as pd

# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        cv = create_db(obj.file.path)
        redirect('view_cv', cv.id_number)
    return render(request, "home.html", {})

def view_cv(request, cv_id):
    cv = Cv.objects.get(id_number=cv_id)
    return render(request, "view_cv.html", {'cv': cv})

def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',',  encoding='ISO-8859-1', on_bad_lines='skip')
    print(df.values)
    list_of_csv = [list(row) for row in df.values]
    for l in list_of_csv:
        new_cv = Cv.objects.create(
            first_name = l[0],
            last_name = l[1],
            email = l[2],
            phone_number = l[3],
            id_number = l[4],
            address = l[5],
            education = l[6],
            gender= l[7],
            skills = l[8],
            experience= l[9],
        )
        return new_cv

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})