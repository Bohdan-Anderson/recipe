from django.db import models
from django.template.defaultfilters import slugify


class Messured_in(models.Model):
	name = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)	
	def __unicode__(self):
		return self.name	

class Messurments(models.Model):
	name = models.CharField(max_length=500)
	notes = models.TextField(max_length=1000, blank=True)	
	types = models.ForeignKey(Messured_in,blank=True,null=True)
	created = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name
	def save(self,*args, **kwargs):
		self.name = self.name.lower()
		super(Messurments, self).save(*args, **kwargs)		

class Ingredient(models.Model):
	name = models.CharField(max_length=500)
	name_other = models.CharField(max_length=500,blank=True,null=True)
	mesured_in = models.ForeignKey(Messured_in, blank=True,null=True)
	notes = models.TextField(max_length=1000, blank=True)
	slug = models.SlugField(blank=True)
	created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	def save(self,*args, **kwargs):
		self.slug = slugify(self.name)
		self.name = self.name.lower()
		super(Ingredient, self).save(*args, **kwargs)	

class Ingredient_Item(models.Model):
	Ingredient = models.ForeignKey(Ingredient)
	mesured_in = models.ForeignKey(Messurments, blank=True,null=True)
	ammount_number = models.FloatField(blank=True,null=True)
	ammount_string = models.TextField(max_length=1000, blank=True)
	created = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return "%s item" %self.Ingredient

class Step(models.Model):
	order = models.IntegerField(default=99,blank=True,null=True)
	note = models.TextField(max_length=1000, blank=True)
	highLight = models.TextField(max_length=1000, blank=True)
	created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.note

class FoodType(models.Model):
	title = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True)
	
	def __unicode__(self):
		return self.title

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(FoodType, self).save(*args, **kwargs)

class Ethnicity(models.Model):
	title = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.title

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Ethnicity, self).save(*args, **kwargs)

class Recipe(models.Model):
	title = models.CharField(max_length=500)
	title_other = models.CharField(max_length=500,blank=True,null=True)

	note = models.TextField(max_length=1000, blank=True)

	ingredients = models.ManyToManyField(Ingredient_Item)
	steps = models.ManyToManyField(Step)

	time_preperation = models.FloatField(blank=True,null=True)
	time_cooking = models.FloatField(blank=True,null=True)
	time_total = models.FloatField(blank=True,null=True)

	foodType = models.ManyToManyField(FoodType,blank=True)
	ethnicity = models.ManyToManyField(Ethnicity,blank=True)

	created = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.title

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Recipe, self).save(*args, **kwargs)

	# title = models.CharField(max_length=500,blank=True,null=True)
	# addl_mo_fee = models.IntegerField(blank=True,null=True) 
	# addr = models.TextField(max_length=1000, blank=True)
	# num_max = models.FloatField()
	# community = models.ManyToManyField('listitem',related_name='community', blank=True,null=True)
	# slug = models.SlugField(blank=True)
	# created = models.DateTimeField(auto_now=True)


	# def __unicode__(self):
	# 	return self.text

	# def save(self,*args, **kwargs):
	# 	self.slug = slugify(self.title)
	# 	super(NeightbourHood, self).save(*args, **kwargs)

	# class Meta:
	# 	ordering = ['text']