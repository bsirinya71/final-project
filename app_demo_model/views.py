from mimetypes import types_map
from django.shortcuts import render
import os
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import AppliedScience, HealthScience, PureScience
from .resources import AppliedSciResource, HealthSciResource, PureSciResource
from .forms import AppliedForm, HealthForm, PureForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tablib import Dataset
import pandas as pd
import numpy as np


@login_required
def upload_model(request):   
    return render(request, 'app_demo_model/upload_model.html')

@login_required
def upload_sci_model(request):
    if request.method == 'POST':
        applied = AppliedSciResource()
        pure = PureSciResource()
        health = HealthSciResource()

        dataset = Dataset()
        new_file = request.FILES['myfile']
        
         #check type file
        if new_file.name.endswith('csv'):
            df = pd.read_csv(new_file)
        elif new_file.name.endswith('xlsx'):
            df = pd.read_excel(new_file)
        else :
            messages.info(request, "ต้องการไฟล์ของข้อมูลที่เป็น excel หรือ csv")
            return render(request, 'app_demo_model/upload_model.html')

        print('read data')
        df = df.dropna()#delete row missing value
        # print(df.head())
        
        a = df[(df['major'] == 'ICT')|(df['major'] == 'DSSI')|(df['major'] == 'polymer')]
        # print(a.head())
        # print(len(a))
        
        h = df[(df['major'] == 'enviSci')|(df['major'] == 'safety')]
        # print(h.head())
        # print(len(h))
        
        p = df[(df['major'] == 'bio')|(df['major'] == 'chemi')|(df['major'] == 'math')|(df['major'] == 'microBio')|(df['major'] == 'physics')]
        # print(p.head())
        # print(len(p))
        
        #check type column
        for i in df.columns:
            if df.dtypes[i] != np.object_:
                messages.info(request, "ในคอลัมน์ของเกรดเฉลี่ยต้องการข้อมูล excellent, very good, good, medium, poor, very poor")
                return render(request, 'app_demo_model/upload_model.html')
              
        # import_data = dataset.load(df)
        import_data = dataset.load(a)
        result = applied.import_data(dataset, dry_run=True, raise_errors=True)
        if not result.has_errors():
            applied.import_data(dataset, dry_run=False)
            
        import_data1 = dataset.load(h)
        result2 = health.import_data(dataset, dry_run=True, raise_errors=True)
        if not result2.has_errors():
            health.import_data(dataset, dry_run=False) 
        
        import_data2 = dataset.load(p)
        result3 = pure.import_data(dataset, dry_run=True, raise_errors=True)
        if not result3.has_errors():
            pure.import_data(dataset, dry_run=False) 
            
        messages.success(request, "อัปโหลดข้อมูลสำเร็จ")
        print('upload success.')
        
    return render(request, 'app_demo_model/upload_model.html')

@login_required
def data_in_applied_sci(request):
    applied = AppliedScience.objects.all() #for all the records
    # print(applied)
    total = applied.count() 
    context={
      'applied':applied,
      'total': total,
    } 
    return render(request, 'app_demo_model/data_in_applied_model.html', context)

@login_required
def delete_data_applied(request):
    applied = AppliedScience.objects.all()
    applied.delete()
    return render(request, 'app_demo_model/data_in_applied_model.html')

# @login_required
# def upload_health_sci_model(request):
#     if request.method == 'POST':
#         health = HealthSciResource()
#         dataset = Dataset()
#         new_health = request.FILES['healthfile']
#         print('name file = ', new_health.name)
#         #check type file
#         if not new_health.name.endswith('xlsx'):
#             messages.info(request, "ต้องการไฟล์ของข้อมูลที่เป็น excel")
#             return render(request, 'app_demo_model/upload_health_sci.html')
        
#         df = pd.read_excel(new_health)
#         df = df.dropna()#delete row with missing value
        
#         #check type column
#         for i in df.columns:
#             if df.dtypes[i] != np.object_:
#                 messages.info(request, "ในคอลัมน์ของเกรดเฉลี่ยต้องการข้อมูล excellent, very good, good, medium, poor, very poor")
#                 return render(request, 'app_demo_model/upload_health_sci.html')
        
#         import_data = dataset.load(df)
#         result = health.import_data(dataset, dry_run=True)
#         if not result.has_errors():
#             health.import_data(dataset, dry_run=False)       
#         messages.success(request, "อัปโหลดข้อมูลสำเร็จ")
        
#         print('upload success.')
        
#     return render(request, 'app_demo_model/upload_health_sci.html')

@login_required
def data_in_health_sci(request):
    health = HealthScience.objects.all() #for all the records
    total = health.count() 
    context={
      'health':health,
      'total': total,
    } 
    return render(request, 'app_demo_model/data_in_health_model.html', context)

@login_required
def delete_data_health(request):
    applied = HealthScience.objects.all()
    applied.delete()
    return render(request, 'app_demo_model/data_in_health_model.html')

# @login_required
# def upload_pure_sci_model(request):
#     if request.method == 'POST':
#         pure = PureSciResource()
#         dataset = Dataset()
#         new_pure = request.FILES['purefile']
#         print('name file = ', new_pure.name)
        
#         if not new_pure.name.endswith('xlsx'):
#             messages.info(request, "ต้องการไฟล์ของข้อมูลที่เป็น excel")
#             return render(request, 'app_demo_model/upload_pure_sci.html')
        
#         df = pd.read_excel(new_pure)
#         df = df.dropna()#delete row with missing value

#         #check type column
#         for i in df.columns:
#             if df.dtypes[i] != np.object_:
#                 messages.info(request, "ในคอลัมน์ของเกรดเฉลี่ยต้องการข้อมูล excellent, very good, good, medium, poor, very poor")
#                 return render(request, 'app_demo_model/upload_pure_sci.html')
        
#         import_data = dataset.load(df)
#         result = pure.import_data(dataset, dry_run=True)
#         if not result.has_errors():
#             pure.import_data(dataset, dry_run=False)
        
#         messages.success(request, "อัปโหลดข้อมูลสำเร็จ")
        
#     return render(request, 'app_demo_model/upload_pure_sci.html')

@login_required
def data_in_pure_sci(request):
    pure = PureScience.objects.all() #for all the records
    # print(pure)
    total = pure.count() 
    print(total)
    context={
      'pure': pure,
      'total': total,
    } 
    return render(request, 'app_demo_model/data_in_pure_model.html', context)

@login_required
def delete_data_pure(request):
    pure = PureScience.objects.all()
    pure.delete()
    return render(request, 'app_demo_model/data_in_pure_model.html')

@login_required
def show_model(request):
    applied = AppliedScience.objects.all()
    health = HealthScience.objects.all()
    pure = PureScience.objects.all()
    total_applied = applied.count()
    total_health = health.count()
    total_pure = pure.count()
    total = total_applied + total_health + total_pure
    context = {
        'applied': applied,
        'health': health,
        'pure': pure,
        'total': total,
    }
    
    return render(request, 'app_demo_model/show_model.html', context)

@login_required
def delete_all_data(request):
    applied = AppliedScience.objects.all()
    health = HealthScience.objects.all()
    pure = PureScience.objects.all()
    applied.delete()
    health.delete()
    pure.delete()
    
    return render(request, 'app_demo_model/show_model.html')
    
    