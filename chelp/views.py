from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
	if request.method == "POST":
		state = request.POST.get("inputState")
		service = request.POST.get("inputService")
		print(service)
		if service == 'Beds':
			data = models.covidHelp.objects.filter(state=state ).filter(service=service).order_by('-created')
			return render(request, 'index.html',{'beds':data})
		elif service == 'Oxygen':
			data = models.covidHelp.objects.filter(state=state ).filter(service=service).order_by('-created')
			return render(request, 'index.html',{'oxygen':data})
		elif service == 'Plasma':
			data = models.covidHelp.objects.filter(state=state ).filter(service=service).order_by('-created')
			return render(request, 'index.html',{'plasma':data})
		elif service == 'Remdesivir':
			data = models.covidHelp.objects.filter(state=state ).filter(service=service).order_by('-created')
			return render(request, 'index.html',{'remdesivir':data})

	return render(request, 'index.html')

def rem (request):
	if request.method == "POST":
		
		if request.POST.get("form_type") == 'stateForm':
			state = request.POST.get("inputState")
			data = models.covidHelp.objects.filter(state=state ).filter(service="Remdesivir").order_by('-created')
			return render(request, 'rem.html',{'remdesivir':data})
		if request.POST.get("form_type") == 'searchForm':

			search = request.POST.get("search").lower()
			data = models.covidHelp.objects.filter(city=search ).filter(service="Remdesivir").order_by('-created')
			return render(request,'rem.html',{'remdesivir':data})
	return render(request,'rem.html')

def bed (request):
	if request.method == "POST":
	
		if request.POST.get("form_type") == 'stateForm':
		
			state = request.POST.get("inputState")
			data = models.covidHelp.objects.filter(state=state ).filter(service="Beds").order_by('-created')
			return render(request, 'beds.html',{'beds':data})
		if request.POST.get("form_type") == 'searchForm':
		
			search = request.POST.get("search").lower()
			data = models.covidHelp.objects.filter(city=search ).filter(service="Beds").order_by('-created')
			return render(request,'beds.html',{'beds':data})
	return render(request,'beds.html')

def oxygen(request):
	if request.method == "POST":
		
		if request.POST.get("form_type") == 'stateForm':
			state = request.POST.get("inputState")
			data = models.covidHelp.objects.filter(state=state ).filter(service="Oxygen").order_by('-created')
			return render(request, 'oxy.html',{'oxygen':data})
		if request.POST.get("form_type") == 'searchForm':
			print('in search')
			search = request.POST.get("search").lower()
			data = models.covidHelp.objects.filter(city=search ).filter(service="Oxygen").order_by('-created')
			return render(request,'oxy.html',{'oxygen':data})
	return render(request,'oxy.html')

def plasma(request):
	if request.method == "POST":
		
		if request.POST.get("form_type") == 'stateForm':
			
			state = request.POST.get("inputState")
			data = models.covidHelp.objects.filter(state=state ).filter(service="Plasma").order_by('-created')
			return render(request, 'plasma.html',{'blood':data})
		if request.POST.get("form_type") == 'searchForm':
			
			search = request.POST.get("search").lower()
			data = models.covidHelp.objects.filter(city=search ).filter(service="Plasma").order_by('-created')
			return render(request,'plasma.html',{'blood':data})
	return render(request,'plasma.html')

def addNew(request):
	if request.method== "POST":
		state= request.POST.get("inputState")
		service = request.POST.get("inputService")
		plasma = request.POST.get("inputPlasma") 
		name = request.POST.get("name") 
		details = request.POST.get("details") 
		mobile = request.POST.get("mobile") 
		city = request.POST.get("city").lower()
		hospital = request.POST.get("hospital")
		blood=  request.POST.get("inputPlasma")
		if service == "Beds" and hospital is not None:
			data= models.covidHelp(person_name=name, person_detail= details, person_mobile=mobile, state=state, city=city, service=service, hospital= hospital, status = "Active")
			data.save()
			return redirect('add')
		if service == 'Remdesivir':
			data= models.covidHelp(person_name=name, person_detail= details, person_mobile=mobile, state=state, city=city, service=service, status = "Active")
			data.save()
			return redirect('add')
		if service == 'Plasma' and blood is not None:
			print('in plasma')
			data= models.covidHelp(person_name=name, person_detail= details, person_mobile=mobile, state=state, city=city, service=service, blood_group=blood, status = "Active")
			data.save()
			print('plasma saved')
			return redirect('add')

		if service == 'Oxygen':
			data= models.covidHelp(person_name=name, person_detail= details, person_mobile=mobile, state=state, city=city, service=service, status = "Active")
			data.save()
			return redirect('add')

	return render(request,'add.html')

def contact(request):
	return render(request,'contact_us.html')