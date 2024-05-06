from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

def HomePage(request):
    return render(request, 'home.html')

def validate_password(password, user=None):
            # Check if the password has at least 3 characters
    if len(password) < 3:
        raise ValidationError('Password must be at least 3 characters long.')

    # Check if the password has at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError('Password must contain at least one special character.')

    # Check if the password has at least one capital alphabetical letter
    if not any(char.isupper() for char in password):
        raise ValidationError('Password must contain at least one capital alphabetical letter.')

def SignupPage(request):
    if request.method == 'POST':
        #18 added
        User = get_user_model()
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # my_user = CustomUser.objects.create_user(username=uname, email=email, password=pass1)
            # my_user.save()
            # return render(request,'authentication/login.html')
            try:
                # Validate password
                validate_password( pass1, user=User(username=uname))
            except ValidationError as e:
                return HttpResponse(", ".join(e.messages))
            
            # If password validation passes, create the user
            user = User.objects.create_user(username=uname, email=email, password=pass1)
            
            return redirect('/login/')
    return render(request, 'authentication/signup.html')


def LoginPage(request):
    '''user = authenticate(email='hello123@gmail.com', password='123456')
    print(user)'''

    if request.method == 'POST':
        email = request.POST.get('email')  # Change 'username' to 'email'
        password = request.POST.get('pass')
        print(f"Email: {email}, Password: {password}")
        print(f"Request: {request}")

        user = authenticate(request, username=email, password=password)
        print(f"Authenticated User: {user}")

        if user is not None:
            login(request, user)
            return HttpResponse("Email or Password is correct!!!")
        else:
            return HttpResponse("Email or Password is incorrect!!!")

    return render(request, 'authentication/login.html')






