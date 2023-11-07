from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # new
from django.views.generic.base import RedirectView



# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'parents', views.ParentView, 'parent')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='app/students/', permanent=False)),
    path('app/', include('app.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
