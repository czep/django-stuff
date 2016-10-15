from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #url(r'^polls/', include('polls.urls')),
    url(r'', include('apps.stuff.urls')),
    url(r'^admin/', admin.site.urls),
]
