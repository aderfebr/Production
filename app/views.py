from django.http import JsonResponse
from app.models import Node,Edge

# Create your views here.

def getnode(request):
    res=list(Node.objects.all().values())
    return JsonResponse({
        'data':res,
        'code':200,
    })

def getedge(request):
    res=list(Edge.objects.all().values())
    return JsonResponse({
        'data':res,
        'code':200,
    })