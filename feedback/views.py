from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.utils import simplejson

from feedback.forms import FeedbackForm

class leave_feedback(View):
    
    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        result = {"success":False,"message":"Something in the form submission failed, we're looking into it"}
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            request.user.message_set.create(message="Your feedback has been saved successfully.")
            
            result = {"success":True,"message":"Thank You"}
        return HttpResponse(simplejson.dumps(result), mimetype='application/json') 
    
