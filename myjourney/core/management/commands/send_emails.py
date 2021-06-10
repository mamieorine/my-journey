from django.core.management.base import BaseCommand, CommandError
from django.core import mail

from core.models import Subscriber


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            connection = mail.get_connection()
            connection.open()

            subscribers = Subscriber.objects.all()
            for subscriber in subscribers:
                email = mail.EmailMessage(
                    'Hello YOU!',
                    '========== Body ==========',
                    'from@example.com',
                    [subscriber.email],
                    connection=connection,
                )
                email.send()

        except Exception:
            raise CommandError("Error!")
