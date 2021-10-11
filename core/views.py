from json.encoder import JSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from .models import ApprovedOrders, GeneralOrders
from .serializers import ApprovedOrdersApiSerializer, GeneralOrdersApiSerializer
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
def approve_general_order(request, item_id):
    print('approve_general_order: ', item_id);
    if request.method != "POST":
        return JsonResponse({'error': 'request need to be post'})
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'user is not authenticated'})
    try:
        obj = GeneralOrders.objects.get(pk=item_id)
        
        approvedOrder = ApprovedOrders.objects.create(
            created=obj.created, 
            name=obj.name, 
            providerName=obj.providerName, 
            total=obj.total,
            type=obj.type)
        
        approvedOrder.save()
        obj.delete()
        return JsonResponse({'success':ApprovedOrdersApiSerializer(approvedOrder).data})
    except Exception as e:
        print(e)
        return JsonResponse({'error':'object not found'})
    
def index_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'index.html', context={})
# Create your views here.
class GeneralOrdersViewSet(viewsets.ModelViewSet):
    queryset = GeneralOrders.objects.all()
    serializer_class = GeneralOrdersApiSerializer
    #filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    #search_fields = ['type', 'name', 'providerName',]
    filterset_fields = ['type', 'providerName', 'name']
    ordering_fields = ['created', 'id', 'name', 'providerName', 'type',]

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        #filter_backends = []
        
        return [permission() for permission in permission_classes]

class ApprovedOrdersViewSet(viewsets.ModelViewSet):
    queryset = ApprovedOrders.objects.all()
    serializer_class = ApprovedOrdersApiSerializer
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]