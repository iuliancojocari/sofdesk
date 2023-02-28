from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Project, Contributor, Issue
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer
from .permissions import ProjectPermissions, ContributorPermissions, IssuePermissions


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

    def get_queryset(self):
        self.project = get_object_or_404(Project, id=self.kwargs["project_pk"])
        return Contributor.objects.filter(project=self.project)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        querySet = self.get_queryset()
        context["project"] = self.project
        context["querySet"] = querySet
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

    def get_queryset(self):
        self.project = get_object_or_404(Project, id=self.kwargs["project_pk"])
        return Issue.objects.filter(project=self.project)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        querySet = self.get_queryset()
        context["project"] = self.project
        context["querySet"] = querySet
        return context

    # reste à faire la suppression d'une issue
    # travailler les permissions
