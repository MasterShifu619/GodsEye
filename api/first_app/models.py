from django.db import models

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
#shows video information
#testing auto git push
class Video_info(models.Model):
    name = models.CharField(max_length=500)
    ifps = models.IntegerField(default=25)
    ofps = models.IntegerField(default=4)
    no_of_people = models.IntegerField(default=3)
    any_violence = models.CharField(max_length=10, default='No')
    time_taken = models.IntegerField(default=10)


