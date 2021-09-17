from django.urls import path
from fileuploadapi.views import FileUploadViewSet
urlpatterns = [
    path("files/", FileUploadViewSet.as_view({"get": "list"}), name="files")
]