from rest_framework import viewsets
from fos_app.serializers import  UserSerializer,SoftSerializer
from django.contrib.auth.models import User

from rest_framework.decorators import action
from rest_framework.response import Response
from fos_app.models import Sofmodel
#from rest_framework import permissions
from rest_framework import renderers
#from fos_app.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SofViewSet(viewsets.ModelViewSet):
    queryset = Sofmodel.objects.all()
    serializer_class = SoftSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    #@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    '''
    def highlight(self, request, *args, **kwargs):
        soft = self.get_object()
        return Response(soft.highlighted)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    '''