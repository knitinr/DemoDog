from DemoDog import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DemoDog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#enter_article
    url(r'^$', views.index),
    url(r'^enter_article', views.enter_article),
    url(r'^accounts/login', views.login),
    url(r'^accounts/logout', views.logout),
    url(r'^accounts/auth', views.authfunc),
    url(r'^accounts/logged_in', views.logged_in),
    url(r'^accounts/invalid', views.invalid_login),
    url(r'^admin/', include(admin.site.urls)),
)
