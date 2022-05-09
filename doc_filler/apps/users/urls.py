from django.urls import path

from doc_filler.apps.users import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(), name='update_user'),
]
