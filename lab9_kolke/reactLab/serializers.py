from rest_framework import serializers
from reactLab.models import Lab


class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lab
        fields = ('id',
                  'title',
                  'description',
                  'published')
