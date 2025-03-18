# from django.db import models
#
# # Create your models here.
# class Login_table(models.Model):
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     type=models.CharField(max_length=100)
#
# class client_table(models.Model):
#     LOGIN=models.ForeignKey(Login_table,on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     place = models.CharField(max_length=100)
#     contact_no = models.BigIntegerField()
#     email=models.EmailField()
#
# class expert_table(models.Model):
#     LOGIN = models.ForeignKey(Login_table, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     contact_no = models.BigIntegerField()
#     address = models.CharField(max_length=100)
#     email= models.EmailField()
#
# class video_table(models.Model):
#     expert= models.ForeignKey(expert_table, on_delete=models.CASCADE)
#     title=models.CharField(max_length=100)
#     video=models.FileField()
#
# class sign_language_table(models.Model):
#     symbol=models.FileField()
#     language=models.CharField(max_length=100)
#     details=models.CharField(max_length=100)
#
# class camera_table(models.Model):
#     c_no=models.IntegerField()
#     longitude=models.FloatField()
#     latitude=models.FloatField()
#
# class complaint_table(models.Model):
#     user_id= models.ForeignKey(client_table, on_delete=models.CASCADE)
#     replay=models.CharField(max_length=100)
#     complaint=models.CharField(max_length=100)
#     date=models.DateTimeField()
#
# class feedback_table(models.Model):
#     user_id = models.ForeignKey(client_table, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     feedback=models.CharField(max_length=100)
#
# class chat_table(models.Model):
#     messsage=models.CharField(max_length=100)
#     date = models.DateTimeField()
#     to_id= models.ForeignKey(expert_table, on_delete=models.CASCADE)
#     from_id = models.ForeignKey(client_table, on_delete=models.CASCADE)
#
# class tips_table(models.Model):
#     tips=models.CharField(max_length=100)
#     expert_id= models.ForeignKey(expert_table, on_delete=models.CASCADE)
#     details=models.CharField(max_length=100)
#
#
#


from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=25)
    Password=models.CharField(max_length=25)
    Type=models.CharField(max_length=25)

class Expert(models.Model):
    Login=models.ForeignKey(LoginTable,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=25)
    SecondName = models.CharField(max_length=25)
    Phone = models.BigIntegerField()
    Email = models.CharField(max_length=25)
    Place = models.CharField(max_length=15)


class User(models.Model):
    Login=models.ForeignKey(LoginTable,on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=25)
    SecondName = models.CharField(max_length=25)
    Phone = models.BigIntegerField()
    Email = models.CharField(max_length=250)
    Place = models.CharField(max_length=150)


class FeedbackReview(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    Feedback=models.CharField(max_length=1500)
    Rating=models.FloatField()
    Date=models.DateField()


class Lecture(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    Name=models.CharField(max_length=1500)
    File=models.FileField()
    Date = models.DateField()

class Complaint(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Complaint=models.CharField(max_length=1500)
    Date = models.DateField()
    Reply = models.CharField(max_length=1500)

class Chat(models.Model):
    Fromid=models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name="fid")
    ToId=models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name="tid")
    Chat=models.CharField(max_length=3000)
    Date = models.DateField()

class Test(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    Test=models.CharField(max_length=3000)
    Date = models.DateField()
    Level=models.CharField(max_length=2000)



class Tips(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    tips=models.CharField(max_length=3000)
    dtails=models.CharField(max_length=2000)


class video_table(models.Model):
    Expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    video=models.FileField()


class Question(models.Model):
    Question=models.FileField()
    Option1 = models.CharField(max_length=3000)
    Option2 = models.CharField(max_length=3000)
    Option3= models.CharField(max_length=3000)
    Option4 = models.CharField(max_length=3000)
    Answer = models.CharField(max_length=300)
    Test=models.ForeignKey(Test, on_delete=models.CASCADE)


class Result(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Score=models.IntegerField()
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)

class Sugession(models.Model):
    Sugession=models.CharField(max_length=10000)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    TEST=models.ForeignKey(Test,on_delete=models.CASCADE)

class camera_table(models.Model):
    c_no=models.IntegerField()
    longitude=models.FloatField()
    latitude=models.FloatField()

class sign_language_table(models.Model):
    symbol=models.FileField()
    language=models.CharField(max_length=100)
    details=models.CharField(max_length=100)