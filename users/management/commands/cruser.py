from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='semenov.dmitrii83@gmail.com',
            first_name='Дмитрий',
            last_name='Семёнов',
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        user.set_password('qazwsx2020g3')
        user.save()
