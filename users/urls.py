from django.urls import path
from .views import AdminPageView, UserPageView, chart_view
urlpatterns = [
    path('chart/', chart_view, name='chart-view'),
    path('trader/', UserPageView.as_view(), name='userpage'),
    path('', AdminPageView.as_view(), name='index')
]