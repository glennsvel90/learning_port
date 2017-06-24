from rest_framework.serializers import ModelSerializer

from courses.models import Course, Review

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
        )
        # model = models.Course


class ReviewSerializer(ModelSerializer):
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
        # model = models.Review
