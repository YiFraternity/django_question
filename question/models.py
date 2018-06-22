from django.contrib.auth.models import User
from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40, )
    email = models.EmailField(max_length=100, unique=True)
    sex = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
 
    class Meta:
        db_table = "MyUser"


class Question(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    quest = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    """
    01：提问原料
    02：提问产物
    03：提问原料和产物
    04：提问影响因素
    05：提问光和色素
    06：实验题
    """
    question_type = models.IntegerField(default=0)
    img_location = models.CharField(max_length=300,default="")
    answer_keyword = models.CharField(max_length=300,default="")
    class Meta:
        db_table = "question_table"


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question,to_field='id',on_delete=models.CASCADE)
    username = models.ForeignKey(MyUser,to_field='username',on_delete=models.CASCADE,default="")
    version = models.IntegerField(primary_key=False,default=1)
    user_answer = models.CharField(max_length=300)    #用户答案

    class Meta:
        db_table = "user_answer"
        unique_together = ("question","username","version")




