from django.shortcuts import render, redirect
from main.models import Ip
import datetime, getpass

def index(request):
	'''try:
		ex = Ip.objects.get(id = 0)'''
	context = {
		'IPs': Ip.objects.all(),
	}
	'''except:
		context = {
			'IPs': 0,
		}'''
	return render(request, 'main/main.html', context)

def set_ip(request):
	if request.POST.get('ip') != '' and request.POST.get('name') != '':
		ip = Ip(ip = request.POST.get('ip'), time = datetime.datetime.now(), name = request.POST.get('name'))
		ip.save()
	return redirect('http://localhost:8000/')

def delete_ip(request):
	try:
		ip = Ip.objects.get(name = request.POST.get('name'))
		ip.delete()
	except:
		pass

	return redirect('http://localhost:8000/')
