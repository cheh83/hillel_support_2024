from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView  # noqa
from rest_framework_simplejwt.views import token_obtain_pair  # noqa

from issues.api import IssuesAPI  # noqa
from issues.api import IssuesRetrieveUpdateDeleteAPI  # noqa
from issues.api import issues_close  # noqa
from issues.api import issues_take  # noqa
from issues.api import messages_api_dispatcher  # noqa; noqa
from users.api import UserListCreateAPI, resend_activation_mail

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # users
    path("users/", UserListCreateAPI.as_view()),
    path("users/activation/resendActivation", resend_activation_mail),
    # issues
    path("issues/", IssuesAPI.as_view()),
    path("issues/<int:id>", IssuesRetrieveUpdateDeleteAPI.as_view()),
    path("issues/<int:id>/close", issues_close),
    path("issues/<int:id>/take", issues_take),
    # messages
    path("issues/<int:issue_id>/messages", messages_api_dispatcher),
    # Authentication
    # path("auth/token/", token_obtain_pair),
    path("auth/token/", TokenObtainPairView.as_view()),
]
