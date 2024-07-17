from blog.forms import BlogPostForm
from blog.models import BlogPost
from django.shortcuts import get_object_or_404, render, redirect
from overrides.viewsets import TemplateViewSet
from rest_framework.request import Request


class BlogPostViewSet(TemplateViewSet):
    def list(self, request: Request):
        return render(request, "blog/list.html", {"posts": BlogPost.objects.all()})

    def retrieve(self, request: Request, pk):
        post = get_object_or_404(BlogPost, id=pk)
        return render(request, "blog/retrieve.html", {"post": post})

    def create(self, request: Request):
        if request.method == "POST":
            form = BlogPostForm(request.POST)
            if form.is_valid():
                post = form.save()
                return redirect(f"/posts/{post.id}/")
        else:
            form = BlogPostForm()

        return render(request, "blog/create.html", {"form": form})

    def update(self, request: Request, pk):
        post = BlogPost.objects.get(id=pk)
        if request.method == "PUT":
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect(f"/posts/{post.id}/")
        else:
            form = BlogPostForm(instance=post)

        return render(request, "blog/update.html", {"form": form, "post": post})

    def destroy(self, request: Request, pk):
        post = BlogPost.objects.get(id=pk)
        post.delete()
        return redirect(f"/posts/")


def homepage_redirect(request):
    return redirect("/posts/")
