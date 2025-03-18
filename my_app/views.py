from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
import subprocess
# Create your views here.
from .sampleeeeee import generate_video

def redirect(request):
    return HttpResponseRedirect('/Gesture.py')
def login(request):
    # return render(request,"login.html")
    return render(request,"admin/loginindex.html")
def logout(request):
    # return render(request,"login.html")
    auth.logout(request)
    return render(request,"admin/loginindex.html")
def log_code(request):
    un=request.POST['textfield']
    ps=request.POST['textfield2']

    lo =LoginTable.objects.filter(Username = un,Password = ps)
    if lo.exists():
        logindata = lo[0]
        request.session['lid']=logindata.id
        if logindata.Type == 'admin':
            return HttpResponse('''<script>alert('Welcome');window.location='/AdminHome_main'</script>''')
        elif logindata.Type == 'Expert':
            return HttpResponse('''<script>alert('Welcome');window.location='/experthome_main'</script>''')


        else:
            return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')


    # try:
    #     ob=LoginTable.objects.get(Username=un,Password=ps)
    #
    #     if ob.Type == 'admin':
    #         ob1=auth.authenticate(username='admin',password='admin')
    #         if ob1 is not None:
    #             auth.login(request,ob1)
    #
    #         return HttpResponse('''<script>alert('Welcome');window.location='/AdminHome_main'</script>''')
    #     elif ob.Type=="Expert":
    #         ob1 = auth.authenticate(username='admin', password='admin')
    #         if ob1 is not None:
    #             auth.login(request, ob1)+-
    #         request.session['lid']=ob.id
    #         return HttpResponse('''<script>alert('Welcome');window.location='/experthome_main'</script>''')
    #     else:
    #         return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')
    # except:
    #     return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')
# @login_required(login_url='/')
def AdminHome(request):
    return render(request,"admin/admin index.html")

def AdminHome_main(request):
    return render(request,"admin/admin index_main.html")

def ManageExpert(request):
    ob=Expert.objects.all()
    return render(request,"admin/Manage Experts.html",{"data":ob})

# @login_required(login_url='/')
def ManageExpert_delete(request,id):
    ob = LoginTable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/ManageExpert'</script>''')

def add_camera(request):
    return render(request,"admin/camera_configuration.html")
def add_camera_post(request):
    cm1 = request.POST['cm']

    obj = camera_table()
    obj.c_no = cm1
    obj.longitude = 1
    obj.latitude = 1
    obj.save()



    return HttpResponse('''<script>alert('Deleted');window.location='/add_camera'</script>''')


def add_sign_language(request):
    return render(request,"admin/sign_language.html")
def add_sign_language_post(request):
    symbol = request.POST['file']
    language = request.POST['file']
    details = request.POST['file']

    d = datetime.now().strftime('%y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\hp\PycharmProjects\Hand_sign_rcognition_system\dataset\\"+d+".jpg",symbol)
    path = "/dataset/"+d+".jpg"

    obj = sign_language_table()
    obj.symbol = path
    obj.language = language
    obj.language = details
    obj.save()



    return HttpResponse('''<script>alert('Deleted');window.location='/add_sign_language'</script>''')

def view_camera(request):
    data = camera_table.objects.all()
    return render(request,'admin/view_camera.html',{'data':data})



# @login_required(login_url='/')
def ManageExpert_edit(request,id):
    ob = Expert.objects.get(id=id)
    request.session['exid']=id
    return render(request, "admin/Edit.html",{'val':ob})


# @login_required(login_url='/')
def updateexp(request):
    fn = request.POST['textfield']
    ln = request.POST['textfield2']
    ad = request.POST['textarea']
    ph = request.POST['textfield3']
    mail = request.POST['textfield4']
    ob1=Expert.objects.get(id=request.session['exid'])
    ob1.FirstName = fn
    ob1.SecondName = ln
    ob1.Place = ad
    ob1.Phone = ph
    ob1.Email = mail
    ob1.save()
    return HttpResponse('''<script>alert('Updated');window.location='/ManageExpert'</script>''')

# @login_required(login_url='/')
def ManageExpert_search(request):
    name=request.POST["textfield"]
    ob=Expert.objects.filter(FirstName__icontains=name)
    return render(request,"admin/Manage Experts.html",{"data":ob,"nm":name})


# @login_required(login_url='/')
def AddExpert(request):
    return render(request,"admin/addindex.html")


# @login_required(login_url='/')
def AddExpert_code(request):
    fn = request.POST['textfield']
    ln = request.POST['textfield2']
    ad = request.POST['textarea']
    ph = request.POST['textfield3']
    mail = request.POST['textfield4']
    un = request.POST['textfield5']
    ps = request.POST['textfield6']

    ob=LoginTable()
    ob.Username=un
    ob.Password=ps
    ob.Type="Expert"
    ob.save()
    ob1=Expert()
    ob1.FirstName=fn
    ob1.SecondName=ln
    ob1.Place=ad
    ob1.Phone=ph
    ob1.Email=mail
    ob1.Login=ob
    ob1.save()
    return HttpResponse('''<script>alert('Expert Added');window.location='/ManageExpert'</script>''')

# @login_required(login_url='/')
def ViewUser(request):
    ob=User.objects.all()
    return render(request,"admin/View User.html",{"data":ob})

# @login_required(login_url='/')
def ViewUser_search(request):
    name = request.POST["textfield"]
    ob = User.objects.filter(FirstName__icontains=name)
    return render(request,"admin/View User.html",{"data":ob,'nm':name})

# @login_required(login_url='/')
def Feedback(request):
    ob = FeedbackReview.objects.all()
    return render(request,"admin/Feedback and rating.html",{"data":ob})


# @login_required(login_url='/')
def Feedback_search(request):
    date = request.POST["textfield"]
    ob = FeedbackReview.objects.filter(Date=date)
    return render(request,"admin/Feedback and rating.html",{"data":ob,'dt':str(date)})

def BlockUnblock(request):
    ob = Expert.objects.all()
    return render(request,"admin/Block or Unblock.html",{"data":ob})


# @login_required(login_url='/')
def blockexp(request,id):
    ob=LoginTable.objects.get(id=id)
    ob.Type="Blocked"
    ob.save()
    return HttpResponse('''<script>alert('Blocked');window.location='/BlockUnblock'</script>''')

# @login_required(login_url='/')
def unblockexp(request,id):
    ob=LoginTable.objects.get(id=id)
    ob.Type="Expert"
    ob.save()
    return HttpResponse('''<script>alert('Unblocked');window.location='/BlockUnblock'</script>''')


# @login_required(login_url='/')
def BlockUnblock_search(request):
    name = request.POST["textfield"]
    ob = Expert.objects.filter(FirstName__icontains=name)
    return render(request,"admin/Block or Unblock.html",{"data":ob,"nm":name})


# @login_required(login_url='/')
def Complaints(request):
    ob = Complaint.objects.all()
    return render(request,"admin/View Complaint & Snt Reply.html",{"data":ob})

def Complaints_search(request):
    date = request.POST["textfield"]
    ob = Complaint.objects.filter(Date=date)
    return render(request,"admin/View Complaint & Snt Reply.html",{"data":ob,"dt":date})


# @login_required(login_url='/')
def ManageAddLectures(request):
    ob = Lecture.objects.filter(Expert__Login__id=request.session["lid"])
    return render(request,"admin/Add & Manage Lecture.html",{'data':ob})


# @login_required(login_url='/')
def ManageAddLectures_delete(request,id):
    ob = Lecture.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/ManageAddLectures'</script>''')

# @login_required(login_url='/')
def LectureSearch(request):
    date = request.POST["textfield"]
    ob = Lecture.objects.filter(Date=date)
    return render(request, "admin/Add & Manage Lecture.html", {"data": ob, 'dt': str(date)})


# @login_required(login_url='/')
def AddLecture(request):
    return render(request,"admin/Add Lecture.html")



# @login_required(login_url='/')
def AddLecture_code(request):
    Name=request.POST['textfield']
    File=request.FILES['file']
    print(request.session["lid"])
    fs=FileSystemStorage()
    fsave=fs.save(File.name,File)

    ob=Lecture()
    ob.File=fsave
    ob.Name=Name
    ob.Expert=Expert.objects.get(Login__id=request.session['lid'])
    ob.Date=datetime.today()
    ob.save()
    return HttpResponse('''<script>alert('Uploaded');window.location='/ManageAddLectures'</script>''')


# @login_required(login_url='/')
def EditLecture(request,id):
    ob = Lecture.objects.get(id=id)
    request.session['lect_id'] = id
    return render(request,"admin/Edit Lecture.html",{'data':ob})


# @login_required(login_url='/')
def editaction_lecture(request):
    tst=request.POST['textfield']

    if 'file' in request.FILES:
        fl = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(fl.name, fl)
        ob=Lecture.objects.get(id=request.session['lect_id'])
        ob.Name=tst
        ob.File=fsave
        ob.save()
    else:
        ob = Lecture.objects.get(id=request.session['lect_id'])
        ob.Name = tst
        ob.save()

    return HttpResponse('''<script>alert('Updated');window.location='/ManageAddLectures'</script>''')


# @login_required(login_url='/')
def ManageTest(request):
    ob = Test.objects.filter(Expert__Login__id=request.session['lid'])

    return render(request,"admin/Manage Test.html",{"data":ob})


# @login_required(login_url='/')
def Managetips(request):
    ob = Tips.objects.filter(Expert__Login__id=request.session['lid'])
    return render(request,"expert/manage_tips.html",{"data":ob})


# @login_required(login_url='/')
def Managevideo(request):
    ob = video_table.objects.filter(Expert__Login__id=request.session['lid'])
    return render(request,"expert/manage_video.html",{"data":ob})

# @login_required(login_url='/')
def testsearch(request):
    nm=request.POST['textfield']
    ob = Test.objects.filter(Expert__Login__id=request.session['lid'],Test__istartswith=nm)
    return render(request, "admin/Manage Test.html", {"data": ob,'nm':nm})


# @login_required(login_url='/')
def AddTestto(request):
    # request.session['tid']
    return render(request,"admin/AddTest.html")

def AddTest(request):
    Testo = request.POST['test']
    Level = request.POST['select']
    ob=Test()
    ob.Test=Testo
    ob.Level=Level
    ob.Expert = Expert.objects.get(Login__id=request.session['lid'])
    ob.Date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert('Uploaded');window.location='/ManageTest'</script>''')


# @login_required(login_url='/')
def Addvideo(request):
    # request.session['tid']
    return render(request,"expert/add_video.html")


def Addvideo_post(request):
    video = request.FILES['file']

    fs=FileSystemStorage()
    fp=fs.save(video.name,video)

    ob=video_table()
    ob.video=fp
    ob.Expert = Expert.objects.get(Login__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert('Uploaded');window.location='/Managevideo'</script>''')




# @login_required(login_url='/')
def Addtipsto(request):
    # request.session['tid']
    return render(request,"expert/add_tips.html")

def Addtipsto_post(request):
    tips = request.POST['tips']
    dtails = request.POST['dtails']
    ob=Tips()
    ob.tips=tips
    ob.dtails=dtails
    ob.Expert = Expert.objects.get(Login__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert('Uploaded');window.location='/Managetips'</script>''')




# @login_required(login_url='/')
def EditTips(request,id):
    ob = Tips.objects.get(id=id)
    request.session['tsid']=id
    return render(request, "expert/edit_tips.html", {"data": ob})



def edittipsto_post(request):
    tips = request.POST['tips']
    dtails = request.POST['dtails']
    ob=Tips.objects.get(id=request.session['tsid'])
    ob.tips=tips
    ob.dtails=dtails
    ob.Expert = Expert.objects.get(Login__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert('Uploaded');window.location='/Managetips'</script>''')




# @login_required(login_url='/')
def EditTest(request,id):
    ob = Test.objects.get(id=id)
    request.session['tsid']=id
    return render(request, "admin/EditTest.html", {"data": ob})


@login_required(login_url='/')
def editaction(request):
    tst=request.POST['test']
    lvl=request.POST['select']
    ob=Test.objects.get(id=request.session['tsid'])
    ob.Test=tst
    ob.Level=lvl
    ob.save()
    return HttpResponse('''<script>alert('Updated');window.location='/ManageTest'</script>''')


# @login_required(login_url='/')
def DeleteTest(request,id):
    ob = Test.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Test Deleted');window.location='/ManageTest'</script>''')


# @login_required(login_url='/')
def Deletetips(request,id):
    ob = Tips.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('tips Deleted');window.location='/Managetips'</script>''')


# @login_required(login_url='/')
def Deletevideo(request,id):
    ob = video_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('video Deleted');window.location='/Managevideo'</script>''')



# @login_required(login_url='/')
def AddQuestions(request):
    return render(request,"admin/Add Questions.html")


# @login_required(login_url='/')
def AddQuestions_code(request):
    Questions=request.FILES['file']
    Option1 = request.POST['textfield2']
    Option2 = request.POST['textfield3']
    Option3 = request.POST['textfield4']
    Option4 = request.POST['textfield5']
    Answer = request.POST['select']
    ob=Question()
    fs = FileSystemStorage()
    fsave = fs.save(Questions.name,Questions)
    ob.Question = fsave
    ob.Option1=Option1
    ob.Option2 = Option2
    ob.Option3 = Option3
    ob.Option4 = Option4
    ob.Answer = Answer
    ob.Test = Test.objects.get(id=request.session['tid'])
    ob.save()
    return HttpResponse('''<script>alert('Added');window.location='/AddQuestions'</script>''')


# @login_required(login_url='/')
def ViewQuestion(request,id):
    ob1 = Question.objects.filter(Test__id=id)
    request.session['tid']=id
    return render(request, "admin/ViewQuestion.html",{"data2":ob1})


# @login_required(login_url='/')
def QuestionDelete(request,id):
    ob=Question.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/ManageTest'</script>''')





# @login_required(login_url='/')
def Reply(request,id):
    request.session['coid']=id
    return render(request, "admin/Reply.html")


# @login_required(login_url='/')
def Replycode(request):
    reply=request.POST['textarea']
    ob=Complaint.objects.get(id=request.session['coid'])
    ob.Reply=reply
    ob.save()
    return HttpResponse('''<script>alert('Replied Successfull');window.location='/Complaints'</script>''')


# @login_required(login_url='/')
def ExpertHome(request):
    return render(request,"admin/expert_index.html")


# @login_required(login_url='/')
def experthome_main(request):
    return render(request, "admin/expert_index_main.html")


# @login_required(login_url='/')
def feedbackexp(request):
    ob = FeedbackReview.objects.all()
    return render(request, "admin/feedback.html",{"data":ob})


# @login_required(login_url='/')
def Feedback_searchexp(request):
    date = request.POST["textfield"]
    ob = FeedbackReview.objects.filter(Date=date)
    return render(request,"admin/feedback.html",{"data":ob,'dt':str(date)})


# @login_required(login_url='/')
def result(request):
    ob=Result.objects.filter(Question__Test__Expert__Login__id=request.session['lid'])
    studelist=[]
    Testlist=[]
    teststudent=[]

    print("---",ob)
    print("---lif",request.session['lid'])
    for i in ob:
        print("---", i.Question.Test.Expert.id)
        if i.User.id in studelist:
            pass
        else:
            studelist.append(i.User.id)
    data=[]
    for i in studelist:
        obb=Result.objects.filter(User=i,Question__Test__Expert__Login__id=request.session['lid'])
        for ij in obb:
            if ij.Question.Test.id in Testlist:
                pass
            else:
                Testlist.append(ij.Question.Test.id)
                # studelist.append(i)

                sug=Sugession.objects.filter(TEST=ij.Question.Test.id,USER=i)
                ob1=User.objects.get(id=i)

                if len(sug)>0:
                    row={"sugg":sug[0].Sugession,"id":ij.Question.Test.id,"sid":ob1.id,"testname":ij.Question.Test.Test,"studentname":ob1.FirstName+""+ob1.SecondName,"mail":ob1.Email}
                else:
                    row = {"sugg": "no", "id": ij.Question.Test.id, "sid": ob1.id,
                           "testname": ij.Question.Test.Test, "studentname": ob1.FirstName + "" + ob1.SecondName,
                           "mail": ob1.Email}

                data.append(row)


    return render(request, "admin/Results.html",{"data":data})


# @login_required(login_url='/')
def Sugessions(request,id,sid):
    request.session['testid'] = id

    print("!!!!!!!!!!!",id,sid)
    request.session["sid"]=sid
    ob=Result.objects.filter(Question__Test__id=id,User=sid)
    sum=0
    for i in ob:
        sum=sum+float(i.Score)

    return render(request,"admin/Sugession.html",{"data":ob,"sum":sum})


# @login_required(login_url='/')
def Sugessions_code(request,):

    sug = request.POST['textarea']
    ob = Sugession()
    ob.Sugession = sug
    ob.TEST_id=request.session['testid']
    ob.USER_id=request.session["sid"]
    ob.save()
    return HttpResponse('''<script>alert('Successfully Sent');window.location='/result'</script>''')

# -----------------------webchat-----------------------
# @login_required(login_url='/')
def chatwithuser(request):
    ob = User.objects.all()
    return render(request,"expert/fur_chat.html",{'val':ob})




def chatview(request):
    ob = User.objects.all()
    d=[]
    for i in ob:
        r={"name":i.FirstName+" "+i.SecondName,'email':i.Email,'loginid':i.Login.id}
        d.append(r)
    print(d)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    print("===",msg,id)
    print("===",msg,id)
    print("===",msg,id)
    print("===",msg,id)
    print("===",msg,id)
    ob=Chat()
    ob.Fromid=LoginTable.objects.get(id=request.session['lid'])
    ob.ToId=LoginTable.objects.get(id=id)
    ob.Chat=msg
    ob.Date=datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=Chat.objects.filter(Fromid__id=id,ToId__id=request.session['lid'])
    ob2=Chat.objects.filter(Fromid__id=request.session['lid'],ToId=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.Fromid.id,"msg":i.Chat,"date":i.Date,"chat_id":i.id})

    obu=User.objects.get(Login__id=id)


    return JsonResponse({"data":res,"name":obu.FirstName+" "+obu.SecondName,"user_lid":obu.Login.id})


#---------------------------------webservices---------------------
import json
def and_log_code(request):
    un=request.POST['uname']
    ps=request.POST['pawd']
    try:
        ob=LoginTable.objects.get(Username=un,Password=ps)
        ob1=User.objects.get(Login__id=ob.id)

        data={"task":"valid","lid":ob.id,"user":ob1.FirstName+" "+ob1.SecondName}
        r=json.dumps(data)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        return HttpResponse(r)


def and_reg_code(request):
    fn=request.POST['firstname']
    ln = request.POST['lastname']
    ad = request.POST['address']
    mail=request.POST['mail']
    ph=request.POST['phone']
    un=request.POST['uname']
    ps=request.POST['pawd']

    ob1 = LoginTable()
    ob1.Username = un
    ob1.Password = ps
    ob1.Type='User'

    ob1.save()
    ob = User()
    ob.FirstName=fn
    ob.LasttName = ln
    ob.Place = ad
    ob.Email = mail
    ob.Phone = ph
    ob.Login=ob1
    ob.save()


    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)

def and_feedback_code(request):
    feedback = request.POST['feedback']
    Rating = request.POST['rating']
    user_id=request.POST['userid']
    expert_id=request.POST['expertid']
    ob=FeedbackReview()
    ob.Feedback=feedback
    ob.Rating=Rating
    ob.Date=datetime.now().today()
    ob.User=User.objects.get(Login=user_id)
    ob.Expert_id=expert_id
    ob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)


def and_complaint_code(request):
    complaint=request.POST['complaint']

    user_id = request.POST['lid']
    expert_id = request.POST['expert']
    ob=Complaint()
    ob.Complaint=complaint
    ob.Date=datetime.now()
    ob.Reply='pending'
    ob.User = User.objects.get(Login__id=user_id)
    ob.Expert = Expert.objects.get(Login_id=expert_id)
    ob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)


def and_lecture_code(request):
    ob = Lecture.objects.all()
    data=[]
    for i in ob:
        row={"id":i.id,"name":i.Name,"file":i.File.url,"date":str(i.Date),"expert":i.Expert.FirstName+""+i.Expert.SecondName}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def and_feeback_code(request):
    ob = FeedbackReview.objects.all()
    data = []
    for i in ob:
        row = {"id":i.id,"feedback":i.Feedback,"Rating":i.Rating,"date":str(i.Date),"user":i.User.FirstName+""+i.User.SecondName,"expert":i.Expert.FirstName+" "+i.Expert.SecondName}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def and_test_code(request):
    lid=request.POST["lid"]
    level=request.POST["level"]
    ob = Test.objects.filter(Level=level)
    data = []
    for i in ob:
        res=Result.objects.filter(Question__Test__id=i.id,User__Login_id=lid)
        if len(res)>0:
            score=0
            for ij in res:
                score=score+int(ij.Score)


            row = {"id":i.id,"test":i.Test,"date":str(i.Date),"level":i.Level,
               "expert":i.Expert.FirstName+""+i.Expert.SecondName,"at_st":"yes","score":score}
        else:
            row = {"id": i.id, "test": i.Test, "date": str(i.Date), "level": i.Level,
                   "expert": i.Expert.FirstName + "" + i.Expert.SecondName, "at_st": "no","score":0}
        data.append(row)
    r = json.dumps(data)
    print(data)
    return HttpResponse(r)


def and_compaint_view_code(request):
    lid=request.POST['lid']
    ob = Complaint.objects.filter(User__Login__id=lid)
    data = []
    for i in ob:
        row = {"id":i.id,"complaint":i.Complaint,"date":str(i.Date),"reply":i.Reply,"expert":i.Expert.FirstName+""+i.Expert.SecondName}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)



def and_expert_view(request):
    ob = Expert.objects.all()
    data = []
    for i in ob:
        row = {"id": i.Login.id,"expert": i.FirstName + "" + i.SecondName}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)



def in_message2(request):
    print(request.POST)
    fromid = request.POST['fid']
    print("fromid",fromid)
    toid = request.POST['toid']
    print("toid",toid)

    message=request.POST['msg']
    ob=Chat()
    ob.Fromid=LoginTable.objects.get(id=fromid)
    ob.ToId=LoginTable.objects.get(id=toid)
    ob.Chat=message
    ob.Date=datetime.today()
    # ob.time=datetime.datetime.now()
    ob.save()
    data = {"status": "send"}
    r = json.dumps(data)
    return HttpResponse(r)

#     # qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,%s,CURDATE())"
#     # value = (fromid, toid, message)
#     # print("pppppppppppppppppp")
#     # print(value)
#     # iud(qry, value)
#     # return jsonify(status='send')
#
#
def view_message2(request):
    print(request.POST)
    fromid=request.POST['fid']
    toid=request.POST['toid']
    mid=request.POST['lastmsgid']
    print(mid,"jjjjjjjjjjj")
    ob1=Chat.objects.filter(Fromid__id=fromid,ToId__id=toid,id__gt=mid)
    ob2=Chat.objects.filter(Fromid__id=toid,ToId__id=fromid,id__gt=mid)
    ob=ob1.union(ob2)
    print(ob1)
    ob=ob.order_by("id")
    data=[]
    for i in ob:
        r={"msgid":i.id,"date":str(i.Date),"message":i.Chat,"fromid":i.Fromid.id}
        data.append(r)
    if len(data)>0:
        return JsonResponse({"status":"ok","res1":data})

    else:
        return JsonResponse({"status":"no"})


def question_view(request):
    tid = request.POST['testid']
    ob = Question.objects.filter(Test__id=tid)
    data = []
    for i in ob:
        row = {"id": i.id,"Question":str(i.Question),"Option1":i.Option1,"Option2":i.Option2,"Option3":i.Option3,"Option4":i.Option4,"Answer":i.Answer}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)



def and_result(request):
   Score = request.POST['score']
   userid = request.POST['lid']
   questionid = request.POST['qid']


   ob = Result()
   ob.User=User.objects.get(Login=userid)
   ob.Question_id=questionid
   ob.Score=Score
   ob.save()


   data = {"task": "valid"}
   r = json.dumps(data)
   return HttpResponse(r)


def and_result_view(request):
    tid = request.POST['testid']
    uid= request.POST['lid']

    print(tid,"---",uid)
    ob = Result.objects.filter(Question__Test__id=tid,User__Login_id=uid,)
    data = []
    for i in ob:
        row = {"id": i.id,"score":i.Score,"Question":i.Question.Question.url,"Option1":i.Question.Option1,"Option2":i.Question.Option2,"Option3":i.Question.Option3,"Option4":i.Question.Option4,"Answer":i.Question.Answer}
        data.append(row)
    print(data,"-----------")
    r = json.dumps(data)
    return HttpResponse(r)


def and_sugession(request):
    uid=request.POST['lid']
    tid=request.POST['tid']
    ob=Sugession.objects.filter(TEST_id=tid,USER_id=uid)

    if len(ob)>0:
        data = {"status": "send","sugg":ob[0].Sugession}
    else:
        data = {"status": "invalid"}

    r = json.dumps(data)
    return HttpResponse(r)

def and_convert(request):
    txt=request.POST['txt']
    fn=generate_video(txt)

    data = {"task": fn}

    r = json.dumps(data)
    return HttpResponse(r)


def guster_det(request):
    subprocess.call(['python','C:\\Users\\zera\\PycharmProjects\\sign_language\\sign_app\\Gesture.py'])
    return render(request,'admin/loginindex.html')

# ===================================================
# @login_required(login_url='/')
def adminwithexpert(request):
    ob = Expert.objects.all()
    return render(request,"expert/fur_chat.html",{'val':ob})




def adminchatview(request):
    ob = Expert.objects.all()
    d=[]
    for i in ob:
        r={"name":i.FirstName+" "+i.SecondName,'email':i.Email,'loginid':i.Login.id}
        d.append(r)
    print(d)
    return JsonResponse(d, safe=False)

