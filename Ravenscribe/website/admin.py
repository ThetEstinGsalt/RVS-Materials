from django.contrib import admin
from .models import Contact, cardimage, contacts, about, social, subscribe

# Register your models here.
admin.site.register(Contact)
admin.site.register(cardimage)
admin.site.register(contacts)
admin.site.register(about)
admin.site.register(social)
admin.site.register(subscribe)
