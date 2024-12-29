from django.contrib import admin
from django.urls import path, include
from events.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('events/', include('events.urls')),
    path('attendees/', include('attendee.urls')),
    path('tasks/', include('tasks.urls')),
    path('', homepage, name='home'),
    path('', include('events.urls')),
]