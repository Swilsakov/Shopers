from rest_framework.viewsets import ModelViewSet
from products.models import CartProduct, Category, Customer, Order, Product, Cart
from products.serializers import BaseProductSerializer, CartProductSerializer, CategorySerializer, \
    CartSerializer, CustomerSerializer, OrderSerializer
from rest_framework.permissions import AllowAny


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BaseProductSerializer
    permission_classes = [AllowAny]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [AllowAny]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]
