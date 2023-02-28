from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

TYPES = [
    ("BACKEND", "BACKEND"),
    ("FRONTEND", "FRONTEND"),
    ("iOS", "iOS"),
    ("ANDROID", "ANDROID"),
]

PRIORITIES = [("LOW", "LOW"), ("MEDIUM", "MEDIUM"), ("HIGH", "HIGH")]

TAGS = [("TASK", "TASK"), ("BUG", "BUG"), ("IMPROVEMENT", "IMPROVEMENT")]

STATUS = [
    ("ASSIGNED", "ASSIGNED"),
    ("IN PROGRESS", "IN PROGRESS"),
    ("RESOLVED", "RESOLVED"),
]

ROLES = [("AUTHOR", "AUTHOR"), ("CONTRIBUTOR", "CONTRIBUTOR")]


class Project(models.Model):
    title = models.CharField(_("project title"), max_length=150, blank=False)
    description = models.TextField(
        _("project description"), max_length=2000, blank=True
    )
    type = models.CharField(_("project type"), choices=TYPES, max_length=8, blank=False)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_author",
    )


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributor",
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributor_project"
    )
    role = models.CharField(
        _("contributor role"), choices=ROLES, max_length=11, blank=False
    )


class Issue(models.Model):
    title = models.CharField(_("issue title"), max_length=150, blank=False)
    description = models.TextField(_("issue description"), max_length=2000, blank=True)
    priority = models.CharField(
        _("issue priority"), choices=PRIORITIES, max_length=6, blank=False
    )
    tag = models.CharField(_("issue tag"), choices=TAGS, max_length=11, blank=False)
    status = models.CharField(
        _("issue status"), choices=STATUS, max_length=11, blank=False
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="project_concerned",
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="issue_author",
    )
    assigned_to = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="issue_assigned_to",
    )
    created_at = models.DateTimeField(_("issue created at"), auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(
        _("comment description"), max_length=2000, blank=False
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment_author",
    )
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name="issue_comment"
    )
    created_at = models.DateTimeField(
        _("comment created date, time"), auto_now_add=True
    )
