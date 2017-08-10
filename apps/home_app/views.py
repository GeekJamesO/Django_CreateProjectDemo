# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    # print """I am inside the  the index function
    #    of the views...  """
    context = {
        'num':2,
        'students': ['Olivier','zarceh','jaims','landece','re']
    }
    request.awesome = "Class is awesome"
    return render(request, "home_app/index.html", context)
