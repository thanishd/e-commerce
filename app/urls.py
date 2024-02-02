from django.urls import path
from app import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('',views.home),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('Cart/',views.Cart,name="Cart"),
    path('fav/',views.fav_page,name="fav"),
    path('favviewpage/',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_Cart/<str:cid>',views.remove_Cart,name="remove_Cart"),
    path('collection/',views.collection,name="collection"),
    path('collection/<str:name>',views.collectionview,name="collection"),
    path('collection/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart/',views.add_to_cart,name="addtocart"),
]
