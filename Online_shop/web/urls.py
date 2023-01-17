from django.urls import path
from Online_shop.web.views import Index, ProductDetailsView, ProductCatalogeView, ProductTopView, ProductEditView, \
    ProductPostView, ProductDeleteView

urlpatterns = (
    path('', Index.as_view(), name='Index'),
#
    path('product/details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('product/cataloge/', ProductCatalogeView.as_view(), name='products cataloge'),
#     path('product/TOP50', ProductTopView.as_view(), name='products TOP50'),
#
    path('product/post', ProductPostView.as_view(), name='product post'),
    path('product/edit/<int:pk>', ProductEditView.as_view(), name='product edit'),
    path('product/delete', ProductDeleteView.as_view(), name='product delete'),
# ))
)