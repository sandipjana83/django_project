
from django.urls import path
from . import views
urlpatterns = [
    path('',views.AllChai,name='all_home'),
    path('<int:chai_id>/',views.View_Details,name='all_details'),
    path('stores/',views.ChaiStores,name='all_stores'),
]