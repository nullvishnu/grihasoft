from django.shortcuts import render

def user_template(request,template_name):
    template_name = template_name
    if template_name is not '':
         return render(request, template_name+".html")

def user_loginui(request):
    return render(request, 'login.html')

def user_signupui(request):
    return render(request, 'signup.html')