from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from inst import urls
from restapi import settings

urlpatterns = [
    path('', RedirectView.as_view(url='login')),
    path('', include('rest_auth.urls')),
    path('', include(urls)),
    path('registration/', include('rest_auth.registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
