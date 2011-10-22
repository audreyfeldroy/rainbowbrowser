from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from rainbows.models import Rainbow

urlpatterns = patterns('rainbows.views',
    url(regex=r'^$',
        view=ListView.as_view(
            queryset=Rainbow.objects.order_by('-pub_date'),
            context_object_name='latest_rainbow_list',
            template_name='rainbows/rainbow_list.html'),
        name='rainbow_list',
    ),
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(
            model=Rainbow,
            template_name='rainbows/rainbow_detail.html'),
        name='rainbow_detail',
    ),
)
