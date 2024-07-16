from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import FormParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ViewSet


class TemplateViewSet(ViewSet):
    authentication_classes = [SessionAuthentication]
    parser_classes = [FormParser]
    renderer_classes = [TemplateHTMLRenderer]
