from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Register a new user"""
	if request.method != 'POST':
		#show blank register form
		form = UserCreationForm()
	else:
		#process the filled form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#authorize the user and direct him to the main page
			login(request, new_user)
			return redirect('learning_logs:index')

	#show blank or invalid form
	context = {'form' : form}		
	return render(request, 'registration/register.html', context)