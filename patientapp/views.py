from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import Contact,Patient
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import PatientRegister

# Create your views here.
def home(request):
    if request.method=="POST":
        pr=PatientRegister(request.POST,request.FILES)
        if pr.is_valid():
            pr.save()
            messages.success(request,"Information Saved Successfully!")
            return HttpResponseRedirect('/')
    else:
        pr=PatientRegister()
    pat=Patient.objects.all()
    return render(request,'index.html',{'form':pr,'pat':pat})




def delete_data(request,id):
    if request.method=="POST":
        pi=Patient.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Data Deletion Successful!")
        return HttpResponseRedirect('/')



def update_data(request,id):
    if request.method=="POST":
        pi=Patient.objects.get(pk=id)
        pr=PatientRegister(request.POST,request.FILES,instance=pi)
        if pr.is_valid():
            pr.save()
            messages.success(request,"Information Updated Successfully!")
            return HttpResponseRedirect('id')
    else:
        pi=Patient.objects.get(pk=id)
        pr=PatientRegister(instance=pi)
    return render(request,'updatedata.html',{'form':pr})




def aboutus(request):
    return render(request,'aboutus.html')


@csrf_exempt
def contactus(request):
    if(request.method=='POST'):
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        contact=request.POST['phone']
        emailid=request.POST['emailid']
        feedback=request.POST['feedback']

        d=Contact(first_name=first_name,
                 last_name=last_name,
                 contact=contact,
                 emailid=emailid,
                 feedback=feedback)
        d.save()
        messages.success(request,"Feedback Received!! Thanks for contacting..we will get back to you very soon!")
        return HttpResponseRedirect('contactus')
    return render(request,'contactus.html')