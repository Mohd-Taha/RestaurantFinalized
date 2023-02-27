from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve
from django.urls import path
from .views import product



urlpatterns = [
    path('index/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('service/',views.service),
    path('booking/',views.booking),
    path('menu/',views.menu),
    path('team/',views.team),
    path('review/',views.review),
    path('orders/',views.orders),
    path('contact/sendmail',views.sendmail),
    path('starterrs/<int:id>',views.product)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]

