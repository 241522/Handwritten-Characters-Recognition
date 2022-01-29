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

        form = FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            stats_nn, stats_fb = calculate_stats(files)
            response = {"stats_nn": stats_nn.__dict__, "stats_fb": stats_fb.__dict__}

            return JsonResponse(response, safe=False)

        return HttpResponse(status=401)


