# Resource Routing in Django

You can read more about this project in [my blog post](https://dev.to/tylerlwsmith/emulating-rails-like-resource-controllers-in-a-server-rendered-django-app-alp).

This project extends Django REST Framework's `ViewSet` and `SimpleRouter` to provide a Ruby on Rails-like request handler class and resource routing in server-render Django applications. It also features form-level method spoofing for `PUT`, `PATCH` and `DELETE` requests via custom middleware.
The table below lists the project's custom `TemplateRouter`'s conventions:

| HTTP Verb | Path               | ViewSet.Action        | Used for                     |
| --------- | ------------------ | --------------------- | ---------------------------- |
| GET       | /posts/            | PostsViewset.list     | list of all posts            |
| GET       | /posts/create/     | PostsViewset.create   | form for creating a new post |
| POST      | /posts/create/     | PostsViewset.create   | create a new post            |
| GET       | /posts/:id/        | PostsViewset.retrieve | return a specific post       |
| GET       | /posts/:id/update/ | PostsViewset.update   | form for editing a post      |
| PUT       | /posts/:id/update/ | PostsViewset.update   | update a specific post       |
| DELETE    | /posts/:id/        | PostsViewset.destroy  | delete a specific post       |

The `TemplateRouter` can be used with a custom `TemplateViewSet` to deliver an Action Controller-like experience:

```py
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
        website = BlogPost.objects.get(id=pk)
        website.delete()
        return redirect(f"/posts/")
```

To see the code in action, view [`blog/views.py`](blog/views.py) and [`resource_routing/urls.py`](resource_routing/urls.py). To view the underlying implementation, view the files in the [`overrides`](overrides) directory.

## Running locally

To run the app locally, clone the project then run the following commands in the main project directory:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
