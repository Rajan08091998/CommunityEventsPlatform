from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    participants = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Event
        fields = ['id','title', 'description', 'start_time','end_time', 'participants','location','organizer']


