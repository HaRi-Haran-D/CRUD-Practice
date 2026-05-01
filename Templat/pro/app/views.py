from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.utils import timezone
from .models import Item
from .forms import ItemForm
from .serializers import ItemSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

logger = logging.getLogger(__name__)


# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  


# @login_required
# @cache_page(60 * 15)
# @vary_on_headers("User-Agent")
def home(request):
    logger.info("Fetching all items from Database")
    logger.info(f"User: {request.user} [{timezone.now().isoformat()}] requested item list form {request.META.get('REMOTE_ADDR')}")
    items = Item.objects.all()
    logger.debug(f"Found {items.count()} items")
    paginator = Paginator(items, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/index.html', {'page_obj':page_obj})



def detail(request, id):
    logger.info(f"Fetching an item with id:{id}")
    try:
        items = get_object_or_404(Item, pk=id)
        # items = Item.objects.get(id=id)
        logger.debug(f"Item Found {items.name} (${items.price})")
        return render(request, 'app/details.html', {'items':items})
    except Exception as e:
        logging.error(f"Error fetching the item %s: %s",id,e)
        raise


def create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app:home')
    return render(request, 'app/item_form.html', {'form':form})


# def update(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('app:home')
#     return render(request, 'app/item_update_form.html', {'form':form})


def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('app:home')
    return render(request, 'app/delete.html')


class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    template_name = 'app/item_update_form.html'
    
    def get_queryset(self):
        return Item.objects.filter(user_name = self.request.user)


# class ItemListCreateAPI(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# class ItemRetrieveUpdateDestryAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


# class ItemListAPIView(APIView):
#     def get(self, request):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# class ItemDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Item.objects.get(pk=pk)
#         except Item.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         item = self.get_object(pk)
#         if not item:
#             return Response({'Error':'Item Not Found'})
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         item = self.get_object(pk)
#         if not item:
#             return Response({'Error':'Item Not Found'})
#         serializer = ItemSerializer(item, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
    
#     def delete(self, request, pk):
#         item = self.get_object(pk)
#         if not item:
#             return Response({'Error':'Item Not Found'})
#         item.delete()
#         return Response({"message":"Item Deleted"})


# @api_view(["GET", "POST"])
# def item_list_api(request):
#     if request.method == "GET":
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(["GET", "PUT", "DELETE"])
# def item_get_api(request, pk):
#     item = Item.objects.get(pk=pk)
#     if request.method == "GET":
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ItemSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         item.delete()
#         return Response({"message":"Item Deleted"})


# class IndexClassView(ListView):
#     model = Item
#     template_name = 'app/index.html'
#     context_object_name = 'items'


# class ItemDeleteView(DeleteView):
#     model = Item
#     success_url = reverse_lazy('app:home')


# class FoodDetailView(DetailView):
#     model = Item
#     template_name = 'app/details.html'
#     context_object_name = 'items'


# class ItemCreateView(CreateView):
#     model = Item
#     fields = ['name', 'price', 'descri', 'image']

#     def form_valid(self, form):
#         form.instance.user_name = self.request.user
#         return super().form_valid(form)


# def get_objects(request):
#     for item in Item.objects.all():
#         print(item.name)

# def get_objects_optimized(request):
#     items = Item.objects.only('name')
#     for item in items:
#         print(item.name)