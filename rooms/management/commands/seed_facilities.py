from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = " This command creates facilites "

    """def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)"""

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created"))
        return
