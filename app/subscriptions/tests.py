from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse
from rest_framework import status


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user@gamil.com', password='password123')
        self.user2 = User.objects.create_user(email='user2@gmail.com', password='123')

        self.client.login(email='user@gmail.com', password='password123')

    # api/v1/subscriptions
    # SubscriptionList
    # [POST]: 구독하기 버튼 클릭

    def test_subscription_list_post(self):
        url = reverse('subs-list')
        data = {
            'subscribed_to': self.user2.pk
        }

        self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # api/v1/subscriptions/{user_id}
    # SubscriptionDetail
    # [DELETE]: 구독취소

    def test_sub_detail_delete():
        pass