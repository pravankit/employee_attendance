from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from service.models import Employee_details
import csv
import calendar
from datetime import datetime


  


def individual_graph(request):
 employee_name = Service.objects.all()
 employee_data = Employee_details.objects.all()
 try:
  e_name= request.GET.get('namelist')
  error=""
  days_graph=[]
  label_names=[] 
  backgroundcolor=[]
  for rows in employee_data:
      days_graph.append(getattr(rows, e_name))
  for rows in employee_data:
      label_names.append(rows.Month)
  for data in days_graph:
   if data>=20:
      backgroundcolor.append('green')
   else:
      backgroundcolor.append('red') 
  if request.GET.get('export'):
    start_date=request.GET.get('start_date')
    end_date=request.GET.get('end_date')
    year,month1,date=start_date.split('-')
    year,month2,date=end_date.split('-')
    month1_name = calendar.month_name[int(month1)]
    month2_name = calendar.month_name[int(month2)]
   
    response=HttpResponse(content_type = 'text/csv')  
    writer = csv.writer(response)
    writer.writerow(['Month','working_days'])
    
    for member in Employee_details.objects.filter(Month_number__range=(month1,month2)).values_list('Month',e_name):
            writer.writerow(member)
    response['Content-Disposition']='attachment; filename='''f'{e_name}({month1_name}-{month2_name}).csv'''''''        
    return response
  
 except:
    days_graph=[0]
    label_names=[0] 
    backgroundcolor=[0]
    error = "Enter the Start Month and End Month"
 my_list ={'emp_name':employee_name,'emp_data': employee_data, 'label_names':label_names, 'days_graph': days_graph,'e_name':e_name, 'error':error,'backgroundcolor':backgroundcolor}
 return render(request, "details.html", my_list)
   
    

    



def home(request):
     employee_name = Service.objects.all()
     
     curr_month_number= datetime.now().month
     
     first_last_month = int((curr_month_number +11 )% 12)
     if first_last_month==0:
        first_last_month=12
     first_last_month_name= calendar.month_name[first_last_month]
     
     second_last_month = int((first_last_month-1 )% 12)
     if second_last_month==0:
        second_last_month=12
     
     second_last_month_name= calendar.month_name[second_last_month]
     third_last_month = int((second_last_month-1 )% 12)
     if third_last_month==0:
        third_last_month=12
     third_last_month_name= calendar.month_name[third_last_month]
     data_first_last_month = []
     data_second_last_month=[]
     data_third_last_month=[]
     data_labels=[]
     data_labels1=[]
     data_labels1.append(first_last_month_name)
     data_labels1.append(second_last_month_name)
     data_labels1.append(third_last_month_name)
     
     for rows in employee_name:   
        data_first_last_month.append(getattr(rows, first_last_month_name))
        data_second_last_month.append(getattr(rows, second_last_month_name))
        data_third_last_month.append(getattr(rows, third_last_month_name))
        data_labels.append(rows.Name)
     
     my_list2={'data_first_last_month':data_first_last_month, 'data_second_last_month':data_second_last_month,'data_third_last_month':data_third_last_month, 'data_labels':data_labels,'data_labels1':data_labels1 }
     return render(request, "index.html",my_list2)
