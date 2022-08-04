from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Image,Texts
from .serializers import FileImageSerializer, FileBasicSerializer, FileDetailsSerializer


class AddFileDetatils(APIView):

    def post(self, request, *args, **kwargs):

        file_serializer = FileBasicSerializer(data=self.request.data)
        print('********',file_serializer)
        if file_serializer.is_valid():
            _file = file_serializer.save()
            for image in self.request.FILES.getlist('images'):
                file_image = FileImageSerializer(
                    data={
                        'img': _file.id,
                        'image': image,
                     

                    }
                )
                if file_image.is_valid():
                    file_image.save()
                else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(FileDetailsSerializer(_file).data, status=status.HTTP_201_CREATED)

    def get(self,request):
        proj=Texts.objects.all()
        serializer=FileDetailsSerializer(proj,many=True)
        print('---------',serializer)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_200_CREATED)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # def get(self,request):
    #     serializer=FileDetailsSerializer(data=request.data)
    #     print('---------',serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)