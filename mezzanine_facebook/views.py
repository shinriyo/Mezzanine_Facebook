from django.shortcuts import render
from mezzanine.conf import settings


def example(request):
    return render(request, 'mezzanine_facebook/example.html', {
        'facebook_app_id': settings.FACEBOOK_APP_ID,
    })
