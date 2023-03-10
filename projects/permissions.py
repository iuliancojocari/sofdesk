from rest_framework import permissions

from .models import Project, Issue


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return Project.objects.filter(
                contributor_project__user=request.user
            ).exists()
        return Project.objects.filter(author=request.user).exists() or True


class ContributorPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return Project.objects.filter(
                id=view.kwargs["project_pk"], contributor_project__user=request.user
            ).exists()
        return Project.objects.filter(
            id=view.kwargs["project_pk"], author=request.user
        ).exists()


class IssuePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return Project.objects.filter(
                id=view.kwargs["project_pk"], contributor_project__user=request.user
            ).exists()
        return Project.objects.filter(
            id=view.kwargs["project_pk"], author=request.user
        ).exists()


class CommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return Project.objects.filter(
                id=view.kwargs["project_pk"], contributor_project__user=request.user
            ).exists()
        elif request.method == "POST":
            return Project.objects.filter(
                id=view.kwargs["project_pk"], contributor_project__user=request.user
            ).exists()
        return Project.objects.filter(
            id=view.kwargs["project_pk"],
            project_concerned__author=request.user,
        ).exists()
