from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from recipe.models import *
import json


def home(request):
	recipies = Recipe.objects.all()
	return render(request,'index.html',{"recipies":recipies})
 
def recipe(request,pk):
	recipe = Recipe.objects.get(pk=pk)
	return render(request,'recipie.html',{"recipe":recipe})

def findIgrident(name):
	try:
		return Ingredient.objects.get(name=name.lower())
	except Exception, e:
		print e
		newIng = Ingredient(name=name)
		newIng.save()
		return newIng

def addMessuredIn(newItem,messured):
	try:
		messured = Messurments.objects.get(name=messured.lower())
	except Exception, e:
		messured = Messurments(name=messured)
		messured.save()
		print e
	newItem.mesured_in = messured


def addAmmount(newItem,ammount):
	try:
		newItem.ammount_number = float(ammount)
	except Exception, e:
		newItem.ammount_string = ammount

def makeStep(note,order):
	out = Step(order=order,note=note)
	out.save()
	return out


def add(request):
	if request.POST:
		print request.POST.get('title', '')
		print request.POST.get('description', '')
		# newRecipie = Recipe()
		for a in range(0,99):
			name = request.POST.get('name_%d'%a, '')
			step = request.POST.get('order_%d'%a,'')
			if(name):
				name = findIgrident(name)				
				newItem = Ingredient_Item(Ingredient= name)
				addAmmount(newItem,request.POST.get('ammount_%d'%a, ''))
				addMessuredIn(newItem,request.POST.get('messured_%d'%a,''))
				print newItem
			if(step):
				newStep = makeStep(request.POST.get('note_%d'%a,''),step)
				print newStep
		# for key, value in request.POST.iteritems():
		# 	print key, value
		# title = request.POST.get('title', '')
		return render(request,'add.html',{"msg":"added recipe"})
	return render(request,'add.html',{"msg":"ready to add recipe"})

