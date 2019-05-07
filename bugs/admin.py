from django.contrib import admin
from .models import Issues, IssueUpvote


class BugAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return Issues.objects.filter(issue_type='Bug')


class Feature(Issues):
    class Meta:
        proxy = True


class Bugs(Issues):
    class Meta:
        proxy = True

class FeatureAdmin(BugAdmin):

    def get_queryset(self, request):
        return Issues.objects.filter(issue_type='Feature')


admin.site.register(Bugs, BugAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(IssueUpvote)
