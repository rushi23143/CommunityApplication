from django.contrib import admin
#from community_app.models import Contact
#from community_app.models import Service
#from community_app.models import Query
#from community_app.models import Answer
from.models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Query)
admin.site.register(Answer)