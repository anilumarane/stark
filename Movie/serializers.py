from rest_framework import serializers

from Movie.models import MoviePoster, Movie


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePoster
        fields = '__all__'

    def create(self, validated_data):
        return MoviePoster.objects.create(**validated_data)
    def get_image(self, im):
        request = self.context.get('request')
        image_url = im.image.url
        return request.build_absolute_uri(image_url)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def get_movie_path(self, mv):
        request = self.context.get('request')
        movie_url = mv.movie_path.url
        return request.build_absolute_uri(movie_url)
