from django.shortcuts import render
from django.http import HttpResponseRedirect

import requests

# Create your views here.

def send_mail(name, email, subject, message):
	
    Message = 'name : ' + str(name) + "\n\n" + 'email : ' + str(email) + '\n\n' + 'message : ' + str(message) + '\n\n'
    
    From = str(name) + " <career@zebu.ai>"
    return requests.post(
		"https://api.mailgun.net/v3/zebu.ai/messages",
		auth=("api", "a4de5ccfb8822bbe4861dacc4f8cc6b1-4b1aa784-9d61b6ad"),
		data={"from": From,
			"to": ["sagarmohanty2k00@gmail.com"],
			"subject": subject,
			"text": Message})

def send(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    send_mail(name, email, subject, message)

    return HttpResponseRedirect('/')