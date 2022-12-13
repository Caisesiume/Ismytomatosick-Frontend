
from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Title', )
    image_file = models.JSONField(blank=False, null=False, verbose_name='Image File')

    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Disease'

    def __str__(self):
        return "{}({})".format(self.title, self.id,)

    def image_tag(self):
        return self.create_img_tag(
            img_url=self.image_file.url,
            alt_text=self.title,
        )