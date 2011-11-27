from django.conf.urls.defaults import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from c10shop.mystore.models import Recipe, Purchase, RecipeDetail
import urllib
import urllib2
import urlparse
import string
import models

def buyStuff(request, itemID):
    #TODO need to check and make sure they haven't purchased this already yet!
    #try:
        #existing = Purchase.obects.get(the iD??)
    #except Purchase.DoesNotExist:
    def _params():
        VERSION = "65.1"
        #TODO move these back to settings.py and import here
        #these need to be reused for GetExpressCheckoutDetails & DoExpressCheckoutPayment
        #PAYPAL_RECEIVER_EMAIL = "merch_1321122587_biz@gmail.com",
        #PAYPAL_TEST = True,           # Testing mode on
        USER = "merch_1321122587_biz_api1.gmail.com"     # Get from PayPal
        PWD = "1321122611"
        SIGNATURE= "AgliXkknNsMGE4qabSbkbusAhtHjA3NseYOuN07jXzJMo4L-x88d9Lxn"
        #SITE_DOMAIN = "http://127.0.0.1:8000/",
    
        # Single-item purchase these are needed to initiate the process with paypal
        METHOD = "SetExpressCheckout"
        RETURNURL = "http://127.0.0.1:8000/success"
        CANCELURL = "http://127.0.0.1:8000/cancel"
        PAYMENTREQUEST_0_PAYMENTACTION = "Sale"
        #PAYMENTREQUEST_0_NOTIFYURL = "YOUR_URL/YourPayPalListener.php", #OPTIONAL - for database integration, back office integration, scalability, etc
        PAYMENTREQUEST_0_AMT = "$3" #TODO pull these from the product model
        PAYMENTREQUEST_0_CURRENCYCODE = "USD"
        PAYMENTREQUEST_0_ITEMAMT = "$3"
        L_PAYMENTREQUEST_0_NAME0 = "Recipe Video"
        L_PAYMENTREQUEST_0_NUMBER0 = itemID
        L_PAYMENTREQUEST_0_AMT0 = "$3"
        L_PAYMENTREQUEST_0_QTY0 = "1"
        L_PAYMENTREQUEST_0_ITEMCATEGORY0 = "Digital"
        #Since it's a digital good (and not physical), we don't need a shipping address.
        REQCONFIRMSHIPPING = "0"
        NOSHIPPING = "1"
        PARAMS = vars()
        return PARAMS
    
    def _parse_response(response):
        """Turn the PayPal response into a dict"""
        response_tokens = {}
        for kv in response.split('&'):
            key, value = kv.split("=")
            response_tokens[key] = urllib.unquote(value)
        return response_tokens
    
    #encode the data with urllib
    data = urllib.urlencode(_params())

    #send it to the server
    response = urllib2.urlopen("https://api-3t.sandbox.paypal.com/nvp", data).read()
    response_tokens = _parse_response(response)
    token = response_tokens['TOKEN']

    return HttpResponseRedirect("https://www.sandbox.paypal.com/incontext?token=" + token)
    
#TODO, need to make success & fail functions/views
def deliverContent(request):
    token = request.GET['token']
    payerID = request.GET['PayerID']
    
    def _params(token):
        VERSION = "65.1"
        #TODO move these as part of refactoring
        USER = "merch_1321122587_biz_api1.gmail.com"
        PWD = "1321122611"
        SIGNATURE= "AgliXkknNsMGE4qabSbkbusAhtHjA3NseYOuN07jXzJMo4L-x88d9Lxn"
    
        # Single-item purchase these are needed to initiate the process with paypal
        METHOD = "GetExpressCheckoutDetails"
        TOKEN = token
        PARAMS = vars()
        return PARAMS
    
    def _parse_response(response):
        """Turn the PayPal response into a dict"""
        response_tokens = {}
        for kv in response.split('&'):
            key, value = kv.split("=")
            response_tokens[key] = urllib.unquote(value)
        return response_tokens
    #encode the data with urllib
    data = urllib.urlencode(_params(token))
    #send it to the server
    response = urllib2.urlopen("https://api-3t.sandbox.paypal.com/nvp", data).read()
    response_tokens = _parse_response(response)
    prodID = response_tokens['L_PAYMENTREQUEST_0_NUMBER0']
    #add this video to a purchases table along with the dg_cookie_check
    recipe = get_object_or_404(Recipe, prodID = prodID)
    purchase = Purchase(recipe=recipe, purchaser=request.user, token=response_tokens['TOKEN'] )
    purchase.save()
    #find the url somehow
    #send the user to the page for the video
    #don't forget tot close the modal inject the js?
    return HttpResponse(prodID)

def cancelPurchase(request):
    token = request.GET #"Cancelled. Thanks! " + token['token']
    #need to write some code to remove the PPDGFrame element quite easy actually
    return HttpResponse('<h1>OK then</h1>')

@login_required
def view_recipe(request, slug):
    context = {'recipe': get_object_or_404(Recipe, slug=slug)}
    recipe = get_object_or_404(Recipe, slug=slug )
    detail_list = RecipeDetail.objects.filter(recipe=recipe)
    try:
        purchased = Purchase.objects.get( recipe=recipe, purchaser=request.user )
        return render_to_response('recipes/recipe_detail.html',
            {'detail_list': detail_list},
            context_instance=RequestContext(request, context)
        )
    except Purchase.DoesNotExist:
        #need a view for people who hit this link but have not bought it yet
        return HttpResponse('no dice')
        
    
@login_required
def myStuff(request):
    #p = get_object_or_404(Purchase)
    #whatever = Purchase.objects.filter(purchaser=request.user)
    purchase_list = Purchase.objects.filter(purchaser=request.user)
    return render_to_response('recipes/my_stuff.html',
        {'purchase_list': purchase_list},
        context_instance=RequestContext(request)
    )
    #return HttpResponse(whatever)