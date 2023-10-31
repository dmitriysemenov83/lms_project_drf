from rest_framework import serializers

from tutorial.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'course')


class CourseSerializer(serializers.ModelSerializer):
    # num_lessons = serializers.IntegerField(source='lesson_set.count', read_only=True)
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set')

    def get_num_lessons(self, obj):
        return Lesson.objects.all().filter(course=obj).count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

