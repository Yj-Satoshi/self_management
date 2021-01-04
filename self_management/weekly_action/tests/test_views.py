from django.test import TestCase
from django.contrib.auth import get_user_model
from monthly_goal.models import MonthlyGoal
from account.models import CustomUser
# from .. models import WeeklyAction
from django.urls import reverse
# Create your tests here.


class TestWeeklyActionView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='samples@sample.com', password='1234pass'
        )

    def test_action_create_success(self):
        self.client.login(username='test1', password='1234pass')
        create_goal = MonthlyGoal.objects.create(
            custom_user=CustomUser.objects.get(username='test1'),
            year=2020,
            month=12,
            goal='aaaa',
            category=1,)
        url_create_action = reverse('weekly_action:action-create', args=(create_goal.id,))
        response = self.client.get(url_create_action)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weekly_action/action_create.html')
        self.assertFalse(response.context['form'].errors)

        # create_action = WeeklyAction.objects.create(
        #     monthly_goal=MonthlyGoal.objects.get(goal='aaaa'),
        #     custom_user=CustomUser.objects.get(username='test1'),
        #     week_no=3,
        #     goal_action='bbbb',
        # )
        # url_action = reverse(
        #     'weekly_action:action-detail', args=(create_action.id, create_goal.id))
        # response_action = self.client.get(url_action)
        # self.assertEqual(response_action.status_code, 200)
        action = self.client.post(url_create_action, {
            'monthly_goal': MonthlyGoal.objects.get(goal='aaaa'),
            'custom_user': self.user.id,
            'week_no': 3,
            'goal_action': 'bbbb',
        })
        self.assertEqual(action.status_code, 302)
        self.assertRedirects(action, '/main')
