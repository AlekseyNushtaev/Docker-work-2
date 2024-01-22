from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #filter_backends = [filters.BaseFilterBackend]
    filterset_fields = ['products']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        queryset = Stock.objects.all()
        products = self.request.query_params.get('products')
        if products is not None:
            queryset = queryset.filter(products=products)
        return queryset
    # при необходимости добавьте параметры фильтрации
