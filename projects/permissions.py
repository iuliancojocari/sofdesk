from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .models import Project, Issue


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return Project.objects.filter(
                contributor_project__user=request.user
            ).exists()
        return Project.objects.filter(author=request.user).exists()


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
                id=view.kwargs["project_pk"], project_concerned__author=request.user
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
        return Issue.objects.filter(
            id=view.kwargs["issue_pk"],
            issue_comment__author=request.user,
        ).exists()
