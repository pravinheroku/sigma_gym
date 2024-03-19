from django.contrib import admin
from authapp.models import (
    Contact,
    Trainer,
    MembershipPlan,
    Enrollment,
    GALLERY,
    Attendance,
)

# Register your models here.


class MembershipAdmin(admin.ModelAdmin):
    list_display = ("plan", "price")


admin.site.register(Contact)
admin.site.register(Trainer)
admin.site.register(MembershipPlan, MembershipAdmin)
admin.site.register(Enrollment)
admin.site.register(GALLERY)
admin.site.register(Attendance)
