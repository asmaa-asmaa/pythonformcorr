from django.urls import path
# from .views import submit_form, get_submissions
from .views import submit_data, index, serve_vue
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index', index, name="home"),
    path('submit/', submit_data, name='submit_data'),
    path('', views.serve_vue, name='serve_vue'),


    # path('submit/', submit_form, name='submit_form'),
    # path('submissions/', get_submissions, name="get_submissions"),
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)