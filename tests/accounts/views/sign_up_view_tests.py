from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@musclearmy.com',
        'password1': 'test1password',
        'password2': 'test1password',
    }

    def test_sign_up__with_valid_data__expect_to_log_in_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA
        )

        print(response.context['user'])

