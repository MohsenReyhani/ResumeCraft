from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from accounts.models import CustomUser
from django.urls import reverse


class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(phone_no='09121221221', password='testpassword')
        self.client.login(phone_no='09121221221', password='testpassword')

    def test_dashboard_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions if needed

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/dashboard/dashboard.html')

    def test_settings_view(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/settings.html')

    # Add other test methods as required

class AuthenticationTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(phone_no='09121221221', password='testpassword')
        self.client.login(phone_no='09121221221', password='testpassword')

    def test_login_view(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign-in.html')

    # Add other test methods as required

# class ExtraViewsTest(TestCase):
#     def test_upgrade_to_pro_view(self):
#         response = self.client.get(reverse('upgrade_to_pro'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'pages/upgrade-to-pro.html')
