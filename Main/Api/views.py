from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.
class FreetrilerView(APIView):
    def get(selfs,request):
        freeobj=FreeTriler.objects.all()
        serialzer=FreeTrailerSerlizers(freeobj,many=True)
        return Response({'status':2000,'payload':serialzer.data})

    def post(self,request):
        serialzer = FreeTrailerSerlizers(data=request.data)
        serialzer.save()
        return  Response({'status':200,'payload':serialzer.data,'message':'save data'})

    # def put(selfs,request):
    #     pass
    #
    # def patch(self,request):
    #     pass
    #
    # def delete(self, request):
    #     pass