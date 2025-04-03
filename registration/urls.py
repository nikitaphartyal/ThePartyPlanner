"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstpage/', views.FirstPage, name = 'firstpage'),
    path('',views.SignUpPage, name = 'signup'),
    path('login/', views.LoginPage, name = 'login'),
    path('home/', views.HomePage, name = 'home'),
    path('logout/', views.LogoutPage, name = 'logout'),
    path('gallery/', views.GalleryPage, name = 'gallery'),
    path('farewell/', views.farewellPage, name = 'farewell'),
    path('FAQ/', views.FAQPage, name = 'faq'),
    path('Venue/', views.VenuePage, name = 'venue'),
    path('Form/', views.FormPage, name = 'form'),
    path('AboutUs/', views.AboutUsPage, name = 'AboutUs'),
    path('Query/', views.QueryPage, name = 'Query'),
    path('feedback/', views.FeedbackPage, name = 'feedback'),
    path('Invoice/', views.InvoicePage, name = 'Invoice'),
    path('Connect/', views.ConnectPage, name = 'Connect'),
    path('Payment/', views.PaymentPage, name = 'Payment'),
    path('Package/', views.PackagePage, name = 'Package'),
    path('galleryyy/', views.galleryyyPage, name = 'galleryyy'),
    path('romanticdate/', views.romanticdatePage, name = 'romanticdate'),
    path('cocktail/', views.cocktailPage, name = 'cocktail'),
    path('engagement/', views.engagementPage, name = 'engagement'),
    path('haldi/', views.haldiPage, name = 'haldi'),
    path('babyshower/', views.babyshowerPage, name = 'babyshower'),
    path('venuee/', views.VenueePage, name = 'Venuee'),
    path('photo/', views.admin_page, name='admin_page'),
    path('admin_page/', views.admin_page, name='adminpage'),
    path('public_page/', views.public_page, name='public_page'),
    path('document_list/', views.document_list, name='document_list'),
    path('admin_upload_document/', views.upload_document, name='upload_document'),
    path('Goldsummary/', views.GoldsummaryPage, name = 'Goldsummary'),
    path('Silvesummary/', views.SilversummaryPage, name = 'Silvesummary'),
    path('Platinumsummary/', views.PlatinumsummaryPage, name = 'Platinumsummary'),
    path('admin_gallery_signup/', views.admin_gallery_signup, name='admin_gallery_signup'),
    path('admin_gallery_login/', views.admin_gallery_login, name='admin_gallery_login'),
    path('admin_venue_signup/', views.admin_venue_signup, name='admin_venue_signup'),
    path('admin_venue_login/', views.admin_venue_login, name='admin_venue_login'),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)