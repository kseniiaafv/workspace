from django.shortcuts import render
from .models import Specialist, Dog, Review


def home(request):
    specialists = Specialist.objects.filter(is_active=True)
    dogs = Dog.objects.filter(is_active=True)

    review_parent = Review.objects.filter(is_active=True, category='parent').last()
    review_adult = Review.objects.filter(is_active=True, category='adult').last()
    review_result = Review.objects.filter(is_active=True, category='result').last()

    context = {
        'specialists': specialists,
        'dogs': dogs,
        'review_parent': review_parent,
        'review_adult': review_adult,
        'review_result': review_result,
    }
    return render(request, 'index.html', context)