from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Serial(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=512)
    description = models.TextField()

    genres = models.ManyToManyField(Genre, related_name='serials')

    is_buy_forever = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    poster = models.ImageField(upload_to='serials')

    release_date = models.DateTimeField(
        null=True, blank=True, verbose_name='Дата выхода'
    )

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)
    serial = models.ForeignKey(Serial, related_name='series', on_delete=models.CASCADE)
    description = models.TextField()
    poster = models.ImageField(upload_to='series')
    release_date = models.DateTimeField(
        null=True, blank=True, verbose_name='Дата выхода'
    )

    def __str__(self):
        return self.name


class ShowCase(models.Model):
    name = models.CharField(max_length=255)
    serials = models.ManyToManyField(Serial)

    def __str__(self):
        return self.name
