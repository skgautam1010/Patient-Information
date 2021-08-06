from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)