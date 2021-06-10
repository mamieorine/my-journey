from django.core.management.base import BaseCommand, CommandError

from core.models import Profile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id', nargs=1, type=int)

    def handle(self, *args, **options):

        try:
            id = options.get('id')[0]
            print(id)
            profile = Profile.objects.get(id=id)
            print(profile.name)
        except Exception:
            raise CommandError("Error!")
