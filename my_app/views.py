from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'index.html')


def logincode(request):
    uname=request.POST['username']
    pwrd=request.POST['password']
    try:
        if uname== "admin@123" and  pwrd =="admin@123":
           return HttpResponse('''<script>alert("welcome");window.location='adminhome'</script> ''')
        elif uname== "expert@123" and  pwrd =="expert@123":
            return HttpResponse('''<script>alert("welcome");window.location='experthome'</script> ''')
        else:
            return HttpResponse('''<script>alert("invalid login");window.location='/'</script> ''')
    except:
        return HttpResponse('''<script>alert("invalid login");window.location='/'</script> ''')


def adminhome(request):
    return render(request,'admin/index.html')
def experthome(request):
    return render(request,'expert/index.html')



def addexpert(request):
    return render(request,'admin/Add_expert.html')

def addsignlanguage(request):
    return render(request,'admin/Add_new_sign.html')

def blockunblock(request):
    return render(request,'admin/Block_and_unblock_User.html')

def complaintReplay(request):
    return render(request,'admin/Complaint_Replay.html')

def managexpert(request):
    return render(request,'admin/Manage_expert.html')

def managesignlanguage(request):
    return render(request,'admin/Manage_sign_language.html')

def viewcomplaint(request):
    return render(request,'admin/View_Complaint.html')

def viewfeedback(request):
    return render(request,'admin/View_Feedback.html')



