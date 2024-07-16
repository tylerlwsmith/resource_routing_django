from rest_framework.routers import SimpleRouter, Route, DynamicRoute


class TemplateRouter(SimpleRouter):
    # Copied from SimpleRouter
    routes = [
        # List route.
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={"get": "list", "post": "create"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        # CUSTOM: New form route.
        Route(
            url=r"^{prefix}/new{trailing_slash}$",
            mapping={"get": "new"},
            name="{basename}-new",
            detail=False,
            initkwargs={},
        ),
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=False,
            initkwargs={},
        ),
        # Detail route.
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
        # CUSTOM: Edit form route.
        Route(
            url=r"^{prefix}/{lookup}/edit{trailing_slash}$",
            mapping={"get": "edit"},
            name="{basename}-edit",
            detail=True,
            initkwargs={},
        ),
        # Dynamically generated detail routes. Generated using
        # @action(detail=True) decorator on methods of the viewset.
        DynamicRoute(
            url=r"^{prefix}/{lookup}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]
