from django.contrib import admin
from django.urls import path, include
from vtools_clone.accounts.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('filters/', include('itemfilters.urls')),
    path('', home_view, name='home')
]
