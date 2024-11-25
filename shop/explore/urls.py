from django.urls import path, include
from . import views
from .views import product_detail
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
urlpatterns = [
    
    path('', views.all_items, name='index'),
    path('all_items/', views.all_items, name='all_items'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('sell/', views.sell, name='sell'),
    path('register/',views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('account/', views.account, name='account'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('success/', views.success, name='success'),
    path('<int:product_id>/edit/',views.prod_edit, name='prod_edit'),
    path('<int:product_id>/delete/',views.prod_delete, name='prod_delete'),
    path('success/<int:product_id>/<int:quantity>/<str:total_price>/', views.success, name='success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)