from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video
from django.db.models import Count, Q


# class Reactionmanager(models.Manager):
#     def get_queryset():
#         likes_count = 
#         dislikes_count = 
#         return 

# yotube: 좋아요(like), 싫어요(dislike), 제거(removelike)
class Reaction(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    # boolean: True, False, None(x)
    # like = models.BooleanField(null=True, default=None)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No reaction'),
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    # from django.db.models import Count, Q
    @staticmethod
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )

        return reactions