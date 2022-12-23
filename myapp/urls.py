from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('error',views.error,name='error'),
    path('note/<int:post_id>',views.post_by_id,name='post_by_id'),
    path('notes/<str:collection>',view=views.notes,name='notes'),
    path('deletePost/<int:post_id>/<str:collection>',views.deletePost,name='deletePost'),
    path('login',view=views.login,name='login'),
    path('register',view=views.register,name='register'),
    path('player',view=views.player,name='player'),
    path('clips',view=views.clips,name='clips'),
    path('lib',view=views.lib,name='lib'),
    path('logout',view=views.logout,name='logout'),
] 