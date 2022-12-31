from django.urls import path
from .views import *

urlpatterns = [
	path('post/<int:pk>/delete/', NewsDeleteView.as_view(), name='post_delete'),
	path('post/<int:pk>/edit', NewsUpdateView.as_view(), name='post_edit'),
	path('post/new/', NewsCreateView.as_view(), name='post_new'),
	path('post/<int:pk>/', NewsDetailView.as_view(), name='post_detail'),
	path('', indexListView.as_view(), name='home'),
]
