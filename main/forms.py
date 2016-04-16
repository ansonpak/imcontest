from django import forms
from main.models import SignUp
import datetime

class SignUpForm(forms.ModelForm):
    #Leader
    leaderSchool = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    leaderClass = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='班級')
    leaderName = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
    leaderPhone = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'12'}), label='電話')
    leaderEmail = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'20'}), label='電郵')
    leaderAddress = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'35'}), label='地址')
    leaderDepartment = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    leaderStudentNo = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學號')
    leaderSex = forms.ChoiceField(required=True, choices=[('女','女'),('男','男')], widget=forms.RadioSelect)
    
    # Advisor 1
    advisor1School = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    advisor1Department = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    advisor1Name = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
    advisor1Phone = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'12'}), label='電話')
    advisor1Email = forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'20'}), label='電郵')
    
    # Advisor 2
    advisor2School = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    advisor2Department = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    advisor2Name = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
    advisor2Phone = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'12'}), label='電話')
    advisor2Email = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'20'}), label='電郵')
    
    # Member 1
    member1School = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    member1Department = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    member1Class = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='班級')
    member1StudentNo = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學號')
    member1Name = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
    
    # Member 2
    member2School = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    member2Department = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    member2Class = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='班級')
    member2StudentNo = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學號')
    member2Name = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
    
    # Member 3
    member3School = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    member3Department = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    member3Class = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='班級')
    member3StudentNo = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學號')
    member3Name = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
        
    # Member 4
    member4School = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學校')
    member4Department = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='科別')
    member4Class = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='班級')
    member4StudentNo = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'15'}), label='學號')
    member4Name = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'size':'10'}), label='姓名')
    
    # other
    category  = forms.ChoiceField(required=True, choices=[('開放式學校專題','開放式學校專題'),('網頁設計/動畫','網頁設計/動畫'),('小論文','小論文')], widget=forms.RadioSelect)
    article = forms.FileField(required=False)
    # article = ndb.StringProperty()
    projectName =  forms.CharField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'50'}), label='作品名稱')
    youtubeAddress = forms.URLField(required=True, max_length=128, widget=forms.TextInput(attrs={'size':'50'}))
    softwareAndTools = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))
    projectDescription = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))
    
    class Meta:
        model = SignUp
        fields = '__all__'