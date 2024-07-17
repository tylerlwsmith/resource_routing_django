from blog.views import BlogPostViewSet, homepage_redirect
from django.contrib import admin
from django.urls import path
from overrides.routers import TemplateRouter

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage_redirect, name="home"),
]

router = TemplateRouter()
router.register(r"posts", BlogPostViewSet, basename="post")

urlpatterns += router.urls
