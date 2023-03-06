from django.urls import path, include

from rest_framework_nested import routers
from .views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

# Root router
# Generate the endopoints below
# /projects/
# /projects/:project_id/
router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")

# Router based on the root router -> projects
# Generate the endpoints below (plus the root endpoints)
# /projects/:project_id/users/
# /projects/:project_id/users/:user_id/
contributor_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
contributor_router.register(r"users", ContributorViewSet, basename="contributors")

# Router based on the root router -> projects
# Generate the endpoints below (plus the root endpoints)
# /projects/:project_id/issues/
# /projects/:project_id/issues/:issue_id/
issue_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
issue_router.register(r"issues", IssueViewSet, basename="issues")

# Router based on the issue router -> issues
# Generate the endpoints below (plus the issue endpoints)
# /projects/:project_id/issues/:issue_id/comments/
# /projects/:project_id/issues/:issue_id/comments/:comment_id/
comment_router = routers.NestedDefaultRouter(issue_router, r"issues", lookup="issue")
comment_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(contributor_router.urls)),
    path(r"", include(issue_router.urls)),
    path(r"", include(comment_router.urls)),
]
