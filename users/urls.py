from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('verify/<path:token>/', views.verify_user, name="verify"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path("campaign/create/", views.create_campaign, name="create-campaign"),
    path('contacts/upload/', views.upload_contacts, name="upload-contacts"),
    path('campaign/send/<int:campaign_id>/', views.send_campaign, name="send-campaign"),
    path('messages/process/', views.process_messages, name="process-messages"),
]