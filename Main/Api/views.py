from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


# Create your views here.
class FreetrilerView(APIView):
    def get(selfs, request):
        try:
            free_triler = FreeTriler.objects.get(windoid=request.data['windoid'])
            serializer = FreeTrailerSerlizers(free_triler)
            return Response({'status': 200, 'payload': serializer.data})
        except Exception as e:
            # free_objs = FreeTriler.objects.all()
            # serializer = FreeTrailerSerlizers(free_objs, many=True)
            return Response({'status': 403, 'error': 'not found'})

    def post(self, request):
        serializer = FreeTrailerSerlizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 204, 'message': 'Data saved successfully'})
        else:
            return Response({'status': 403, 'error': serializer.errors})

    def patch(self, request):  # update single data single
        try:
            # Get the object based on the windoid
            firee_obj = FreeTriler.objects.get(windoid=request.data['windoid'])
            serializer = FreeTrailerSerlizers(firee_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 204, 'message': 'Data Update successfully'})
            else:
                return Response({'status': 403, 'error': serializer.errors})



        except FreeTriler.DoesNotExist:
            # Handle the case where the object with the specified windoid is not found
            return Response({'status': 404, 'error': 'Resource not found'})

        except Exception as e:
            # Handle other exceptions
            return Response({'status': 500, 'error': f'Internal Server Error: {str(e)}'})

    #
    # def delete(self, request):
    #     firee_obj = FreeTriler.objects.get(id=request.data['id'])
    #     firee_obj.delete()
    #     return Response({'status': 204, 'message': 'Delete Records'})
    #
    # def put(selfs, request):  # update complete package send
    #     try:
    #         firee_obj = FreeTriler.objects.get(id=request.data['id'])
    #         serializers = FreeTrailerSerlizers(firee_obj, data=request.data)
    #         if not serializers.validations():
    #             return Response({'status': 403, 'error': serializers.errors})
    #         serializers.save()
    #         return Response({'status': 200, 'payload': serializers.data, 'message': 'save data'})
    #     except Exception as e:
    #         return Response({'status': 403, 'error': 'invalid input'})


class DashbrdFreetriler(APIView):
    def get(self,request):
        if request.data['id']=='9102382767@rkmnarouipo':
            free_objs = FreeTriler.objects.all()
            serializer = FreeTrailerSerlizers(free_objs, many=True)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            return Response({'status': 403, 'error': 'invalid id'})

    def patch(self, request):
        try:
            # Get the object based on the windoid
            firee_obj = FreeTriler.objects.get(windoid=request.data['windoid'])
            serializer = FreeTrailerSerlizers(firee_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 204, 'message': 'Data Update successfully'})
            else:
                return Response({'status': 403, 'error': serializer.errors})



        except FreeTriler.DoesNotExist:
            # Handle the case where the object with the specified windoid is not found
            return Response({'status': 404, 'error': 'Resource not found'})

        except Exception as e:
            # Handle other exceptions
            return Response({'status': 500, 'error': f'Internal Server Error: {str(e)}'})

    def delete(self,request):
        try:
            firee_obj = FreeTriler.objects.get(windoid=request.data['windoid'])
            firee_obj.delete()
            return Response({'status': 204, 'message': 'Delete Records'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'error': 'Invalid Input'})



