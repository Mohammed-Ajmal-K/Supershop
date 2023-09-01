from django.urls import path
from webapp import views

urlpatterns=[
    path('home_pg/',views.home_pg,name="home_pg"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('cat_pg/',views.cat_pg,name="cat_pg"),
    path('prod_pg/<cat_name>',views.prod_pg,name="prod_pg"),
    path('cart_pg/',views.cart_pg,name="cart_pg"),
    path('cartsave/', views.cartsave, name="cartsave"),
    path('deletecart/<int:cartid>/', views.deletecart, name="deletecart"),

    path('singleproduct/<int:dataid>/', views.singleproduct, name="singleproduct"),
    path('regpage/', views.regpage, name="regpage"),
    path('savereg/', views.savereg, name="savereg"),
    path('Userlogin/', views.Userlogin, name="Userlogin"),
    path('Userlogout/', views.Userlogout, name="Userlogout"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('checkout/', views.checkout, name="checkout"),

]
