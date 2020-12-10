from django.urls import path, include
from. import views
from .views import BookCreateView, UserUpdateView, BookDetailView, UserDetailView, OrderDetailView
from .views import UserDeleteView, BookDeleteView, OrderUpdateView


urlpatterns = [
    path('', views.main, name='home'),
    path('booklist/addbook/', BookCreateView.as_view(), name='book_create'),
    path('userlist/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('userform/', views.UserFormView.as_view(), name='userform'),
    path('success/', views.success, name='success'),
    path('libuser/', views.lib_user, name='libuser'),
    path('userlist/', views.user_list, name='userlist'),
    path('booklist/', views.book_list, name='booklist'),
    path('updatebook/<int:pk>/', views.book_update, name='updatebook'),
    path('userlist/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('booklist/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
    path('search/', views.search, name='search'),
    path('user_search', views.search_user, name='user_search'),
    path('update_order/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('orderlist/', views.order_list, name='order_list'),
    path('orderlist/<int:pk>/', views.delete_order, name='delete_order'),
    path('history', views.history, name='history'),
    path('booklist/<int:pk>/read/', BookDetailView.as_view(), name='book_read'),
    path('user_list/<int:pk>/read/', UserDetailView.as_view(), name='customer_read'),
    path('orderlist/<int:pk>/read/', OrderDetailView.as_view(), name='order_read'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]