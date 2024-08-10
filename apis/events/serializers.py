from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','title', 'description', 'date', 'location','organizer']
        extra_kwargs = {'organizer': {'read_only': True}}


