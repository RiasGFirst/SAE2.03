from django.urls import path
from .views import views, views_product, views_category, views_order, views_customer, views_list

urlpatterns = [
    # Home URL
    path('', views.home),

    # Product URLs
    path('product/', views_product.home),
    path('product/add/', views_product.add),
    path('product/processing/', views_product.processing),
    path('product/update/<int:id>', views_product.update),
    path('product/processing_update/<int:id>/', views_product.processing_update),
    path('product/show/<int:id>', views_product.show),
    path('product/delete/<int:id>', views_product.delete),
    path('product/import/', views_product.import_product),

    # Order URLs
    path('order/', views_order.home),
    path('order/add/', views_order.add),
    path('order/processing/', views_order.processing),
    path('order/update/<int:id>', views_order.update),
    path('order/processing_update/<int:id>/', views_order.processing_update),
    path('order/show/<int:id>', views_order.show),
    path('order/delete/<int:id>', views_order.delete),
    path('order/export/<int:id>', views_order.export_orders),

    # List URLs

    path('list/add/<int:id>/', views_list.add),



    # Customer URLs
    path('customer/', views_customer.home),
    path('customer/add/', views_customer.add),
    path('customer/processing/', views_customer.processing),
    path('customer/update/<int:id>', views_customer.update),
    path('customer/processing_update/<int:id>/', views_customer.processing_update),
    path('customer/show/<int:id>', views_customer.show),
    path('customer/delete/<int:id>', views_customer.delete),

    # Category URLs
    path('category/', views_category.home),
    path('category/add/', views_category.add),
    path('category/processing/', views_category.processing),
    path('category/update/<int:id>', views_category.update),
    path('category/processing_update/<int:id>/', views_category.processing_update),
    path('category/show/<int:id>', views_category.show),
    path('category/delete/<int:id>', views_category.delete),
]