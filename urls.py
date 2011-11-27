from django.conf.urls.defaults import *
from django.views.generic import list_detail, DetailView, ListView
from c10shop.mystore.models import Catalog, Category, Recipe, Purchase
from c10shop.mystore.views import buyStuff, cancelPurchase, deliverContent, view_recipe, myStuff
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
import registration
from django.contrib.auth.views import password_reset

from django.contrib import admin
admin.autodiscover()

recipe_list = {
    'queryset': Recipe.objects.all(),
    'template_name': 'recipes/recipe_list.html'
}


def recipes_by_category(request, category):
    #Look up the category and raise 404 if not found
    category = get_object_or_404(Category, name__iexact=category)
    name ='recipe-by-category'
    queryset = Recipe.objects.filter(category=category).exclude(purchase__purchaser=request.user)
    #queryset = queryset.exclude( Purchase.objects.filter(purchaser=request.user) )
    #Use the object_list view to do the heavy lifting
    return list_detail.object_list(
        request,
        queryset,
        template_name = "recipes/recipe_by_category.html",
        template_object_name = 'recipe',
        extra_context = {'category': category}
    )
    

urlpatterns = patterns('',
    
    url(r'^recipes/(?P<category>(\w+))/$', recipes_by_category),
    
    url(r'^recipes/view/(?P<slug>[^\.]+).html', view_recipe, name='view_recipe'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^xhr_test$','c10shop.mystore.views.xhr_test'),
    url(r'^$', direct_to_template, {'template': 'home.html' }),
    url(r'^index/$', direct_to_template, {'template': 'home.html' }),
    url(r'^paypal/(\w+)/$', buyStuff),
    url(r'^success', deliverContent),
    url(r'^cancel', cancelPurchase),
    url(r'^accounts/', include('registration.urls')),
    url(r'^accounts/mystuff/$', myStuff),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)