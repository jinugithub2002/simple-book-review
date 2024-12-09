from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('check_adminlogin/',views.check_adminlogin,name='check_adminlogin'),
    path('admin_homepage/',views.admin_homepage,name='admin_homepage'),
    path('savebook/',views.savebook,name='savebook'),
    path('editbook/<id>',views.editbook,name='editbook'),
    path('updatebook/<id>',views.updatebook,name='updatebook'),
    path('deletebook/<id>',views.deletebook,name='deletebook'),
    path('availablebooks/', views.availablebooks, name='availablebooks'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('addreview/<id>', views.addreview,name='addreview'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('cusregistrations/',views.cusregistrations,name='cusregistrations'),
    path('savecus/',views.savecus,name='savecus'),
    path('cuslogin/',views.cuslogin,name='cuslogin'),
    path('cuslogin_check/',views.cuslogin_check,name='cuslogin_check'),
    path('save_reviews/<id>',views.save_reviews,name='save_reviews'),
    path('viewreviews/<id>',views.viewreviews,name='viewreviews'),
    path('addtocart/<id>',views.addtocart,name='addtocart'),
    path('cart/',views.cart,name='cart'),
    path('cartdetete/<int:id>/', views.cartdetete, name='cartdetete'),
    path('checkout/',views.checkout,name='checkout'),
    path('savebill/',views.savebill,name='savebill'),
    path('order/',views.order,name='order'),
    path('billing_details/', views.billing_details, name='billing_details')
    
]
