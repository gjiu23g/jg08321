from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from myproject.api.models import Review, Dealership

class Command(BaseCommand):
    help = 'Seed the database with random reviews'

def handle(self, *args, **kwargs):
    for i in range(1, 16):
        dealership = Dealership.objects.get(pk=i)
        for j in range(1, 2):  # Assuming each dealership gets one review for simplicity
            review_content = f"This is a review {get_random_string(length=8)}."
            rating = 5  # Assuming a top rating for simplicity
            
            Review.objects.create(
                dealership=dealership,
                content=review_content,
                rating=rating
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded review {i}'))

