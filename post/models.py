from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    pub_date_update = models.DateTimeField('date published',null=True, blank=True)
    content = models.TextField(null=True)



    def __str__ (self):
        return 'Post : {}'.format(self.question_text)


class Comment(models.Model):
    post = models.ForeignKey(Post,
                on_delete=models.CASCADE,
                related_name='comments')
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
