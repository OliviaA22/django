from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  mymembers = Member.objects.all().values()

  # When using the filter method to fetch data, below method is used:
  # mydata = Member.objects.filter(firstname='Emil').values()
  # | Member.objects.filter(firstname='Tobias').values()

  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


# Queryset filter method using the Q expression
# def testing(request):
#   mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# Queryset filter method using the field lookups which are
# keywords that represents specific SQL keywords. They must be specified with the
# fieldname, followed by 2 underscore and then the keyword.
# example: __startswith, __endswith, etc.

# def testing(request):
#  mydata = Member.objects.filter(firstname__startswith='L').values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# Queryset order_by() method:
# mydata = Member.objects.all().order_by('firstname').values()

# Multiple order_by:
# mydata = Member.objects.all().order_by('lastname', '-id').values()

