from django.db import models
from django.contrib.auth.models import User


class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    education = models.TextField()  # Trường thông tin về học vấn
    work_experience = models.TextField()  # Trường thông tin về kinh nghiệm làm việc
    skills = models.TextField()  # Trường thông tin về kỹ năng
    projects = models.TextField()  # Trường thông tin về các dự án đã tham gia
    awards = models.TextField(default="")



class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    

