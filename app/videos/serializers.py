from rest_framework.serializers import ModelSerializer
from .models import Video

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__' # Video 모델의 전체 필드를 보여줘