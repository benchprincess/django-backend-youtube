from django.db import models
from common.models import CommonModel
from users.models import User


# class VideoManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().annotate(
#             likes_count=models.Count('reaction', filter=models.Q(reaction__reaction=1)),
#             dislikes_count=models.Count('reaction', filter=models.Q(reaction__reaction=-1))
#         )

class Video(CommonModel):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_uploded_url = models.URLField()
    video_file = models.FileField(upload_to='storage/')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # objects = VideoManager()
