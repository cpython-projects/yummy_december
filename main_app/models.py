from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class MainMenuItems(models.Model):
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='url')
    url = models.CharField(max_length=100, blank=True)
    is_anchor = models.BooleanField(default=False)
    is_manager_only = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        if self.is_anchor:
            return reverse('yummy:home') + f'#{self.slug}'
        return self.slug

    def __str__(self):
        return f'{self.title}/{self.slug}'

    class Meta:
        ordering = ('order',)


class Footer(models.Model):
    address = RichTextField()
    reservation = RichTextField()
    opening_hours = RichTextField()
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    copyright_text = RichTextField()
    credits_text = RichTextField()

    def __str__(self):
        return 'Footer Info'
