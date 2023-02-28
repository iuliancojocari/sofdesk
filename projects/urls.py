from django.urls import path, include

from rest_framework_nested import routers
from .views import ProjectViewSet, ContributorViewSet, IssueViewSet

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")
contributor_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
contributor_router.register(r"users", ContributorViewSet, basename="contributors")
issue_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
issue_router.register(r"issues", IssueViewSet, basename="issues")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(contributor_router.urls)),
    path(r"", include(issue_router.urls)),
]
