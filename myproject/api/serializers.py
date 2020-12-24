from rest_framework import serializers
from .models import users
from .models import bookmark
from .models import scene_percentage
from .models import understood
from .models import not_understood
from .models import scene
from .models import recommendation
from .models import words

class usersSerializers (serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
class bookmarkSerializers (serializers.ModelSerializer):
    class Meta:
        model = bookmark
        fields = '__all__'
class scene_percentageSerializers (serializers.ModelSerializer):
    class Meta:
        model = scene_percentage
        fields = '__all__'
class understoodSerializers (serializers.ModelSerializer):
    class Meta:
        model = understood
        fields = '__all__'
class not_understoodSerializers (serializers.ModelSerializer):
    class Meta:
        model = not_understood
        fields = '__all__'
class sceneSerializers (serializers.ModelSerializer):
    class Meta:
        model = scene_percentage
        fields = '__all__'
class recommendationSerializers (serializers.ModelSerializer):
    class Meta:
        model = recommendation
        fields = '__all__'
class wordSerializers (serializers.ModelSerializer):
    class Meta:
        model = words
        fields = '__all__'
