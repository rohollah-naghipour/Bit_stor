from django.core.management.base import BaseCommand
from users.models import Token  

from django.utils import timezone

class Command(BaseCommand):
    help = 'Deletes expired tokens'

    def handle(self, *args, **options):
        now = timezone.now()
        expired_tokens = Token.objects.filter(expires_at__lt=now)
        count = expired_tokens.count()
        expired_tokens.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} expired tokens.'))
