from django.shortcuts import render
from django.http import HttpResponse

from news.models import NewsDetail
# Create your views here.

def index(request):
    keys = NewsDetail.objects.order_by('-published_date').filter(is_published=True)[:3]

    context = {
        'keys': keys
    }

    return render(request, 'pages/index.html', context)
