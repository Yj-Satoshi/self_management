from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class TestMonthlyGoalView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='samples@sample.com', password='1234pass'
        )

    def test_goal_create_success(self):
        self.client.login(username='test1', password='1234pass')

        response = self.client.get('/goal/new/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].errors)
        self.assertTemplateUsed(response, 'monthly_goal/goal_create.html')

        monthly_goal = self.client.post('/goal/new/', {
            'custom_user': self.user.id,
            'year': 2020,
            'month': 12,
            'goal': 'aaaa',
            'category': 1,
        })
        self.assertEqual(monthly_goal.status_code, 302)
        self.assertRedirects(monthly_goal, '/main')
