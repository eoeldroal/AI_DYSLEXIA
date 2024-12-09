from django.contrib import admin

from .models import *
 
admin.site.register(Lesson)
admin.site.register(UserProfile)
admin.site.register(LessonTag)
admin.site.register(Language)
admin.site.register(UserLanguage)
admin.site.register(CommunityPost)
