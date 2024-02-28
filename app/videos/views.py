from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer



# 1. VideoList
# api/v1/videos
# - GET: 전체 비디오 목록 조회 => Video.objects.all() => 클라이언트에 전달
# - POST: 새로운 비디오 생성
# - DELETE, PUT: X
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        print('videos:', videos) # 직렬화 작업(장고객체 -> JSON 으로 변환) => serializer

        serializer = VideoSerializer(videos, many-=True)

        return Response(serializer.data)
    
    def post(self):
        pass

# 2. VideoDetail
# api/v1/videos/{video_id}
# - GET: 특정 비디오 상세 조회
# - POST: X
# - PUT: 특정 비디오 정보 업데이트(수정)
# - DELETE: 특정 비디오 삭제