from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.signup),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$',views.home_index, name="homePage"),
    url(r'profile/',views.profile_path, name='profile'),

]
