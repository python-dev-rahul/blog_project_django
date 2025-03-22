# myapp urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_us, name="about_us"),  # Moved this pattern to the top
    path('newsletter/', views.newsletter, name="newsletter"),
    path('send_email/', views.send_email, name="send_email"),
    path('admin-panel-dreamers-infotech-abcdefgh12345684ghvyasvgvastcvbh!_+$%^&*(gFDSA)rctvybunim/', views.admin_url, name="admin-panel"),
    path('admin-add-blog-erftgvybnuim123456789!(rctvybunim/', views.admin_add_blog, name="admin-add-blog"),
    path('edit-blog-erftgvybnuim123456789!(rctvybunim/drftgyhujimklkmjnhbgvfcdxrftgyhukmhgtrytfuygihujlnbhgvfcdfghj523658236956232595626965edrfytguyihuj/', views.edit_blog, name="edit-blog"),
    path('update-post/<int:id>/', views.updatepost, name="updatepost"),
    path('deletepost/<int:id>/', views.delete_post, name="delete-post"),
    path('<slug:slug>/', views.show_blog_detail, name='blog_detail'),
    path('<str:name>/', views.all_category, name="all_category"),
    path("", views.home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
