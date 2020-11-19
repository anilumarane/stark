from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ResponseHandle import exception_handler
from ResponseHandle.permissions import IsAdminAuth

from Movie.models import MoviePoster, Movie
from Movie.serializers import PosterSerializer, MovieSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminAuth])
def movie_create(request):
    if not request.data:
        return exception_handler.error_handling(errMsg="invalid access")

    request.data["update_by"] = request.user.id
    request.data["created_by"] = request.user.id

    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return exception_handler.error_handling(data=serializer.data)
    return exception_handler.error_handling(errMsg=serializer.errors)



@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminAuth])
def movie_update(request, movie_id):
    try:
        poster = Movie.objects.get(id=movie_id)
    except MoviePoster.DoesNotExist:
        error = "movie  id does not exist"
        return exception_handler.error_handling(errMsg=error)

    request.data["update_by"] = request.user.id
    request.data['update_by_time_stamp'] = datetime.now()
    serializer = MovieSerializer(poster, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return exception_handler.error_handling(data=serializer.data)
    return exception_handler.error_handling(errMsg=serializer.errors)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminAuth])
def movie_delete(request, movie_id):
    try:
        poster = Movie.objects.get(id=movie_id)
    except MoviePoster.DoesNotExist:
        error = "movie  id does not exist"
        return exception_handler.error_handling(errMsg=error)

    poster.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
