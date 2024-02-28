from django.db import models
from common.models import CommonModel
from users.models import User

# User:Subscription => 1:N
class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
