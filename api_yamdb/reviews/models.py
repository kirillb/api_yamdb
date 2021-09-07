from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='category', max_length=256)
    slug = models.SlugField(
        verbose_name='category slug',
        unique=True,
        max_length=50
    )

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='genre', max_length=50)
    slug = models.SlugField(
        verbose_name='genre slug',
        unique=True,
        max_length=50
    )

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(verbose_name='title', max_length=256)
    year = models.IntegerField(verbose_name='year of issue')
    description = models.TextField(
        verbose_name='description',
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='genre title'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='category title'
    )

    class Meta:
        ordering = ('-year',)

    def __str__(self):
        return self.name
