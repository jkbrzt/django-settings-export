from django.conf.urls import patterns

from . import views


urlpatterns = patterns(
    '',
    ('^$', views.render_ok),
    ('^error$', views.render_error),
)


