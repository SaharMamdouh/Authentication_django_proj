from django.contrib import admin
from .models import Movie , Category ,Cast , Review
# Register your models here.
class InlineReview(admin.StackedInline):
    model=Review

class MovieAdmin(admin.ModelAdmin):
    list_filter=('name',)
    search_fields=('name','rate','actors__cast_name')
    list_display=('name','rate','language')
    readonly_fields=("new_custom_field",)
    inlines = [InlineReview]

    def new_custom_field(self,obj):
        new_rate=obj.rate
        if new_rate:
            return 20* new_rate
        else:
            return new_rate

    new_custom_field.short_description="watch counts"

    fieldsets = (
    ["Section A" , {"fields": ["name", "description","language"]}],
    ["Section B", {"fields": ["running_time", "rate", "release_date","new_custom_field"]}],
    ["Section C", {"fields":["image", "video","active"]}],
    )

    def has_delete_permission(self,request,obj=None):
        if request.user.username=='Sahar':
            return True
        return False


admin.site.register(Movie,MovieAdmin),
admin.site.register(Category),
admin.site.register(Cast),
admin.site.register(Review)