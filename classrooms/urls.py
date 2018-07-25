
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from rest_framework_jwt.views import obtain_jwt_token
from classes_api.views import (
    ClassListView,
    ClassDetailView,
    ClassUpdateView,
    ClassDeleteView,
    ClassCreateView,
    RegisterView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api/list/', ClassListView.as_view(), name='api-list'),
    path('api/create/', ClassCreateView.as_view(), name='api-create'),
    path('api/<int:class_id>/detail/', ClassDetailView.as_view(), name='api-detail'),
    path('api/<int:class_id>/update/', ClassUpdateView.as_view(), name='api-update'),
    path('api/<int:class_id>/delete/', ClassDeleteView.as_view(), name='api-delete'),
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api-token-auth/', obtain_jwt_token),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
