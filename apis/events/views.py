from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from events.models import Event
from apis.events.serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return super().perform_create(serializer.save(organizer=self.request.user))

    def get_queryset(self):
        return super().get_queryset().filter(organizer=self.request.user).order_by('-id')

    # @action(detail=False, methods=['get'])
    # def custom_action(self, request):
    #     # Custom action logic here
    #     data = {"message": "Custom action response"}
    #     return Response(data)

    # @action(detail=True, methods=['get'])
    # def special_detail(self, request, pk=None):
    #     # Custom detail action logic here
    #     event = self.get_object()
    #     serializer = self.get_serializer(event)
    #     data = {"event": serializer.data, "special_info": "Additional data"}
    #     return Response(data)
