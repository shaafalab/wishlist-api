from items.models import Item
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    ItemListSerializer,
    DetailSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter , OrderingFilter

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields =['name' , 'description']


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsAuthenticated,]

