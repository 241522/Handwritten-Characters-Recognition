from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from .forms import FileFieldForm

@csrf_exempt
def form_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                print(f)
            return JsonResponse({"stats": "dummy"})

        return HttpResponse(status=401)


