from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                         related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()


class Image(Content):
	path = models.FilePathField()
	def info(self):
		return self.title


class Contributor(models.Model):
    cid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    content = []
    def die(self):
        self.delete()
