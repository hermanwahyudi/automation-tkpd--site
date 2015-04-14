from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
	if 'sess_key' not in request.session:
		c = {}
		c.update(csrf(request))
		return render(request, 'login.html', c)
	else:
		var = {}
		if not request.user.is_authenticated():
			var = request.session['sess_email']
		return render_to_response('home.html', {'email':var})

def login(request):
	email = request.POST['email']
	passw = request.POST['passw']
	if email == "tkpd.qc@gmail.com" and passw == "1234asdf":
		request.session['sess_key'] = email + "&" + passw
		request.session['sess_email'] = email
		request.session['sess_passw'] = passw
	return redirect('/')

def logout(request):
	del request.session['sess_key']
	return redirect("/")

"""
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
"""
