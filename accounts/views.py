from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group
from contacts.models import Contact
from realtors.models import Owner
from listings.models import Listing, Contribute
from .decorators import allowed_users
from .forms import OwnerForm, ListingForm
# Create your views here.


def register_page(request):
    if request.method == "POST":
        role = request.POST.get("role")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Check if passwords mathch
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, f"Username {username} already exists!.")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, f"Email {email} is being used by another user!.")
                    return redirect('register')
                else:
                    # Looks Good

                    user = User.objects.create_user(
                        username=username, password=password, email=email,
                        first_name=first_name, last_name=last_name)
                    if role == "customer":
                        group = Group.objects.get(name=role)
                        user.groups.add(group)

                    user.save()
                    messages.success(
                        request, f"You are now Registered & can log in!.")
                    return redirect('login')
                    # login after register
                    # auth.login(request,user)
                    # messages.success(request, f"You are now logged in!.")

        else:
            messages.error(request, "Passwords do not match!.")
            return redirect('register')

    return render(request, 'accounts/register.html')


def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            owner_group = Group.objects.get(name="owner")
            customer_group = Group.objects.get(name="customer")

            if user.groups.filter(name=owner_group):
                return redirect('profile')
            # if user.groups.filter(name=customer_group):
            elif user.groups.filter(name=customer_group):
                messages.success(
                    request, f"Welcome {username}, You are now logged in!.")
                return redirect('dashboard')
                
           
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')



@allowed_users(allowed_roles=['customer'])
def dashboard_page(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)




@allowed_users(allowed_roles=['owner'])
def account_settings(request):
  

    owner_info = request.user.owner
    
    form = OwnerForm(instance=owner_info)
    
    if request.method == 'POST':
        form = OwnerForm(request.POST, request.FILES,instance=owner_info)
        if form.is_valid():
            form.save()
        else:
            messages.error(
                    request, f"Something went wrong!. Please try again later, or contact us.")
  
    context = {
        'form': form

    }
    return render(request,'accounts/account_settings.html', context)



@allowed_users(allowed_roles=['owner'])
def add_listing(request):
    owner = request.user
    print(owner)
    listing_form = ListingForm(instance=owner)

    if request.method == 'POST':
        listing_form = ListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            

            listing_form.save()
            messages.success(
                    request, f"Thank you for posting!. We will update the information as soon as possible")
            return redirect('owner_dashboard')
        else:
            print("error==========")
          


    context = {
        'form': listing_form

    }
    return render(request,'accounts/add_listing.html', context)


@allowed_users(allowed_roles=['owner'])
def owner_dashboard(request):
    contributes = Contribute.objects.order_by(
        '-id').filter(username=request.user)

    context = {
        'contacts': contributes
    }

    return render(request, 'accounts/owner_dashboard.html', context)

def logout_page(request):
    auth.logout(request)
    messages.success(request, f"You have been logged out!.")

    return redirect('login')


# .\venv\Scripts\activate

def error_404(request, exception):
   context = {}
   return render(request,'404.html', context)

def error_500(request):
   context = {}
   return render(request,'500.html', context)