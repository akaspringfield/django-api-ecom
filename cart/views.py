# Create your views here.

from rest_framework import generics

from user.models import User
from .serializers import CartListSerializer
from .models import Cart
from user.mixinx import CustomLoginRequiredMixin

class CartList(CustomLoginRequiredMixin, generics.ListAPIView):
    #hear we geting the user model as object
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer

    #get request
    def get(self, request, *args, **kwargs):
        self.queryset = Cart.objects.order_by('-created_at').filter(user=request.login_user)
        return self.list(request, *args, **kwargs)


class CartAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    #hear we geting the user model as object
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer

    #post request
    def post(self, request, *args, **kwargs):
        request.data['username'] = request.login_user.id
        return self.create(request, *args, **kwargs)