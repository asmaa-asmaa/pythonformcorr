from django.urls import path
# from .views import submit_form, get_submissions
from .views import submit_data, index, serve_vue


urlpatterns = [
    path('index', index, name="home"),
    path('submit/', submit_data, name='submit_data'),
    path('', serve_vue)


    # path('submit/', submit_form, name='submit_form'),
    # path('submissions/', get_submissions, name="get_submissions"),
]