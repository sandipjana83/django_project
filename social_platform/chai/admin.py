from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate


class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 2


class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_add', 'price')
    inlines = [ChaiReviewInLine]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varity',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


class ChaiReviewAdmin(admin.ModelAdmin):
    list_display = ('chai', 'user', 'rating', 'date')


admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiReview, ChaiReviewAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)