from django.contrib import admin

# Register your models here.


from .models import (Category, SubCategory,
                     Industry, Source, HashTag, Article, ArticleMedia,
                     ArticleRating, RelatedArticle, Settings)

admin.site.register(Settings)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Industry)
admin.site.register(Source)
admin.site.register(HashTag)
admin.site.register(Article)
admin.site.register(ArticleMedia)
admin.site.register(ArticleRating)
admin.site.register(RelatedArticle)
