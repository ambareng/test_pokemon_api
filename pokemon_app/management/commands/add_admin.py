from django.core.management.base import BaseCommand
from pokemon_app.models import Trainer
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Adds the admin account to the database'

    def handle(self, *args, **options):
        Trainer.objects.create(
            name='admin',
            email='admin@test.com',
            password=make_password('Yeahyeahyeah1!'),
            is_admin=True,
        )
        print('Added admin')
