from rest_framework import serializers
from work.models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'title', 'percentage', 'bar_color')