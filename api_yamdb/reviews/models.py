from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


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


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Фильм',
    )
    text = models.TextField('Текст отзыва')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.IntegerField('Рейтинг')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='one_review'
            )
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
