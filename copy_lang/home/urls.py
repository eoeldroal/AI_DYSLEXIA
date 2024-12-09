from django.urls import path

from home.views.index import index
from home.views.dashboard import dashboard
from home.views.community_posts import community_posts
from home.views.update_profile import update_profile
from home.views.create_lesson import create_lesson
from home.views.create_community_post import create_community_post
from home.views.login import login
from home.views.logout import logout
from home.views.signup import signup
from home.views.lesson_detail import lesson_detail
from home.views.create_lesson_tag import create_lesson_tag
from home.views.language import language
from home.views.select_favorite_language import select_favorite_language
from home.views.highlightingapp import play_audio, page_view,generate_question, lookup_word_explanation
from home.views.process_text import process_text

urlpatterns = [
    path('', index, name="index"),
    path('signup', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('community/', community_posts, name='community_posts'),
    path('community/create/', create_community_post,
         name='create_community_post'),
    path('update-profile/', update_profile, name='update_profile'),
    path('create_lesson/', process_text, name='create_lesson'),
    path('select_favorite_language/', select_favorite_language,
         name='select_favorite_language'),
    path('create_lesson_tag/', create_lesson_tag, name='create_lesson_tag'),
    path('language/', language, name='language'),
    path('lookup_word/<str:word>/', lookup_word_explanation, name='lookup_word_explanation'),
    path('play_audio/<str:audio_file>/', play_audio, name='play_audio'),
    path('page/<int:page_number>/', page_view, name='page_view'),
    path('generate_question/', generate_question, name='generate_question'),

]