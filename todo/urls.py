from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todo import views


urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)