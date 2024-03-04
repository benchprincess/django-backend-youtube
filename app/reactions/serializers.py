from rest_framework import serializer

class ReactionSerializer(serializer.ModelSerializer):
    class Meta:
        mode = Reaction
        fields = "__all__"