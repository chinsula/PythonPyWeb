"""projectDbDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Чтобы была возможность подгрузить файл с настройками
from django.conf.urls.static import static  # Чтобы подгрузить обработчик статических файлов

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.app.urls')),
    path('train/', include('apps.db_train.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('apps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Добавление путей для обработки
    # медиафайлов в Django(по умолчанию не обрабатывается, поэтому пишем, чтобы обрабатывалась как статика). Для режима
    # продакшн (Debug=False) нужно использовать другие сервисы (не Django) для обработки медиафайлов.

    # После urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path('api_alter/', include('apps.db_train_alternative.urls')),
    ]