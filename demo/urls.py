from django.conf.urls import patterns

from . import views


urlpatterns = patterns(
    '',
    ('^$', views.render_ok),
    ('^rename$', views.render_ok_rename),
    ('^error$', views.render_error),
)


