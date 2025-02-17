from django.db import models

# Create your models here.
class Login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class client_table(models.Model):
    LOGIN=models.ForeignKey(Login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    contact_no = models.BigIntegerField()
    email=models.EmailField()

class expert_table(models.Model):
    LOGIN = models.ForeignKey(Login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.BigIntegerField()
    address = models.CharField(max_length=100)
    email= models.EmailField()

class video_table(models.Model):
    expert= models.ForeignKey(expert_table, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    video=models.FileField()

class sign_language_table(models.Model):
    symbol=models.FileField()
    language=models.CharField(max_length=100)
    details=models.CharField(max_length=100)

class camera_table(models.Model):
    c_no=models.IntegerField()
    longitude=models.FloatField()
    latitude=models.FloatField()

class complaint_table(models.Model):
    user_id= models.ForeignKey(client_table, on_delete=models.CASCADE)
    replay=models.CharField(max_length=100)
    complaint=models.CharField(max_length=100)
    date=models.DateTimeField()

class feedback_table(models.Model):
    user_id = models.ForeignKey(client_table, on_delete=models.CASCADE)
    date = models.DateTimeField()
    feedback=models.CharField(max_length=100)

class chat_table(models.Model):
    messsage=models.CharField(max_length=100)
    date = models.DateTimeField()
    to_id= models.ForeignKey(expert_table, on_delete=models.CASCADE)
    from_id = models.ForeignKey(client_table, on_delete=models.CASCADE)

class tips_table(models.Model):
    tips=models.CharField(max_length=100)
    expert_id= models.ForeignKey(expert_table, on_delete=models.CASCADE)
    details=models.CharField(max_length=100)



