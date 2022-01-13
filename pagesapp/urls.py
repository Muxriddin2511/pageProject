from django.urls import path
from .views import HomePageView,AboutpageView,SahifaPageView

urlpatterns = [
    path('sahifa/', SahifaPageView.as_view(), name='sahifa'),

    path('about/',AboutpageView.as_view(),name='about'),
    path('',HomePageView.as_view(),name='home'),

]