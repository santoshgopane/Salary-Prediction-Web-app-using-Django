from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import numpy as np
from sklearn.externals import joblib
# Create your views here.

Model = joblib.load('./models/Salary_prediction.pkl')
# def details(request):
#     # return HttpResponse('Hello, World!')
#     return render(request,'test.html')

def linear(request):
    return render(request,'index.html')

def predict(request):
    # messages.info(request,'Checking Message')
    if request.method == 'POST':
        years = float(request.POST['years'])
        year = np.array([[years]])
        predict = Model.predict(year)
        predict = int(predict)
        context = {'a':predict}
        return render(request,'index.html',context)
    else:
        return redirect(request,'')