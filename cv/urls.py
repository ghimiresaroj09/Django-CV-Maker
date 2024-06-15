from django.urls import path
from .views import *

urlpatterns = [
    path('', cv_create, name='cv_create'),
    path('<int:profile_id>/', cv_download, name='cv_download'),
    path('view/<int:profile_id>/', cv_view, name='cv_view'),
    path('delete/<int:profile_id>/', cv_delete, name='cv_delete'),
    path('update/<int:profile_id>/', cv_update, name='cv_update'),
    path('list', list_view, name='list_view'),
]
