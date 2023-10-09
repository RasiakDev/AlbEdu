from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'parents', views.ParentView, 'parent')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('app/', include('app.urls'))
]