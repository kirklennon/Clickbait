from django.shortcuts import render

from api.models import Paragraph, Source

queryset = Paragraph.objects.values().order_by('?')

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_para = Paragraph.objects.all().count()
    num_source = Source.objects.all().count()

    context = {
        'num_para': num_para,
        'num_source': num_source,
        'paragraph_list': queryset[:10],
    }

    return render(request, 'index.html', context=context)

from django.core import serializers
from django.http import HttpResponse
import json

def api(request):
    cleanlist = []
    rawdata = serializers.serialize('python', Paragraph.objects.order_by('?')[:10])
    for row in rawdata:
        cleanlist.append(row['fields']['text'])
    data = json.dumps(cleanlist)
    r = HttpResponse(data, content_type='application/json')
    r['Access-Control-Allow-Origin'] = '*' # Cross-Origin Resource Sharing
    return r
