from django.test import TestCase

from core.models import Profile, Subscriber


class TestProfile(TestCase):
    def test_profile_should_have_fields(self):
        profile = Profile.objects.create(
            name="Mamieo"
        )

        assert profile.name == "Mamieo"


class TestSubscriber(TestCase):
    def test_subscriber_should_have_fields(self):
        subscriber = Subscriber.objects.create(
            email="janthong@gmail.com"
        )

        assert subscriber.email == "janthong@gmail.com"


class TestIndexView(TestCase):
    def test_index_view_should_see_my_name(self):
        # Given
        profile = Profile.objects.create(name="Mamieo")
        assert profile.name == "Mamieo"

        # When
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # Then
        assert response.status_code == 200
        assert "Mamieo" in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        # Given
        Profile.objects.create(name="Mamieo")
        Subscriber.objects.create(email="mamieorinee@gmail.com")

        # When
        data = {
            "email": "mamieorinee@gmail.com"
        }
        response = self.client.post("/", data=data)

        # Then
        assert response.status_code == 200
        subscriber = Subscriber.objects.last()
        assert subscriber.email == "mamieorinee@gmail.com"
