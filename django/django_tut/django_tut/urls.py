
from django.urls import include, path
#from django.conf.urls import include
from django.contrib import admin



from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',views.homepage),
    path("polls/", include("polls.urls")),
]
