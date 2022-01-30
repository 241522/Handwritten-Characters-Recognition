import json

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from statistics.Stats import calculate_stats
from .forms import FileFieldForm


@csrf_exempt
def form_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        json_string = request.body.decode()
        json_dict = json.loads(json_string)
        stats_nn, stats_fb = calculate_stats(json_dict['path'])
        response = {"stats_nn": stats_nn.__dict__, "stats_fb": stats_fb.__dict__}

        return JsonResponse(response, safe=False)
