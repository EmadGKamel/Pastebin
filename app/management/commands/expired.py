from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Snippet


class Command(BaseCommand):
    help = 'Deletes expired rows'

    def handle(self, *args, **options):
        now = timezone.now()
        Snippet.objects.filter(expiration_date__lt=now).delete()