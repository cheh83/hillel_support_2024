from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from issues.api import (IssuesAPI, IssuesRetrieveUpdateDeleteAPI, issues_close,
                        issues_take, messages_api_dispatcher)
from users.api import UserListCreateAPI

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # users
    path("users/", UserListCreateAPI.as_view()),
    # issues
    path("issues/", IssuesAPI.as_view()),
    path("issues/<int:id>", IssuesRetrieveUpdateDeleteAPI.as_view()),
    path("issues/<int:id>/close", issues_close),
    path("issues/<int:id>/take", issues_take),
    # messages
    path("issues/<int:issue_ad>/messages", messages_api_dispatcher),
    # Authentication
    # path("auth/token/", token_obtain_pair),
    path("auth/token/", TokenObtainPairView.as_view()),
]
