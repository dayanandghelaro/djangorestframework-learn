from django.urls import path
from fileuploadapi.views import FileUploadViewSet
urlpatterns = [
    path("files/", FileUploadViewSet.as_view({"get": "list"}), name="files"),
    path("add-file/", FileUploadViewSet.as_view({"post": "create"}), name="create"),
    path("<pk>/", FileUploadViewSet.as_view({"get":"retrieve"}), name="detail"),
    path("<pk>/update/", FileUploadViewSet.as_view({"post":"update"}), name="update"),
    path("<pk>/delete/", FileUploadViewSet.as_view({"get":"destroy"}), name="delete"),
]