from django.contrib import admin

from students.models import Student

class StudentAdmin(admin.ModelAdmin):
  list_display=['Full_name','email','skype']
  search_fields = ['surname','email']
  list_filter = ['courses']
  fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', { 
            'fields': ('email', 'phone', 'address','skype')
        }),
        (None, {
            'fields': ('courses', ),
        }),
    )



  def Full_name(self, obj):
    return "%s %s" % (obj.name, obj.surname)

admin.site.register(Student,StudentAdmin)