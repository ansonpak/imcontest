from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^addSignUp/$', views.addSignUp, name='addSignUp'),
    url(r'^success/', views.success, name='success'),
    url(r'^signUp/(?P<signUpID>[0-9]+)/$', views.signUp,name='signUp'),
    url(r'^admin7123/', views.admin7123, name='admin7123'),
    url(r'^deletesignUp/(?P<signUpID>[0-9]+)/$', views.deletesignUp,name='deletesignUp'),
]