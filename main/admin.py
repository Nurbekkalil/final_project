from django.contrib import admin
from main.models import News, ImageNews, Law, FavouriteLaws, Publication, FavouriteNews, FavouritePublication

admin.site.register(News)
admin.site.register(ImageNews)
admin.site.register(Law)
admin.site.register(Publication)
admin.site.register(FavouriteNews)
admin.site.register(FavouriteLaws)
admin.site.register(FavouritePublication)

