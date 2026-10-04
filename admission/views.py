from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from admission.models import Admission
from admission.forms import admission
from django.db.models import Q

def home(request):
    # return render(request,'index.html',{})
    students_data=Admission.objects.all()
    result=students_data.filter(id=4).exists()
    if result:
        result=students_data.get(id=3)
    # students_data=students_data.filter(id=2,stu_class='Python')
    # students_data=students_data.filter(id__gt=1,id__lt=5)
    # students_data=students_data.filter(id__gte=1,id__lte=5)
    # students_data=students_data.filter(Q(fees__gte=3000) & Q(stu_class="Python"))
    students_data=students_data.filter(Q(fees__gte=3000) | Q(stu_class="Python"))
    res=render(request,'index.html',{'students_data':list(students_data),'result':result})
    return res

def deleteadmission(request,id):
    result=Admission.objects.get(id=id)
    result.delete()
    return redirect('home')

def editadmission(request,id):
    result=Admission.objects.get(id=id)
    res=render(request,"admissionedit.html",{'result':result})
    return res

def admissionentry(request):
    # admission_form=admission()
    if request.method=='POST':
        result=admission(request.POST)
        if result.is_valid():
            id=result.cleaned_data['id']
            stu_name=result.cleaned_data['stu_name']
            stu_father=result.cleaned_data['stu_father']
            joindate=result.cleaned_data['joindate']
            stu_class=result.cleaned_data['stu_class']
            fees=result.cleaned_data['fees']
            result=Admission(
                id=int(id),
                stu_name=stu_name,
                stu_father=stu_father,
                joindate=joindate,
                stu_class=stu_class,
                fees=int(fees)
            )
            result.save()
            # fs=open("students.txt",'a')
            # fs.write('\n-----------------------------')
            # fs.write("\nID              : "+str(id))
            # fs.write("\nName            : "+str(stu_name))
            # fs.write("\nFather          : "+str(stu_father))
            # fs.write("\nJoinDate        : "+str(joindate))
            # fs.write("\nCourse          : "+str(stu_class))
            # fs.write("\nFees            : "+str(fees))
            # fs.close()
            return redirect('home')
            
    res=render(request,'admissionentry.html',{})
    return res

def products(request):
    return render(request,'products.html',{})

def services(request):
    # return HttpResponse("<h1>Services Available</h1>")
    return render(request,'services.html',{})

def login(request):
    return render(request,'login.html',{})

