from django.contrib import admin
from rango.models import Category, Page, UserProfile
from django.contrib.sessions.models import Session

class CategoryAdmin(admin.ModelAdmin):
	prepopulate_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)

class SessionAdmin(admin.ModelAdmin):
	def _session_data(self, object):
		return object.get_decoded()
	list_display = ['session_key', 'session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)