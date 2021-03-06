from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from bolsa import views as core_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.inicio, name='inicio'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^nueva_oportunidad/$', core_views.nueva, name='nueva_oportunidad'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]