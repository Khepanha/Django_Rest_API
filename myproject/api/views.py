from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import usersSerializers
from .serializers import bookmarkSerializers
from .serializers import scene_percentageSerializers
from .serializers import understoodSerializers
from .serializers import not_understoodSerializers
from .serializers import sceneSerializers
from .serializers import recommendationSerializers
from .serializers import wordSerializers
from .models import users
from .models import bookmark
from .models import scene_percentage
from .models import understood
from .models import not_understood
from .models import scene
from .models import recommendation
from .models import words
# Create your views here.

class usersData (APIView):
    def get(self, request, id):
        # data = users.objects.all()
        data = users.objects.filter(id = id)
        word = usersSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class bookmarkData (APIView):
    def get(self, request):
        data = bookmark.objects.all()
        word = bookmarkSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class scene_percentageData (APIView):
    def get(self, request):
        data = scene_percentage.objects.all()
        word = scene_percentageSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class readScene_Percentage_By_user_idData(APIView):
    def get(self, request, user_id):
        data = scene_percentage.objects.filter(user_id = user_id)
        word = scene_percentageSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class understoodData (APIView):
    def get(self, request):
        data = understood.objects.all()
        word = understoodSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class not_understoodData (APIView):
    def get(self, request):
        data = not_understood.objects.all()
        word = not_understoodSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class sceneData (APIView):
    def get(self, request):
        data = scene.objects.all()
        word = sceneSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class readScene_By_LevelData (APIView):
    def get(self, request, lvl):
        data = scene.objects.filter(level = lvl)
        word = sceneSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class recommendationData (APIView):
    def get(self, request):
        data = recommendation.objects.all()
        word = recommendationSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class wordData (APIView):
    def get(self, request):
        data = words.objects.all()
        word = wordSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass
class readWord_By_Scene_idData (APIView):
    def get(self, request, scene_id):
        data = words.objects.filter(scene_id = scene_id)
        word = wordSerializers(data, many = True)
        return Response(word.data)
    def post(self): pass