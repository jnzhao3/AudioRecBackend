from rest_framework import viewsets, decorators, response, views, status


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
