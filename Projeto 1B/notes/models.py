from django.db import models

# code from https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.tag}'
    
    class Meta:
        ordering = ['tag']

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id}.{self.title}.{self.tag}'