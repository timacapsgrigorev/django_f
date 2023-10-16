from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user with age greater<age>."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='Userage')
    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age) # age__gt=age gt больше того возвраста что мы указали
        self.stdout.write(f'{user}')