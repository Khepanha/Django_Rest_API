from django.db import models

class users (models.Model):
    user_name = models.CharField( max_length=20 )
    user_password = models.CharField( max_length=20 )
    email = models.CharField( max_length=20 )
    user_level = models.IntegerField()
class bookmark (models.Model):
    word = models.CharField( max_length=20 )
    definition = models.TextField()
    user = models.ForeignKey(users, on_delete=models.CASCADE)
class scene_percentage (models.Model):
    scene_name = models.CharField( max_length=20 )
    percentage = models.IntegerField()
    total_vocab = models.IntegerField()
    complete = models.IntegerField()
    user = models.ForeignKey(users, on_delete=models.CASCADE)
class understood (models.Model):
    word = models.CharField( max_length=20 )
    user = models.ForeignKey(users, on_delete=models.CASCADE)
class not_understood (models.Model):
    word = models.CharField( max_length=20 )
    user = models.ForeignKey(users, on_delete=models.CASCADE)

class scene (models.Model):
    scene_name = models.CharField( max_length=20 )
    scene_image = models.CharField( max_length=20 )
    level = models.IntegerField()
class recommendation (models.Model):
    scene_image = models.CharField( max_length=20 )
    scene = models.ForeignKey(scene, on_delete=models.CASCADE)
class words (models.Model):
    word = models.CharField( max_length=20 )
    pic = models.CharField( max_length=20 )
    audio = models.CharField( max_length=20 )
    synonym = models.CharField( max_length=20 )
    definition = models.TextField()
    example = models.TextField()
    scene = models.ForeignKey(scene, on_delete=models.CASCADE)



