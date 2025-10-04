from django.contrib import admin,messages
from .models import Event,participation_event

# Register your models here.
from datetime import datetime
class Evet_Filter(admin.SimpleListFilter):
    title="Event Date"
    parameter_name="evt_date"
    def lookups(self, request, model_admin):
        return (
            ('PE',('Past Event')),
            ('UE',('Upcoming Event')),
            ('TE',('Today Event')),
        )
    def queryset(self, request, queryset):
        if self.value()=='PE':
            return queryset.filter(evt_date__lt=datetime.today())
        if self.value()=='UE':
            return queryset.filter(evt_date__gt=datetime.today())
        if self.value()=='TE':
            return queryset.filter(evt_date__exact=datetime.today())
        
class Participations(admin.StackedInline):
    model=participation_event
    extra=1
    readonly_fields=('participation_date',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def accept_status(self,request,queryset):
        row_update=queryset.update(state=True)
        if(row_update==1):
            msg="1 event was"
        else:
            msg=f"{row_update} events were"
        messages.success(request,f"{msg} successfully updated")
    accept_status.short_description="state True"
    actions=[accept_status]
    list_display=('title','description','state','evt_date','category','organizer')
    ordering=('-evt_date',)
    list_per_page=1
    search_fields=('title',)
    list_filter=['title','state',Evet_Filter]
    inlines=[Participations]
    readonly_fields=('creation_date','updated_date',)
    autocomplete_fields=["organizer"]
    # fieldsets=(
    #     'Event Date',{
    #         "fields":('evt_date','creation_date','updated_date'),}
    # ),
    

# admin.site.register(Event,EventAdmin)

@admin.register(participation_event)
class Participation(admin.ModelAdmin):
    pass