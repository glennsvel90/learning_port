
from django.db.models import Avg
from courses.models import Course, Review

from rest_framework import serializers



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only':True}
        }
        model = Review
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at',
        )
    def validate_rating(self, value):
        if value in range(1,6):
            return value
        raise serializers.ValidationError(
            'rating has to be between 1 and 5')


class CourseSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(
        many = True,
        read_only = True,
    )
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'reviews',
            'average_rating',
        )
        # model = models.Course
    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
            return 0

        return round(average*2) / 2
