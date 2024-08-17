from rest_framework import viewsets, status
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

    # def get_queryset(self):
    #     return super().get_queryset().filter(organizer=self.request.user).order_by('-id')

    @action(detail=True, methods=['post'],url_path='participants')
    def participants(self, request, pk=None):
        event = self.get_object()
        user = request.user
        event.participants
        if event.participants.filter(id=user.id).exists():
            return Response({'status': 'You have already Joined'}, status=status.HTTP_400_BAD_REQUEST)
        event.participants.add(user)
        return Response({'status': 'JOined successful'}, status=status.HTTP_200_OK)

