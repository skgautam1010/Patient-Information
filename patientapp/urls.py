from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

#if settings.DEBUG:
 #   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)