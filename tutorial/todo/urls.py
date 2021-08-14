from django.urls import path
from .views import index,detail,create,update,delete,deleteitem
app_name = 'todo'
urlpatterns = [
    path('' , index , name='index'),
    path('<int:list_id>/' , detail , name= 'list_detail'),
    path('create/' , create , name= 'list_create'),
    path('<int:list_id>/<str:title>/update/' , update , name= 'list_update'),
    path('<int:list_id>/delete/' , delete , name='list_delete'),
    path('<int:list_id>/<str:title>/delete/' , deleteitem , name='list_deleteitem'),
]
