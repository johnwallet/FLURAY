from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from personalaccount.models import RequestChange
from .serializers import RequestAPI


def home(request):
    return render(request, 'home/index.html')


class RequestList(APIView):
    """Список заявок"""
    def get(self, request):
        req = RequestChange.objects.all()
        s = RequestAPI(req, many=True)
        return Response(s.data)
