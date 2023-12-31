from rest_framework import viewsets, decorators, response, views, status
from .forms import UploadFileForm
from .storage import uploadFile

class BaseAPIView(views.APIView):

    def get(self, request, pk=None):
        return response.Response("Audio Recorder", status=status.HTTP_200_OK)

class RecordingAPIView(views.APIView):
    
    # @decorators.action(methods=['get'], detail=True)
    def get(self, request, pk=None):
        return response.Response([
            {
                "day": "Saturday",
                "date":"Unix Timestamp",
                "location":{
                    "lat": 0.0,
                    "lng": 0.0
                },
                "duration": 2138218937123
            }
        ], status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES["file"]
                uploadFile(file)
                return response.Response("File Uploaded Successfully", status=status.HTTP_200_OK)
        else:
            form = UploadFileForm()
        return response.Response("File Cannot Be Uploaded", status=status.HTTP_400_BAD_REQUEST)
