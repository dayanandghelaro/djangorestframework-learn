from rest_framework import serializers


from fileuploadapi.models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FileUpload
        fields = ['file', 'name']
    
    
