from rest_framework import decorators, status
from rest_framework.response import Response
from ..serializer import CvSerializer

@decorators.api_view(['POST'])
def CreateCvView(request) : 
    try : 
        serializer = CvSerializer(data=request.data)

        if serializer.is_valid() : 
            cv = serializer.save()
            return Response(cv,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error : 
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)