from django.urls import path
from app.views import index,management,operations,engineering,e_form,m_form,o_form
urlpatterns = [
    path('index/',index),
    path('engineering/',engineering),
    path('management/',management),
    path('operations/',operations),
    path('eform/',e_form),
    path('mform/',m_form),
    path('oform/',o_form),
]
