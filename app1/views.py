from django.shortcuts import render,HttpResponse,redirect #HttpResponse,redirect should be imported manually
from django.contrib.auth.models import User #imported model
from django.contrib.auth import authenticate, login,logout #authenticate, login should be imported manually so that the username in the database and the username entered by the new customer should not be same; logout should be imported manually
from django.contrib.auth.decorators import login_required
from .models import Photo,Document
from .forms import PhotoForm,DocumentUploadForm
from django.http import HttpResponse
from .models import PartyDetails
from .models import Query
from .models import Feedback
import razorpay
from django.shortcuts import render
# Create your views here.
@login_required(login_url = 'login')#by this not everyone can access the home page just by typing the url of the home page
def FirstPage(request):
 return render (request , 'firstpage.html')
def HomePage(request):
 return render (request , 'home.html')
def SignUpPage(request):
    if request.method=='POST':
      uname = request.POST.get('username')
      email = request.POST.get('email')
      pass1= request.POST.get('password1')
      pass2 = request.POST.get('password2')
      #to make sure both the passwords are same
      if pass1!=pass2:
        return HttpResponse("Your password and confirm password are not similar")
      else:
           my_user= User.objects.create_user(uname,email,pass1) #every entry will be stored in this variable
           my_user.save() #details are saved
           return redirect('login') #name = 'login' from urls.py and redirect('login') should be same
      
    return render (request , 'signup.html')
def LoginPage(request):
  if request.method=='POST':
      username = request.POST.get('username')
      pass1=request.POST.get('pass')
      #so that the username in the database and the username entered by the new customer should not be same
      user = authenticate(request, username = username, password = pass1)
      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         return HttpResponse("Username or Password is incorrect!!")
  return render(request , 'login.html')

# def admin_gallery_signup(request):
#    if request.method=='POST':
#       uname = request.POST.get('username')
#       email = request.POST.get('email')
#       pass1= request.POST.get('password1')
#       pass2 = request.POST.get('password2')
#       #to make sure both the passwords are same
#       if pass1!=pass2:
#         return HttpResponse("Your password and confirm password are not similar")
#       else:
#            my_user= User.objects.create_user(uname,email,pass1) #every entry will be stored in this variable
#            my_user.save() #details are saved
#            return redirect('admin_gallery_login') #name = 'login' from urls.py and redirect('login') should be same
def admin_gallery_signup(request):
    if request.method == 'POST':
        # Handle the POST request and form submission
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # ... (rest of your POST request handling)

        return redirect('admin_gallery_login')
    else:
        # Handle the GET request (initial page load)
        # You can add any additional context data you need for the GET request
        return render(request, 'admin_gallery_signup.html')
   

def admin_gallery_login(request):
   if request.method=='POST':
      username = request.POST.get('username')
      pass1=request.POST.get('pass')
      #so that the username in the database and the username entered by the new customer should not be same
      user = authenticate(request, username = username, password = pass1)
      if user is not None:
         login(request, user)
         return redirect('adminpage')
      else:
         return HttpResponse("Username or Password is incorrect!!")
   return render(request , 'admin_gallery_login.html')

def admin_venue_signup(request):
    if request.method == 'POST':
        # Handle the POST request and form submission
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # ... (rest of your POST request handling)

        return redirect('admin_venue_login')
    else:
        # Handle the GET request (initial page load)
        # You can add any additional context data you need for the GET request
        return render(request, 'admin_venue_signup.html')
   

def admin_venue_login(request):
   if request.method=='POST':
      username = request.POST.get('username')
      pass1=request.POST.get('pass')
      #so that the username in the database and the username entered by the new customer should not be same
      user = authenticate(request, username = username, password = pass1)
      if user is not None:
         login(request, user)
         return redirect('upload_document')
      else:
         return HttpResponse("Username or Password is incorrect!!")
   return render(request , 'admin_venue_login.html')

def LogoutPage(request):
  logout(request)
  return redirect('login')

def GalleryPage(request):
   return render(request, 'gallery.html')
def FAQPage(request):
   return render(request, 'faq.html')
def VenuePage(request):
   return render(request, 'venue.html')
def AboutUsPage(request):
   return render(request, 'AboutUs.html')
def VenueePage(request):
   return render(request, 'Venuee.html')
def QueryPage(request):
   if request.method=='POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      message = request.POST.get('message')
     # Here you can process the form data as per your requirements
        # For example, you can store it in the database or perform any other operations
         # Create a new instance of PartyDetails model
         #i.e make a new db on the admin page
      query = Query(
            name=name,
            email=email,
            message=message
            
        ) #every entry will be stored in this variable
      # Save the PartyDetails instance to the database
      query.save()
        # Return a success message
      return HttpResponse("Form submitted successfully!")
      

    # If the request method is GET or any other method, render the form page
   return render(request, 'Query.html')
  

def InvoicePage(request):
   return render(request, 'Invoice.html')
def FeedbackPage(request):
   if request.method=='POST':
      message = request.POST.get('message')
     # Here you can process the form data as per your requirements
        # For example, you can store it in the database or perform any other operations
         # Create a new instance of PartyDetails model
         #i.e make a new db on the admin page
      feedback = Feedback(
            message=message
            
        ) #every entry will be stored in this variable
      # Save the PartyDetails instance to the database
      feedback.save()
        # Return a success message
      return HttpResponse("Form submitted successfully!")
   return render(request, 'feedback.html')

def ConnectPage(request):
   return render(request, 'Connect.html')
def PaymentPage(request):
   if request.method == 'POST':
         amount = 50000 # Rs. 500
         order_currency = 'INR'
         client = razorpay.Client(
            auth = ('rzp_test_Kl3OSZQurfGyC4','2G7tEXwO3kRJsHZjOErTk4ZG'))
         payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
   return render(request, 'Payment.html')
def PackagePage(request):
   return render(request, 'Package.html')
def galleryyyPage(request):
   return render(request, 'galleryyy.html')
def romanticdatePage(request):
   return render(request, 'romanticdate.html')
def engagementPage(request):
   return render(request, 'engagement.html')
def cocktailPage(request):
   return render(request, 'cocktail.html')
def haldiPage(request):
   return render(request, 'haldi.html')
def babyshowerPage(request):
   return render(request, 'babyshower.html') 
def farewellPage(request):
   return render(request, 'farewell.html')
def GoldsummaryPage(request):
    if request.method == 'POST':
         amount = 50000 # Rs. 500
         order_currency = 'INR'
         client = razorpay.Client(
            auth = ('rzp_test_C4SVACevRwDudk','NRXbUqTR9qHsLfXfv6BXU5QM'))
         payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    return render(request, 'Goldsummary.html')
def SilversummaryPage(request):
   if request.method == 'POST':
         amount = 50000 # Rs. 500
         order_currency = 'INR'
         client = razorpay.Client(
            auth = ('rzp_test_C4SVACevRwDudk','NRXbUqTR9qHsLfXfv6BXU5QM'))
         payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
   return render(request, 'Silversummary.html')
def PlatinumsummaryPage(request):
   if request.method == 'POST':
         amount = 50000 # Rs. 500
         order_currency = 'INR'
         client = razorpay.Client(
            auth = ('rzp_test_C4SVACevRwDudk','NRXbUqTR9qHsLfXfv6BXU5QM'))
         payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
   return render(request, 'Platinumsummary.html')
def FormPage(request):
     if request.method=='POST':
      firstname = request.POST.get('firstname')
      email = request.POST.get('email')
      lastname = request.POST.get('lastname')
      date= request.POST.get('date')
      date1= request.POST.get('date1')
      guest= request.POST.get('guest')
      party= request.POST.get('party')
      budget = request.POST.get('budget')
      theme = request.POST.get('theme')
      info = request.POST.get('info')
     # Here you can process the form data as per your requirements
        # For example, you can store it in the database or perform any other operations
         # Create a new instance of PartyDetails model
         #i.e make a new db on the admin page
      party_details = PartyDetails(
            first_name=firstname,
            last_name=lastname,
            email=email,
            party_date=date,
            suppliers_date=date1,
            guest_count=guest,
            party_type=party,
            budget=budget,
            theme=theme,
            additional_info=info
        ) #every entry will be stored in this variable
      # Save the PartyDetails instance to the database
      party_details.save()
        # Return a success message
      return HttpResponse("Form submitted successfully!")
      

    # If the request method is GET or any other method, render the form page
     return render(request, 'form.html')
def admin_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = PhotoForm()
    photos = Photo.objects.all()
    return render(request, 'admin_page.html', {'form': form, 'photos': photos})

def public_page(request):
    photos = Photo.objects.all()
    return render(request, 'public_page.html', {'photos': photos})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentUploadForm()
    return render(request, 'admin_upload_document.html', {'form': form})