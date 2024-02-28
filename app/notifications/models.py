from django.db import models
from users.models import User
from videos.models import Video

class Notification(CommonModel):
    message = models.CharField
    is_
