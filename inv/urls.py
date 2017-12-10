from django.urls import path

from . import views

app_name = 'inv'
urlpatterns = [
  path('lc/create/', views.LCCreateView.as_view(), name='lc_createview'),
  path('lc/update/<int:pk>/', views.LCUpdateView.as_view(), name='lc_updateview'),
  path('lc/list/', views.LCListView.as_view(), name='lc_listview'),
  path('lc/<int:pk>/', views.LCDetailView.as_view(), name='lc_detailview'),
  path('lc/search/', views.LCSearchView.as_view(), name='lc_searchview'),
  path('lc/search/result/', views.LCSearchResultListView.as_view(), name='lc_search_result_listview'),

  path('yarn/rcv/create/<int:lc_item_pk>/', views.YarnRcvCreateView.as_view(), name='yarn_rcv_createview'),
]
