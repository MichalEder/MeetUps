from django.contrib import admin

from .models import MeetUp, Location, Participant, Organizer, Registration

# Register your models here.
class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 1
class MeetUpAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'organizer')
    list_filter = ('location', 'date', 'organizer')
    inlines = (RegistrationInline,)
    prepopulated_fields = {'slug': ('title',)}

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('meetup', 'participant')


admin.site.register(MeetUp, MeetUpAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Organizer)
admin.site.register(Registration, RegistrationAdmin)