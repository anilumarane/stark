from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ResponseHandle import exception_handler
from ResponseHandle.permissions import IsAdminAuth

from Movie.models import MoviePoster
from Movie.serializers import PosterSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminAuth])
def poster_create(request):
    if not request.data:
        return exception_handler.error_handling(errMsg="invalid access")
    request.data["update_by"] = request.user.id
    request.data["created_by"] = request.user.id
    serializer = PosterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return exception_handler.error_handling(data=serializer.data)
    return exception_handler.error_handling(errMsg=serializer.errors)



@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminAuth])
def poster_update(request, poster_id):
    try:
        poster = MoviePoster.objects.get(id=poster_id)
    except MoviePoster.DoesNotExist:
        error = "poster  id does not exist"
        return exception_handler.error_handling(errMsg=error)
    request.data["update_by"] = request.user.id
    request.data['update_by_time_stamp'] = datetime.now()
    serializer = PosterSerializer(poster, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return exception_handler.error_handling(data=serializer.data)
    return exception_handler.error_handling(errMsg=serializer.errors)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminAuth])
def poster_delete(request, poster_id):
    try:
        poster = MoviePoster.objects.get(id=poster_id)
    except MoviePoster.DoesNotExist:
        error = "poster  id does not exist"
        return exception_handler.error_handling(errMsg=error)

    poster.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
