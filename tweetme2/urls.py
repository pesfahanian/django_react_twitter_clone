from django.contrib import admin
from django.urls import path

from tweets.views import home, tweet_detail, tweet_lits

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('tweets/<int:tweet_id>', tweet_detail),
    path('tweets', tweet_lits),
]