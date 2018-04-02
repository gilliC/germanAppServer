from django.http import JsonResponse
from django.core.serializers import serialize
import json

from .models import Word


def index(request):
        vocabulary = Word.objects.all()
        json_data = serialize("json", vocabulary)
        final_data = json.loads(json_data)
        return JsonResponse(final_data, safe=False)
