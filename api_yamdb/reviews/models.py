from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='category', max_length=50)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='genre', max_length=50)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(verbose_name='title', max_length=200)
    year = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='titles'
    )

    class Meta:
        ordering = ('-year',)

    def __str__(self):
        return self.name
