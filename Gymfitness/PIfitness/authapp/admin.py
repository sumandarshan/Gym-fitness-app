from django.contrib import admin
from authapp.models import Contact,Trainer,MembershipPlan,Enrollment,Gallery,WorkoutLog

# Register your models here.
admin.site.register(Contact)
admin.site.register(Trainer)
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Gallery)
admin.site.register(WorkoutLog)