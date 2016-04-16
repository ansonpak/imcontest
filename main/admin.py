from django.contrib import admin
from main.models import SignUp

# Register your models here.
class  SignUpModelAdmin(admin.ModelAdmin):
    list_display = ['leaderSchool', 'leaderName']
    readonly_fields = ['signUpTime']
    
    class Meta:
        model = SignUp
        
admin.site.register(SignUp, SignUpModelAdmin)