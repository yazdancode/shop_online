# accounts/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Customer


class PhoneNumberTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("save_phone_number")
        self.test_url = reverse("test_page")

    def test_phone_registration_and_session(self):
        """
        بررسی می‌کند که:
          1. با ارسال فرم شماره تلفن ثبت شده و به صفحه تست ریدایرکت شود.
          2. شماره در دیتابیس ذخیره شده باشد.
          3. صفحه تست پیام مربوطه را نمایش دهد.
        """
        # ارسال شماره تلفن از طریق پست
        phone = "09123456789"
        data = {"phone_number": phone}
        response = self.client.post(self.register_url, data)

        # بررسی ریدایرکت شدن به صفحه test_page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.test_url)

        # بررسی ذخیره شماره در دیتابیس
        self.assertTrue(Customer.objects.filter(number=phone).exists())

        # دسترسی به صفحه تست برای بررسی نمایش پیام
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        # بررسی اینکه پیام نمایش داده شده شامل شماره تلفن باشد.
        self.assertContains(response, phone)
        # برای اطمینان، می‌توانید بررسی کنید که پیام ارسال کد وجود دارد.
        self.assertContains(response, "کد عبور ارسال شد")

    def test_test_page_without_session(self):
        """
        بررسی می‌کند که در صورت عدم وجود شماره تلفن در سشن،
        پیام مناسب (مثلاً "شماره در سشن یافت نشد.") نمایش داده شود.
        """
        # قبل از مراجعه به صفحه تست، هیچ شماره‌ای در سشن ذخیره نشده است.
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "شماره در سشن یافت نشد")
