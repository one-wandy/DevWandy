from django.shortcuts import redirect
from django.urls import reverse
from . import models


class Options:
      def List_Redirect(self):
            URL = reverse('customer:list-customer')
            return redirect(URL)