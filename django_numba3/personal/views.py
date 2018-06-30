from django.shortcuts import render, redirect
from personal.models import Stories
from personal.forms import StoriesForm
import datetime



def index(request):
	return render(request, 'personal/home.html')

def write(request):
	return render(request, 'personal/basic.html', {'content':['hello you cannot contact me for now :3', 'Geronyl']})

def writing(request):
	print "Hello Form"
	title = request.POST["title"]
	body = request.POST["body"]
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	new_story = Stories(title = title, date=date, body=body)
	new_story.save()
	return redirect('/stories/')

def update(request):
	return render(request, 'personal/update.html')

def updating(request, id):
	if request.method == 'POST':
		
		
		title = request.POST["title"]
		body = "<-UPDATED-> \n" + request.POST["body"]
		newdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		
		a = Stories.objects.get(id = id)
		a.title = title
		a.body = body
		a.date = newdate
		a.save()
		
		return redirect('/stories/')



def stories(request):
	return render(request,'personal/stories.html')


def delete(request, id):
	e=Stories.objects.get(id=id)
	e.delete()
	return redirect('/stories/')