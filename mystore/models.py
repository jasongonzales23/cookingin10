from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Catalog(models.Model):
    name= models.CharField(max_length=255)
    slug= models.CharField(max_length=255)
    description= models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name

class Category(models.Model):
    catalog = models.ForeignKey('Catalog')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name,
                                     self.parent.name,
                                     self.name)
        return u'%s: %s' % (self.catalog.name, self.name)


class Recipe(models.Model):
    category = models.ForeignKey('Category', related_name='categories')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    prodID = models.CharField(max_length=30)
    description= models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails', blank=True)
    video = models.FileField(upload_to='uploads/videos')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateTimeField(default=datetime.now())
    ingredient_total_cost = models.CharField(max_length=30)
    servings = models.CharField(max_length=30)
    cost_per_serving = models.CharField(max_length=30)
    

    def __unicode__(self):
        return u'%s' % (self.name)

    @models.permalink
    def get_absolute_url(self):
	return ('view_recipe', (), {'slug': self.slug})

class RecipeDetail(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.CharField(max_length=255)
    amount = models.CharField(max_length=30)
    cost = models.CharField(max_length=30)
    
    
class Purchase(models.Model):
    recipe = models.ForeignKey(Recipe)
    purchaser = models.ForeignKey(User)
    purchased_date = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
	return u'%s %s' % (self.recipe.name, self.recipe.price)

