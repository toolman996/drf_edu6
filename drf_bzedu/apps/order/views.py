from rest_framework.generics import CreateAPIView

from order.models import Order
from order.serializer import GenerateOrderSerializer


class GenerateOrderAPIView(CreateAPIView):
    queryset = Order.objects.filter(is_show=True,is_delete=False)
    serializer_class = GenerateOrderSerializer














































































































































