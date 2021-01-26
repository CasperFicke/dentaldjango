from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.core.mail import send_mail

from .forms import SignUpForm, EditProfileForm

# Index view
def index(request):
  return render(request, 'index.html', {})

# Login view
def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, ('Succesfully logged in'))
      # Redirect to a success page.
      return redirect('index')
    else:
      messages.success(request, ('Error logging in. Please try again..'))
      return redirect('login')
  else:
    return render(request, 'authenticate/login.html', {})

# Logout view
def logout_user(request):
  logout(request)
  messages.success(request, ('Succesfully logged out'))
  # Redirect to a success page.
  return redirect('index')

# Register view
def register_user(request):
  if request.method == 'POST':
    #do something
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(request, username=username, password=password)
      login(request, user)
      messages.success(request, ("You're Registered"))
      return redirect('index')
  else:
    form = SignUpForm()
  context = {'form': form}
  return render(request, 'authenticate/register.html', context)

# edit profile view
def edit_profile(request):
  if request.method == "POST":
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, ("You successfully updated your profile"))
      return redirect('index')
  else:
    form = EditProfileForm(instance=request.user)
  context = {'form': form}
  return render(request, 'authenticate/edit_profile.html', context)

# change password view
def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(data=request.POST, user=request.user)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      messages.success(request, ("You successfully changed your password"))
      return redirect('index')
  else:
    form = PasswordChangeForm(user=request.user)
  context = {'form': form}
  return render(request, 'authenticate/change_password.html', context)

# contact view
def contact(request):
  # present the page after posting the form
  if request.method == "POST":
    message_name  = request.POST['message-name']
    message_email = request.POST['message-email']
    message       = request.POST['message']

    # send email
    send_mail(
      'email from website by ' + message_name, # subjext
      message, # mesage
      message_email, # from
      ['cficke@quicknet.nl'], # to
      fail_silently=False,
    )
    return render(
      request,
      'contact.html',
      {'message_name':  message_name}
    )
  else:
    # present the page
    return render(request, 'contact.html', {})

# about view
def about(request):
  return render(request, 'about.html', {})

# blog view
def blog(request):
  return render(request, 'blog.html', {})

# blog-details view
def blog_details(request):
  return render(request, 'blog-details.html', {})

# pricing view
def pricing(request):
  return render(request, 'pricing.html', {})

# service view
def service(request):
  return render(request, 'service.html', {})

# book appointment view
def book_appointment(request):
  return render(request, 'book_appointment.html', {})
