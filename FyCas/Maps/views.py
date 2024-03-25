from django.shortcuts import render
from django.views.generic import *
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
import os
from datetime import datetime



    
class Maps(TemplateView):
      template_name = "maps/location.html"
