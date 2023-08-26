try:
    from django.urls import path
except ImportError:
    # Old Django
    from django.conf.urls import url as path

from . import views


urlpatterns = [
    path('', views.render_ok),
    path('rename', views.render_ok_rename),
    path('error', views.render_error),
    path('list', views.render_list),
]
