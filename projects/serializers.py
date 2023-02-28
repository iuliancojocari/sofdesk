from rest_framework import serializers

from .models import Project, Contributor, Issue
from users.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ("id", "author")

    def create(self, validated_data):
        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author_id=self.context["request"].user.id,
        )
        project.save()
        Contributor.objects.create(
            user=self.context["request"].user, project=project, role="AUTHOR"
        )
        return project


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"
        read_only_fields = ("id", "role", "project")

    def create(self, validated_data):
        try:
            Contributor.objects.get(
                user=validated_data["user"], project=self.context["project"]
            )
            raise serializers.ValidationError(
                {"detail": "This user already exist as contributor !"}
            )
        except Contributor.DoesNotExist:
            try:
                contributor = Contributor.objects.create(
                    user=validated_data["user"],
                    project=self.context["project"],
                    role="CONTRIBUTOR",
                )
                contributor.save()
                return contributor
            except User.DoesNotExist:
                raise serializers.ValidationError({"message": "User not found !"})


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ("id", "project", "author", "created_at")

    def create(self, validated_data):
        try:
            Contributor.objects.get(
                user=validated_data["assigned_to"], project=self.context["project"]
            )
            try:
                issue = Issue.objects.create(
                    project=self.context["project"],  # get_serializer_context
                    author=self.context["request"].user,
                    **validated_data
                )
                issue.save()
                return issue
            except User.DoesNotExist:
                raise serializers.ValidationError({"detail": "User not found !"})
        except Contributor.DoesNotExist:
            raise serializers.ValidationError({"detail": "Contributor not found !"})
