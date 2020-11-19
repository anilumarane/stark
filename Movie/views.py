
# Create your views here.
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes

from ResponseHandle import exception_handler
from ResponseHandle.permissions import IsAdminAuth
from rest_framework.permissions import IsAuthenticated

from Movie.models import Movie
from Movie.serializers import MovieSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True, context={"request": request})
    return exception_handler.error_handling(data=serializer.data)

    # return exception_handler.error_handling(data='hello worlds')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movies(request):
    search = request.query_params.get('search')
    movie = Movie.objects.filter(Q(title__icontains=search)
                                   )
    serializer = MovieSerializer(movie,many=True, context={"request": request} )
    return exception_handler.error_handling(data=serializer.data)

