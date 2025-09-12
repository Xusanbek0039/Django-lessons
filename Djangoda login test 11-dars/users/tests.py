from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


# class ResgiterTestCase(TestCase):
    # def test_user_account_is_created(self):
    #     self.client.post(
    #         reverse("users:register"),
    #         data={
    #             "username":"Xusanbek",
    #             "first_name":"Husan",
    #             "last_name":"Suyunov",
    #             "email":"itcreative@gmail.com",
    #             "password":"0071"
    #         }
    #         )
    #     user = User.objects.get(username="Xusanbek")

    #     self.assertEqual(user.first_name,"Husan")
    #     self.assertEqual(user.last_name,"Suyunov")
    #     self.assertEqual(user.email,"itcreative@gmail.com")
    #     self.assertNotEqual(user.password,"0071")
    #     self.assertTrue(user.check_password("0071"))


    # def test_required_fields(self):
    #     response = self.client.post(
    #         reverse("users:register"),
    #         data={
    #             "first_name": "Husan",
    #             "email":"itcreative@gmail.com"
    #         }
    #     )

    #     user_count = User.objects.count()

    #     self.assertEqual(user_count,0)
    #     self.assertFormError(response,"form","username","This field is required.")
    #     self.assertFormError(response,"form","password","This field is required.")


    # def test_invalid_email(self):
    #     response=self.client.post(
    #         reverse("users:register"),
    #         data={
    #             "username":"ITCreative",
    #             "first_name":"Husan",
    #             "last_name":"Suyunov",
    #             "email":"itcreativegmail.com",
    #             "password":"0071" 
    #         }
    #     )
    #     user_count = User.objects.count()
    #     self.assertEqual(user_count, 0)
    #     print(response.status_code)
    #     print(response.content)
    #     self.assertFormError(response,"form","email","Enter a valid email address.")


    # def test_unique_username(self):
    #     user = User.objects.create_user(
    #         username="Xusanbek",
    #         first_name="Husan",
    #         last_name="Suyunov",
    #         email="itcreative@gmail.com",
    #         password="0071"
    #     )
        
    #     response = self.client.post(
    #         reverse("users:register"),
    #         data={
    #             "username": "Xusanbek",
    #             "first_name": "Husan",
    #             "last_name": "Suyunov",
    #             "email": "itcreative@gmail.com",
    #             "password": "0071"
    #         }
    #     )
        
    #     user_count = User.objects.count()
    #     form = response.context['form']
    #     self.assertFormError(form, "username", "A user with that username already exists.")
