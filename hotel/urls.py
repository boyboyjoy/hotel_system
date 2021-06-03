from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='app/', permanent=True), name='redirect'),
    path('admin/', admin.site.urls),
    path('app/', include('database_view.urls')),
]
