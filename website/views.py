from django.shortcuts import render
from django.core.mail import send_mail

# Index view
def index(request):
  return render(request, 'index.html', {})

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
