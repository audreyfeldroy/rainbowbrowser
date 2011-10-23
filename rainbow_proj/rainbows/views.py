from django.views.generic import DetailView
from rainbows.models import Rainbow

class RainbowPDEView(DetailView):

    context_object_name = "rainbow"
