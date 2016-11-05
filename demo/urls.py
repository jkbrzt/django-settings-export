from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.render_ok),
    url('^rename$', views.render_ok_rename),
    url('^error$', views.render_error),
]


