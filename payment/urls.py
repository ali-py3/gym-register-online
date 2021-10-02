from django.urls import path
from payment.views import callback_gateway_view, go_to_gateway_view

app_name = 'pay'

urlpatterns = [
    path('got-to-gateway/<int:pk>/', go_to_gateway_view, name='gateway'),
    path('callback/', callback_gateway_view),
]