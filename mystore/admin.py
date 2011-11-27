from django.contrib import admin
from c10shop.mystore.models import Catalog, Category, Recipe, Purchase, RecipeDetail

class RecipeDetailInline(admin.StackedInline):
    model = RecipeDetail

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'pub_date')
    search_fields  = ('name',)
    inlines = [
        RecipeDetailInline,
    ]

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchaser', 'recipe', 'purchased_date')
    search_fields = ('purchaser',)

admin.site.register(Catalog)
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(RecipeDetail)