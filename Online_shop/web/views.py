from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

import django.views.generic as generic_views
from django.urls import reverse_lazy

from Online_shop.web.forms import ProductPostForm
from Online_shop.web.models import Product
from django.core.paginator import Paginator



class Index(generic_views.TemplateView , generic_views.ListView):
    template_name = 'index.html'
    queryset= Product.objects.all().filter(promo = True)
    # paginate_by = 5
    queryset2 = Product.objects.order_by('-sales')[:5]

    def get(self, request, *args, **kwargs):
        # products = Product.objects.all()
        return  render(request,'index.html' ,{
            'promo': self.queryset ,
            'top': self.queryset2,
        })



class ProductDetailsView(LoginRequiredMixin,generic_views.TemplateView):
     template_name = 'web/product_details.html'

     def get(self, request,pk, *args, **kwargs):
         product = Product.objects.all().get(barcode= pk)
         return render(request, 'web/product_details.html', {'product': product})


class ProductCatalogeView(generic_views.ListView):
    template_name = 'web/cataloge.html'
    queryset = Product.objects.all().order_by('price')
    paginate_by = 3
    model = Product
    context_object_name = 'products'


class ProductTopView():
    pass


class ProductPostView(LoginRequiredMixin,generic_views.CreateView):
    form_class = ProductPostForm
    template_name = 'web/product_form.html'
    success_url = reverse_lazy('Index')


class ProductEditView(LoginRequiredMixin,generic_views.UpdateView,SuccessMessageMixin,):

    login_url = reverse_lazy()

    model = Product

    template_name  = 'web/product_form.html'
    success_url = reverse_lazy('Index')
    fields = '__all__'
    success_message = 'Information successfully updated'


    def put(self,  *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return self.post(kwargs)


class ProductDeleteView(LoginRequiredMixin,generic_views.DeleteView):
    login_url = reverse_lazy('Index')

    model = Product
    success_url = reverse_lazy('Index')
    template_name = 'web/product_delete.html.'
    pass
