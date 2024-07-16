from rest_framework.routers import SimpleRouter, Route, DynamicRoute


class TemplateRouter(SimpleRouter):
    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={"get": "list", "post": "create"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        # NEW: New form route.
        Route(
            url=r"^{prefix}/new{trailing_slash}$",
            mapping={"get": "new", "post": "new"},
            name="{basename}-new",
            detail=False,
            initkwargs={},
        ),
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=False,
            initkwargs={},
        ),
        Route(
            url=r"^{prefix}/{lookup}{trailing_slash}$",
            mapping={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            },
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Instance"},
        ),
        # NEW: Edit form route.
        Route(
            url=r"^{prefix}/{lookup}/edit{trailing_slash}$",
            mapping={"get": "edit", "put": "edit"},
            name="{basename}-edit",
            detail=True,
            initkwargs={},
        ),
        DynamicRoute(
            url=r"^{prefix}/{lookup}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]
