from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from .permissions import (
    ProjectPermissions,
    ContributorPermissions,
    IssuePermissions,
    CommentPermissions,
)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ProjectPermissions]
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        return Project.objects.filter(contributor_project__user=self.request.user)


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ContributorPermissions]
    http_method_names = ["get", "post", "delete"]

    def initial(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs["project_pk"])
        return super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return Contributor.objects.filter(project=self.project)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project"] = self.project
        return context

    def destroy(self, request, *args, **kwargs):
        contributor = get_object_or_404(Contributor, user=self.kwargs["pk"])
        if contributor.role == "AUTHOR":
            return Response(
                {"detail": "Project author cannot be deleted !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            contributor.delete()
            return Response(
                {"detail": "Contributor successfully deleted !"},
                status=status.HTTP_204_NO_CONTENT,
            )


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IssuePermissions]
    http_method_names = ["get", "post", "put", "delete"]

    def initial(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs["project_pk"])
        return super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return Issue.objects.filter(project=self.project)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["project"] = self.project
        return context

    def destroy(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, id=self.kwargs["pk"])
        issue.delete()
        return Response(
            {"detail": "Issue successfully deleted !"},
            status=status.HTTP_202_ACCEPTED,
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentPermissions]
    http_method_names = ["get", "post", "put", "delete"]

    def initial(self, request, *args, **kwargs):
        self.issue = get_object_or_404(
            Issue, id=self.kwargs["issue_pk"], project=self.kwargs["project_pk"]
        )
        return super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(issue=self.issue)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["issue"] = self.issue
        return context
