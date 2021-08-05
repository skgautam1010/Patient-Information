from django.shortcuts import render
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')




@csrf_exempt
def contactus(request):
    if(request.method=='POST'):
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        contact=request.POST['telnum']
        emailid=request.POST['emailid']
        feedback=request.POST['feedback']

        d=Contact(first_name=first_name,
                 last_name=last_name,
                 contact=contact,
                 emailid=emailid,
                 feedback=feedback)
        c=d.save()
        messages.success(request,"Feedback Received!! Thanks for contacting..we will get back to you very soon!")

    return render(request,'contactus.html')