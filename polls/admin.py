from django.contrib import admin
from .models import *
# Register your models here.





#admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        #print("obj: ",self.readonly_fields )

        if obj:  # editing an existing object
            return  ('start_date',)
        return self.readonly_fields

    #readonly_fields = ["start_date"]
    #list_display = ('id', 'cond',  'name','publ_date', 'end_date','authtor' )
    #list_filter = ('id','authtor','publ_date' )
    #fields = [('name','cond' ), 'descr','authtor',('attributes','witrin_readers' ), ('publ_date', 'end_date')]

admin.site.register(Question, QuestionAdmin)


admin.site.register(Option)
admin.site.register(MultiOption)
admin.site.register(Answer)

