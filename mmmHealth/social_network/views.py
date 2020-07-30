from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core import mail
from django.utils.translation import gettext as _




from .forms import RegisterForm
from .models import User


def index(request):

    context = {'first_name': _('Hello World!'), 'last_name': _('Today is 25 November 2018!')}
    return render(request, 'register_page.html', context)

def user_detail(request, user_id):
    user_instance = get_object_or_404(User, pk=user_id)
    return render(request, 'user_detail.html', {'user': user_instance})


def register_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_instance = User.objects.create()
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user_instance.first_name = form.cleaned_data['first_name']
            user_instance.last_name = form.cleaned_data['last_name']
            user_instance.email = form.cleaned_data['email']
            user_instance.country = form.cleaned_data['country']
            user_instance.phone_number = form.cleaned_data['phone_number']
            user_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register_page.html', {'form': form})


def email_test(request):
    connection = mail.get_connection()

    # Manually open the connection
    connection.open()

    email1 = mail.EmailMessage(
    'Hello',
    'Body goes here',
    'from@example.com',
    ['K0jnCZ@gmail.com'],
    connection=connection,
    )

    email1.send() # Send the email

    connection.close()
    return render(request, 'test_email.html', {'email': 'K0jnCZ@gmail.com'})
