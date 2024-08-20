from django.contrib.auth.models import Group
from django.contrib import admin
from leaders.models import Leader,leadersProfile

admin.site.register(Leader)
admin.site.register(leadersProfile)
admin.site.unregister(Group)

