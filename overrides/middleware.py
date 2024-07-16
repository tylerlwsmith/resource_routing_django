from django.conf import settings


class FormMethodOverrideMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            desired_method = request.POST.get("_method", "").upper()
            if desired_method in ("PUT", "PATCH", "DELETE"):
                token = request.POST.get("csrfmiddlewaretoken", "")

                # Override request method.
                request.method = desired_method

                # Hack to make CSRF validation pass.
                request.META[settings.CSRF_HEADER_NAME] = token

        return self.get_response(request)
