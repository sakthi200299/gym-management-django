from django.urls import path, include

urlpatterns = [
    path('api/gym/users/', include('users.urls')),
    path('api/gym/plans/', include('plans.urls')),
    path('api/gym/subscriptions/', include('subscriptions.urls')),
    path('api/gym/trainers/', include('trainers.urls')),
    path('api/gym/exercises/', include('exercises.urls')),
]
