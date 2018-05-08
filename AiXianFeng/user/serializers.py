from rest_framework import serializers

from AXF.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = []

    def to_representation(self, instance):
        data = super().to_representation(instance)

        return data
