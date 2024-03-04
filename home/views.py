from django.shortcuts import render
from .models import PartnerImages


# Create your views here.
def index(request):
    """ A view to return the index page """

    p_images = PartnerImages.objects.all()

    return render(request, 'home/index.html', {
        'partner_images': p_images,
    })
