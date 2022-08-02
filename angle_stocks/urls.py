from django.urls import path
from angle_stocks import views
from django.views.generic import RedirectView

urlpatterns = [
    path('rs/', views.RS, name="update_rs"),
    path('delivery/', views.DeliveryData, name="delivery_update"),
    path('delivery-delete/', views.DeliveryDelete, name="delivery_delete"),
    # path('stocks/', views.Home ),
    # path('data/<int:token>/', views.GetStockData, name='stock_data'),
    # path('', RedirectView.as_view(url='stocks/'))
]