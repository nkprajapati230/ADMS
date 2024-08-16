from django.contrib.auth.models import Group
from django.contrib import admin
from leaders.models import Leader

admin.site.register(Leader)
admin.site.unregister(Group)

