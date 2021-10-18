from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    url(r'^departments/$', views.departmentApi),
    url(r'^departments/([0-9]+)$', views.departmentApi),

    url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
