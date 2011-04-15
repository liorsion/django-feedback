from django.conf import settings

from feedback.forms import FeedbackForm

def feedback_form(request):
    feedback_form = None
    if request.user.is_authenticated():
        feedback_form = FeedbackForm()
    return {'feedback_form': feedback_form, 'FEEDBACK_CHOICES' : settings.FEEDBACK_CHOICES}