from django.contrib import admin
from django.conf.urls.defaults import *
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    
    model = Feedback
    change_form_template = "feedback/view_feedback.html"
    
    list_display = ['user', 'message', 'time', 'type', 'status', 'view']
    search_fields = ['user', 'message']
    list_filter = ['type', 'time', 'status']
    actions = ['mark_fixed']
    
    def view(self, obj):
        return "<a href='%s'>View</a>" % obj.get_absolute_url()
    
    view.allow_tags = True
    
    def get_urls(self):
        urls = super(FeedbackAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^view/(?P<feedback_id>\d+)/$', self.admin_site.admin_view(self.view_feedback), name='view-feedback'),
        )
        return my_urls + urls
        
    def view_feedback(self, request, feedback_id):
        return self.change_view(request, feedback_id)
    
    def mark_fixed(self,modeladmin, request, queryset):
        rows_updated = queryset.update(status='F')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as fixed." % message_bit)
    
    mark_fixed.short_description = "Mark selected feedback as fixed"
    
admin.site.register(Feedback, FeedbackAdmin)

admin.site.index_template = 'feedback/index.html'