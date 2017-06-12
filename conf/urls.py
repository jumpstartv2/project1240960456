"""
Django Macros Url:
    Pre-defined Macros Url regex variables:
        slug - [\w-]+
        year - \d{4}
        month - (0?([1-9])|10|11|12)
        day - ((0|1|2)?([1-9])|[1-3]0|31)
        id - \d+
        pk - \d+
        page - \d+
        uuid - [a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12}

    Defining your own regex variables with macrosurl:
        macrosurl.register('myhash', '[a-f0-9]{9}')
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'conf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="_jumpstart.html")),
    url(r'^admin/', include(admin.site.urls)),
)
