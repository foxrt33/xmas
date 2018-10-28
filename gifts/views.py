from django.shortcuts import render
from django.db.models import QuerySet
import datetime

from .models import Gift


# Create your views here.

def index(request):
    """ The home page for the gifts """
    return render(request, 'gifts/index.html')


def gifts_for_current_year(request):
    """ Show all gift assignments for the current year """
    gifts = []
    current_year = datetime.datetime.now().year
    for gift in Gift.objects.order_by('name_from'):
        if gift.year == current_year:
            gifts.append(gift)
    context = {'gifts': gifts}
    return render(request, 'gifts/gifts.html', context)


def all_gifts(request):
    """ Show all gift assignments recorded, ordered
    by year and giver """
    gifts_by_year = Gift.objects.order_by('-year', 'name_from')
    y = None
    entries = []
    all_entries = []
    for g in gifts_by_year:
        if not y:
            y = g.year
        if y != g.year:
            all_entries.append({'year': y, 'gifts': entries})
            entries = []
            y = g.year
        entries.append(g)
    all_entries.append({'year': y, 'gifts': entries})
    context = {'gifts_by_year': all_entries}
    return render(request, 'gifts/gifts_all.html', context)


def gifts_by_giver(request, name_from):
    """ Show all gifts by from person """
    gifts_by_from = Gift.objects.filter(name_from=name_from).order_by('-year')
    context = {'gifts': gifts_by_from, 'name_from': name_from}
    return render(request, 'gifts/gifts_by_from.html', context)


def gifts_by_recipent(request, name_to):
    """ Show all gifts by TO person """
    gifts_by_to = Gift.objects.filter(name_to=name_to).order_by('-year')
    context = {'gifts': gifts_by_to, 'name_to': name_to }
    return render(request, 'gifts/gifts_by_to.html', context)

def gifts_by_person(request, name):
    gifts_from = Gift.objects.filter(name_from=name).order_by('-year')
    gifts_to = Gift.objects.filter(name_to=name).order_by('-year')
    context = {'gifts_from': gifts_from, 'gifts_to': gifts_to, 'profile_name': name}
    return render(request, 'gifts/gifts_by_person.html', context)
