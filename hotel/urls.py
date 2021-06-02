from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='database', permanent=True), name='redirect'),
    path('admin/', admin.site.urls),
    path('database/', include('database_view.urls')),

]
