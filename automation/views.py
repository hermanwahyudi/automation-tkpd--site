from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.http import HttpResponse

#from .models import Greeting

# Create your views here.
def index(request):
	if 'sess_key' not in request.session:
		c = {}
		c.update(csrf(request))
		return render(request, 'login1.html', c)
	else:
		var = {}
		if request.user.is_authenticated():
			var = request.session['sess_email']
		return render_to_response('dashboard.html', {'email':var})

def login(request):
	if request.POST:
		email = request.POST['email']
		passw = request.POST['passw']
		data_email = ['tkpd.qc@gmail.com', 'herman.wahyudi02@gmail.com']
		is_found_email = False
		for c in data_email:
			if c == email:
				is_found_email = True
				break
		if is_found_email and passw == "1234asdf":
			request.session['sess_key'] = email + "&" + passw
			request.session['sess_email'] = email
			request.session['sess_passw'] = passw
			return redirect('/')
		else:
			c = {}
			c.update(csrf(request))
			error = "Email or password is incorrect!"
			c.update({'error':error})
			return render_to_response('login1.html', c)
	else:
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
