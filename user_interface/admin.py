from django.contrib import admin
from user_interface.models import BookMark, PaperTrade, TradeJournal

# Register your models here.
admin.site.register(BookMark)
admin.site.register(PaperTrade)
admin.site.register(TradeJournal)
