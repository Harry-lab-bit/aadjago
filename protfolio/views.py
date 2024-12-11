from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Blogs, Internship

# Create your views here.
def home(request):
    return render(request, "home.html")

def blog(request):
    posts=Blogs.objects.all()
    context={'posts': posts}
    return render(request, "blog.html", context)


def about(request):
    return render(request, "about.html")

def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect("/auth/login")
    
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fusn = request.POST.get('usn')
        fcollege = request.POST.get('cname')
        foffer = request.POST.get('offer')
        fstartdate = request.POST.get('startdate')
        fenddate = request.POST.get('enddate')
        fprojreport = request.POST.get('projreport', '') 
        
        # Convert to upper case only if the value is not None
        if fname:
            fname = fname.upper()
        if fusn:
            fusn = fusn.upper()
        if fcollege:
            fcollege = fcollege.upper()
        if fprojreport:
            fprojreport = fprojreport.upper()
        if foffer:
            foffer = foffer.upper()
            
            
            #
            check1=Internship.objects.filter(usn=fusn)
            check2=Internship.objects.filter(email=femail)
            
            if check1 or check2:
                messages.warning(request, "Your Details are Stored Already")
                return redirect("/internshipdetails")

        # Create the Internship object
        query = Internship(
            fullname=fname,
            email=femail,
            usn=fusn,
            college_name=fcollege,
            offer_status=foffer,
            start_date=fstartdate,
            end_date=fenddate,
            proj_report=fprojreport  # If proj_report is None, it will default to an empty string
        )
        
        query.save()
        messages.success(request, "Form is submitted successfully!")
        return redirect('/internshipdetails')
    
    return render(request, "internshipdetails.html")





def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')

        # Check if phone number is missing or empty
        if not fphoneno:
            fphoneno = "Unknown"  # Or a default value if you want

        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you.")
        return redirect('/contact')

    return render(request, "contact.html")
