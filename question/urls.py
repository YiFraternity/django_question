from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.urls import path
from . import views

app_name = "question"

urlpatterns = [
        #ex:/question/
        path('index/', views.index,name='index'),
        path('register/',views.register,name='register'),
        path('login/',views.login,name='login'),
        path('quest/',views.question,name='quest'),
        path('type/',views.type,name='type'),
        path('default/',views.default,name='default'),
        path('ask-question/',views.ask_question,name='ask-question'),
        path('question/<str:question>/',views.get_quest,name='each-question'),
        path('type/<int:qType>/',views.type_quests,name="type-questions"),
        path('show-answer/',views.show_answer,name='show-answer'),
        path('search/',views.search,name='search'),
        path('practice/',views.practice,name='practice'),
        path('practice-show-answer/',views.practice_show_answer,name='practice-show-answer'),
        path('practice/<str:question>/',views.practice_quest,name='practice-each-question'),
        path('practice-ask-question/',views.practice_ask_answer,name='practice-ask-question'),
        path('practice-continue/',views.practice_continue,name='practice-continue'),
]
urlpatterns += staticfiles_urlpatterns()
