from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logged_out.html'}),
    url(r'^cms/', include('cms.urls', namespace='cms')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]