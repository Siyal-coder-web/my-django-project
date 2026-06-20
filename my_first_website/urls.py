from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('edit/<int:project_id>/', views.edit_project, name='edit_project'),
    
    # Profile URL
    path('profile/', views.profile_page, name='profile'),
    
    # Auth URLs
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]

# Yeh line development mein images dikhane ke liye zaroori hai
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)