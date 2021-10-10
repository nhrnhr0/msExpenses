from django.shortcuts import render
from rest_framework import viewsets
from .models import GeneralOrders
from .serializers import GeneralOrdersApiSerializer


def index_view(request):
    return render(request, 'index.html', context={})
# Create your views here.
class GeneralOrdersViewSet(viewsets.ModelViewSet):
    queryset = GeneralOrders.objects.all()
    serializer_class = GeneralOrdersApiSerializer