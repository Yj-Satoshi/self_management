from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class TestWeeklyActionView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='samples@sample.com', password='1234pass'
        )

    def test_action_create_success(self):
        self.client.login(username='test1', password='1234pass')
        goal = self.client.post('/goal/new/', {
            'custom_user': self.user.id,
            'year': 2020,
            'month': 12,
            'goal': 'aaaa',
            'category': 1,
        })
        response = self.client.get('/goal/1/action/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weekly_action/action_create.html')

        action = self.client.post('/goal/1/action/new/', {
            'custom_user': self.user.id,
            'monthly_goal': goal.id,
            'week_no': 5,
            'goal_action': 'bbbb',
        })
        self.assertEqual(action.status_code, 302)
        self.assertRedirects(action, '/main')
