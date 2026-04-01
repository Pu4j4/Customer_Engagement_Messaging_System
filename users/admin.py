from django.contrib import admin
from .models import User, Campaign, Plan, Document, Contact, MessageLog, UserSubscription

# Register your models here.
admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Campaign)
admin.site.register(Document)
admin.site.register(Contact)
admin.site.register(MessageLog)
admin.site.register(UserSubscription)
