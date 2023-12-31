from django.urls import path, include
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, increment_stock, decrement_stock, delete_product, edit_product, get_product_json, add_product_ajax, create_product_json, edit_product_json, delete_product_json, register_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment_stock/<int:product_id>/', increment_stock, name='increment_stock'),
    path('decrement_stock/<int:product_id>/', decrement_stock, name='decrement_stock'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('auth/', include('authentication.urls')),
    path('create_product_json/', create_product_json, name='create_product_json'),
    path('auth/register_json/', register_json, name='register_json'),
    path('edit_product_json/', edit_product_json, name='edit_product_json'),
    path('delete_product_json/', delete_product_json, name='delete_product_json'),
]