from django.urls import path
from main.views import (
    show_main, create_product, show_product, show_xml, show_json,
    show_xml_by_id, show_json_by_id, register_ajax, login_ajax, logout_ajax,
    edit_product, delete_product, add_product_ajax, update_product_ajax,
    delete_product_ajax,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('product/<uuid:id>/edit/', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete/', delete_product, name='delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register_ajax, name='register'),
    path('login/', login_ajax, name='login'),
    path('logout/', logout_ajax, name='logout'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('update-product-ajax/<uuid:product_id>/', update_product_ajax, name='update_product_ajax'),
    path('delete-product-ajax/<uuid:product_id>/', delete_product_ajax, name='delete_product_ajax'),
]
