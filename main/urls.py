from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'signup/', views.signup, name="signup"),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$',views.home_index, name="homePage"),
    url(r'profile/',views.profile_path, name='profile'),
    # url(r'new/',views.new_index, name='new')
    url(r'update/',views.update, name='update'),
    url(r'^search/', views.search_project, name='search_results'),
    url(r'post_new/',views.post_new, name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
