from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Registration
from django.urls import reverse

# Create your views here.
def index(req):
      add_members =Registration.objects.all().values()
      template=loader.get_template('index.html')
      context={
            'add_members': add_members,
      }
      return HttpResponse(template.render(context,req))
def add(req):
      template=loader.get_template('addr.html')
      return HttpResponse(template.render({},req))
def addrecord(req):
      x =req.POST['first_name']
      y =req.POST['last_name']
      add_members=Registration(first_name=x,last_name=y)
      add_members.save()
      return HttpResponseRedirect(reverse('index'))
def delete(req,id):
      add_members=Registration.objects.get(id=id)
      add_members.delete()
      return HttpResponseRedirect(reverse('index'))

def update(req,id):
      add_members=Registration.objects.get(id=id)
      template=loader.get_template('update.html')
      context={
            'add_members':add_members
      }
      return HttpResponse(template.render(context,req))
def updaterecord(req,id):
      first_name=req.POST['first_name']
      last_name=req.POST['last_name']
      add_members=Registration.objects.get(id=id)
      add_members.first_name=first_name
      add_members.last_name=last_name
      add_members.save()
      return HttpResponseRedirect(reverse('index'))
