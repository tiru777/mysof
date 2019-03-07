from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from fos_app import views


#router = DefaultRouter()
#router.register(r'soft', views.SofViewSet)
# router.register(r'users', views.UserViewSet)

#from rest_framework.schemas import get_schema_view

#schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    #path('', include(router.urls)),
    path('sof/', views.SofViewSet.as_view()),
    path('user/', views.UserViewSet.as_view()),
    #path('schema/', schema_view)
]