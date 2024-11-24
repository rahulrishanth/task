from django.db import models

# Create your models here.

class tbl_event(models.Model):
    event_name=models.CharField(max_length=100)
    event_date=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    image=models.FileField(max_length=100,upload_to="invitation",null=True,blank=True)
    venue=models.CharField(max_length=100)
    event_time=models.CharField(max_length=100)
    guest_name=models.CharField(max_length=100,null=True)
    guest_profile=models.FileField(max_length=100,null=True,upload_to="guest_profile")
    def __str__(self):
        return self.event_name

class tbl_student(models.Model):
    name=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    regno=models.CharField(max_length=1000)
    password=models.CharField(max_length=100)
    ref_event=models.ForeignKey(tbl_event,related_name="ref_event_detail",null=True,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.name
    
class tbl_feedback(models.Model):
    star=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    ref_event=models.ForeignKey(tbl_event,related_name="ref_event_view",on_delete=models.CASCADE,null=True,blank=True)
    ref_student=models.ForeignKey(tbl_student,related_name="ref_student_detail",on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.star

    

