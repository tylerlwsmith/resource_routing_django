from rest_framework.routers import SimpleRouter, Route, DynamicRoute


class TemplateRouter(SimpleRouter):
    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        # NEW:  "create" to its own route.
        Route(
            url=r"^{prefix}/create{trailing_slash}$",
            mapping={"get": "create", "post": "create"},
            name="{basename}-create",
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
            mapping={"get": "retrieve", "delete": "destroy"},
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Instance"},
        ),
        # NEW: Extracted "updated" to its own route.
        Route(
            url=r"^{prefix}/{lookup}/update{trailing_slash}$",
            mapping={"get": "update", "put": "update"},
            name="{basename}-update",
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
