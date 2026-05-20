from rest_framework import serializers
from ..models import Trainee, Course

        
class TraineeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_null=False)
    age = serializers.IntegerField(allow_null=False)
    image = serializers.ImageField(required=False, allow_null=True)
    degree = serializers.DecimalField(decimal_places=2,max_digits=4,allow_null=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Trainee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name      = validated_data.get('name', instance.name)
        instance.age       = validated_data.get('age', instance.age)
        instance.image     = validated_data.get('image', instance.image)
        instance.degree    = validated_data.get('degree', instance.degree)
        instance.course    = validated_data.get('course', instance.course)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance