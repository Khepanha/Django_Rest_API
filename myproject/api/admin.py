from django.contrib import admin
from .models import users
from .models import bookmark
from .models import scene_percentage
from .models import understood
from .models import not_understood
from .models import scene
from .models import recommendation
from .models import words
# Register your models here.
admin.site.register(users)
admin.site.register(bookmark)
admin.site.register(scene_percentage)
admin.site.register(understood)
admin.site.register(not_understood)
admin.site.register(scene)
admin.site.register(recommendation)
admin.site.register(words)
