from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import Post
from .serializers import PostSerializer, VeriyEmailSerializer
from .permissions import IsAuthorOrReadOnly
from allauth.account.views import ConfirmEmailView
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    template_name = 'account/email_confirm.html'

    def get_serializer(self, *args, **kwargs):
        return VeriyEmailSerializer(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        raise MethodNotAllowed('GET')
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        self.get_object().confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)

