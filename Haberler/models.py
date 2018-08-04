from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField


# TODO: CREATE THE TURKISH VERSION OF THE ADMIN PANEL
# Ayarlar
class Settings(models.Model):
    LogoImage = models.ImageField()


class NewsSiteBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")

    class Meta:
        abstract = True


class Category(NewsSiteBaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name


class SubCategory(NewsSiteBaseModel):
    category = models.ForeignKey(on_delete=None, to=Category, verbose_name="Ebeveyn kategori")
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return "%s > %s" % (self.category, self.name)


class Industry(NewsSiteBaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Industries"

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    active = models.BooleanField()

    class Meta:
        verbose_name_plural= "Kaynaklar"

    def __str__(self):
        return self.name


class HashTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(NewsSiteBaseModel):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    source = models.ForeignKey(on_delete=None, to=Source, verbose_name="Haber Kaynağı")
    category = models.ForeignKey(on_delete=None, to=Category, verbose_name="Kategori")
    sub_category = models.ForeignKey(on_delete=None, to=SubCategory, blank=True, null=True, default=None, verbose_name="Ebeveyn kategori")
    hash_tags = models.ManyToManyField(HashTag, blank=True, default=None, verbose_name="Etiket")
    cover_image = models.ImageField(verbose_name="Görsel Ekle")
    full_text = RichTextField(blank=True, null=True, verbose_name="Haber Detayı")
    published_on = models.DateTimeField(auto_now_add=True, verbose_name="Yayınlama Tarihi")
    active = models.BooleanField(verbose_name="Sıcak Haber")
    hot = models.BooleanField(verbose_name="Flash Haber")
    popular = models.BooleanField(verbose_name="Manşet Haber")
    avg_rating = models.FloatField()
    view_count = models.FloatField()
    rating_count = models.FloatField()

    class Meta:
        verbose_name_plural = "Yazılar"

    def __str__(self):
        return self.title


class ArticleMedia(NewsSiteBaseModel):
    article = models.ForeignKey(on_delete=None, to=Article)
    category = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return "%s > %s" % (self.article, self.category)


# TODO: add reference to User model
class ArticleRating(NewsSiteBaseModel):
    article = models.ForeignKey(on_delete=None, to=Article)
    rating = models.FloatField()

    def __str__(self):
        return "%s -> %s" % (self.article, self.rating)


class RelatedArticle(NewsSiteBaseModel):
    source = models.ForeignKey(on_delete=None, to=Article, related_name="source_article")
    related = models.ForeignKey(on_delete=None, to=Article, related_name="related_article")
    score = models.FloatField()

    def __str__(self):
        return "%s -> %s" % (self.source, self.related)



