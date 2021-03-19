from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from blog.blogpost.views import BlogpostListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogposts/", BlogpostListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
