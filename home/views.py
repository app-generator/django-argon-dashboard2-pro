from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# Uncomment to force login in all cases
# @login_required(login_url='/accounts/basic-login/')
def index(request):

    # Page from the theme 
    return render(request, 'pages/dashboards/default.html')
