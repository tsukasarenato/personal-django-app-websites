from django.contrib import admin
from .models import Websites, Categories, Products, Groups, Options, \
    Banners, Contacts, Icons, Colors


class ContactsInline(admin.StackedInline):
    model = Contacts


class IconsInline(admin.StackedInline):
    model = Icons


class ColorsInline(admin.StackedInline):
    model = Colors


class ProductsInline(admin.StackedInline):
    model = Products
    extra = 1


class GroupsInline(admin.StackedInline):
    model = Groups
    extra = 1


class OptionsInline(admin.StackedInline):
    model = Options
    extra = 1


class WebsitesAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'home', 'timezone', 'currency', 'is_available', 'get_created_at')

    inlines = [
        ContactsInline,
        IconsInline,
        ColorsInline,
    ]


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'get_created_at')

    inlines = [
        ProductsInline,
    ]


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'images', 'price', 'price_type', 'is_available', 'get_created_at')

    inlines = [
        GroupsInline,
    ]


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'price_type', 'maximum', 'minimum', 'get_created_at')

    inlines = [
        OptionsInline,
    ]


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'maximum', 'minimum', 'get_created_at')


class BannersAdmin(admin.ModelAdmin):
    list_display = ('title', 'images', 'get_created_at')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'telephone', 'facebook', 'twitter', 'linkedin', 'instagram', 'get_created_at')


class IconsAdmin(admin.ModelAdmin):
    list_display = ('shortcut', 'account', 'cart', 'search', 'home', 'get_created_at')


class ColorsAdmin(admin.ModelAdmin):
    list_display = ('navbar', 'category', 'active', 'footer', 'text', 'title', 'title_hover', 'get_created_at')


admin.site.register(Websites, WebsitesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Options, OptionsAdmin)
admin.site.register(Banners, BannersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Icons, IconsAdmin)
admin.site.register(Colors, ColorsAdmin)
