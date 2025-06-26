from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Film(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=65, verbose_name="Başlık")
    content = RichTextField("İçerik")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturma Tarihi")
    # film_image=models.FileField(blank=True,null=True,verbose_name="Filme Resim Ekleyin")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    film = models.ForeignKey(
        Film, on_delete=models.CASCADE, verbose_name="Film", related_name="comments")
    comment_author = models.CharField(
        max_length=30, verbose_name="Ad", blank=False)
    comment_content = models.CharField(
        max_length=200, verbose_name="Yorum", blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
