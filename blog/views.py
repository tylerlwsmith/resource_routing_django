from blog.forms import BlogPostForm
from blog.models import BlogPost
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from overrides.viewsets import TemplateViewSet
from rest_framework.response import Response
from rest_framework.request import Request


class BlogPostViewset(TemplateViewSet):
    def list(self, request: Request):
        return Response(
            template_name="blog/list.html",
            data={"posts": BlogPost.objects.all()},
        )

    def retrieve(self, request: Request, pk):
        return Response(
            template_name="blog/retrieve.html",
            data={"post": get_object_or_404(BlogPost, id=pk)},
        )

    def create(self, request: Request):
        if request.method == "POST":
            form = BlogPostForm(request.POST)
            if form.is_valid():
                post = form.save()
                return HttpResponseRedirect(f"/posts/{post.id}/")
        else:
            form = BlogPostForm()

        return Response(
            template_name="blog/create.html",
            data={"form": form},
        )

    def update(self, request: Request, pk):
        post = BlogPost.objects.get(id=pk)
        if request.method == "PUT":
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                return HttpResponseRedirect(f"/posts/{post.id}/")
        else:
            form = BlogPostForm(instance=post)

        return Response(
            template_name="blog/update.html",
            data={"form": form, "post": form.instance},
        )

    def destroy(self, request: Request, pk):
        website = BlogPost.objects.get(id=pk)
        website.delete()

        return HttpResponseRedirect(f"/posts/")
