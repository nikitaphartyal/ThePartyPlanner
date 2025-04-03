from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('photo/', include('plannerapp.urls')),
    path('', views.admin_page, name='admin_page'),  # Add this line
    path('public_page/', views.public_page, name='public_page'),
    path('documents/', views.document_list, name='document_list'),
    path('admin/upload_document/', views.upload_document, name='upload_document'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
