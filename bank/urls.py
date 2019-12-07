from django.urls import path
from . import views

handler_404 = views.handler404

urlpatterns = [
    path('<str:ifsc>/', views.BranchIFSC.as_view()),
    path('<str:bank>/<str:city>/', views.BranchFilter.as_view())
] 