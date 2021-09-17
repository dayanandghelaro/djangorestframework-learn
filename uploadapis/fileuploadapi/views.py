from rest_framework import views
from rest_framework import viewsets
from rest_framework import  permissions
from fileuploadapi.serializers import FileUploadSerializer
from fileuploadapi.models import FileUpload

# Create your views here.
class FileUploadViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploadSerializer
    permission_classes = [ permissions.AllowAny ]
    queryset = FileUpload.objects.all()

