from django.conf.urls import url
from social_django.urls import urlpatterns, app_name
from django.urls import path,include
from . import views


urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^registro/$',views.registroPersona,name="registro"),
    url(r'^login/$',views.ingreso,name="login"),
    url(r'^olvido/$',views.olvido,name="olvido"),
    url(r'^restablecer/$',views.restablecer,name="restablecer"),
    url(r'^registroPerro/$', views.registroPerro, name='registroPerro'),
    url(r'^registroAdmin/$', views.registroAdmin, name='registroAdmin'),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^Adoptar/$',views.registroPerro,name="adoptaPerro"),
    url('', include('social_django.urls', namespace='social')),
    url(r'^fb/$',views.social,name="fb"),
    url('accounts/', include('allauth.urls')),
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'