from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Quote
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'cur_user': User.objects.get(id = request.session['id']),
        'favorite_quotes': Quote.objects.filter(quotelist = request.session['id']),
        'all_quotes': Quote.objects.exclude(quotelist = request.session['id']),
    }

    return render(request,'main_app/home.html', context)


def create(request):

    results = Quote.objects.validate(request.POST)
    if len(results['errors']) > 0:
        for error in results['errors']:
            messages.error(request,error)
        return redirect('/main/home')

    else:
        logged_user = User.objects.get(id = request.session['id'])
        new_quote = Quote.objects.create(
            quoted_by = request.POST['quoted_by'],
            message = request.POST['message'],
            created_by = logged_user
        )
        logged_user.quotes_made.add(new_quote)
        logged_user.quotelist.add(new_quote)

    return redirect('/main/home')

def removefromlist (request, id):
    quote = Quote.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    user.quotelist.remove(quote)
    return redirect('/main/home')

def addtolist(request, id):
    quote = Quote.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    user.quotelist.add(quote)
    return redirect('/main/home')

def show(request, id):
    context = {
        'quote': Quote.objects.get(id = id)
    }
    return render(request, 'main_app/show.html', context)