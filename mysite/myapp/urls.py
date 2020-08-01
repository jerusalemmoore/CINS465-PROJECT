from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.loginView),
    path('home/', views.homeView),
    path('users/',views.getUsers),
    path('login/', views.loginView),
    path('logout/', views.logoutView),
    path('signup/', views.signupView),
    path('explore/', views.exploreView),
    path('friends/',views.friendsView),
    path('password/', views.changePassword),
    path('settings/', views.settingsView),
    path('friends/<int:id>', views.guestFriendsView),
    # path('explore/<str:user>/', views.userView),
    path('chat', views.chat),
    path('chat/<str:room_name>/', views.room),
    path('delete/<int:id>/', views.postDelete),
    path('<int:id>/', views.userView),
    path('<int:id>/<str:operation>/', views.changeFriendsUserView),
    path('connect/<str:operation>/<int:id>', views.changeFriends, name='changeFriends')
    # url(r'^logout', views.logoutView, name = 'logout'),
]
