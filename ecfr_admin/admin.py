from django.contrib import admin
# Register your models here.
from .models import Departments, Faculties
# from results.models import DeclareResult
# from student_classes.models import StudentClass
from students.models import Student
from subjects.models import Subject, SubjectRegistered


class EcfrDbAdmin(admin.ModelAdmin):
    using = 'ecfr_db'
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)
    def delete_model(self, request, obj):
        obj.delete(using=self.using)
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


admin.site.register(Faculties, EcfrDbAdmin)
admin.site.register(Departments, EcfrDbAdmin)
# admin.site.register(DeclareResult, ecfrDbAdmin)
# admin.site.register(StudentClass, ecfrDbAdmin)
admin.site.register(Student, EcfrDbAdmin)
admin.site.register(Subject, EcfrDbAdmin)
admin.site.register(SubjectRegistered, EcfrDbAdmin)


# class AuthDbAdmin(admin.ModelAdmin):
#     # A handy constant for the name of the alternate database.
#     using = 'sn_auth_db'

#     def save_model(self, request, obj, form, change):
#         # Tell Django to save objects to the 'other' database.
#         obj.save(using=self.using)

#     def delete_model(self, request, obj):
#         # Tell Django to delete objects from the 'other' database
#         obj.delete(using=self.using)

#     def get_queryset(self, request):
#         # Tell Django to look for objects on the 'other' database.
#         return super().get_queryset(request).using(self.using)

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         # Tell Django to populate ForeignKey widgets using a query
#         # on the 'other' database.
#         return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         # Tell Django to populate ManyToMany widgets using a query
#         # on the 'other' database.
#         return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


