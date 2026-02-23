from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=("id","title","author","price","pub_date")
    list_filter=("author",)
    list_editable=("price",)
    search_fields=("author","title",)
    ordering=("id",)
    actions=['Mark_Free']
    
    def Mark_Free(self,request,queryset):
        queryset.update(price=0)
        self.message_user(request,"Selected book has been marked as free")
        
    Mark_Free.short_description ="Mark selected book as free"


admin.site.register(Book, BookAdmin)