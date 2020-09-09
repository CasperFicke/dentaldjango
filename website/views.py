from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
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