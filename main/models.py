from django.db import models

# Create your models here.
class SignUp(models.Model):
    #Leader
    leaderSchool = models.CharField(max_length=128)
    leaderClass = models.CharField(max_length=128)
    leaderName = models.CharField(max_length=128)
    leaderPhone = models.CharField(max_length=128)
    leaderEmail = models.CharField(max_length=128)
    leaderAddress = models.CharField(max_length=128)
    leaderDepartment = models.CharField(max_length=128)
    leaderStudentNo = models.CharField(max_length=128)
    leaderSex = models.CharField(max_length=128)
    
    # Advisor 1
    advisor1School = models.CharField(max_length=128)
    advisor1Department = models.CharField(max_length=128)
    advisor1Name = models.CharField(max_length=128)
    advisor1Phone = models.CharField(max_length=128)
    advisor1Email = models.CharField(max_length=128)
    
    # Advisor 2
    advisor2School = models.CharField(max_length=128)
    advisor2Department = models.CharField(max_length=128)
    advisor2Name = models.CharField(max_length=128)
    advisor2Phone = models.CharField(max_length=128)
    advisor2Email = models.CharField(max_length=128)
    
    # Member 1
    member1School = models.CharField(max_length=128)
    member1Department = models.CharField(max_length=128)
    member1Class = models.CharField(max_length=128)
    member1StudentNo = models.CharField(max_length=128)
    member1Name = models.CharField(max_length=128)
    
    # Member 2
    member2School = models.CharField(max_length=128)
    member2Department = models.CharField(max_length=128)
    member2Class = models.CharField(max_length=128)
    member2StudentNo = models.CharField(max_length=128)
    member2Name = models.CharField(max_length=128)
    
    # Member 3
    member3School = models.CharField(max_length=128)
    member3Department = models.CharField(max_length=128)
    member3Class = models.CharField(max_length=128)
    member3StudentNo = models.CharField(max_length=128)
    member3Name = models.CharField(max_length=128)
        
    # Member 4
    member4School = models.CharField(max_length=128)
    member4Department = models.CharField(max_length=128)
    member4Class = models.CharField(max_length=128)
    member4StudentNo = models.CharField(max_length=128)
    member4Name = models.CharField(max_length=128)
    
    category  = models.CharField(max_length=128)
    article = models.FileField(upload_to=None)
    # article = ndb.StringProperty()
    projectName =  models.CharField(max_length=128)
    youtubeAddress = models.URLField(max_length=128)
    softwareAndTools = models.TextField()
    projectDescription = models.TextField()
    signUpTime = models.DateTimeField(auto_now_add=True)