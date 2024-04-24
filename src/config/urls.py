from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView  # noqa

from issues.api import IssuesAPI  # noqa
from issues.api import IssuesRetrieveUpdateDeleteAPI  # noqa
from issues.api import issues_close  # noqa
from issues.api import issues_take  # noqa
from issues.api import messages_api_dispatcher  # noqa; noqa
from users.api import UserListCreateAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", UserListCreateAPI.as_view()),
    path("issues/", IssuesAPI.as_view()),
    path("issues/<int:id>", IssuesRetrieveUpdateDeleteAPI.as_view()),
    path("issues/<int:id>/close", issues_close),
    path("issues/<int:id>/take", issues_take),
    path("issues/<int:issue_ad>/messages", messages_api_dispatcher),
    path("auth/token/", TokenObtainPairView.as_view()),
]
