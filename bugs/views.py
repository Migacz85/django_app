from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bugs
from .forms import BugForm


def get_bugs(request):
    """ Show all bugs """

    bugs = Bugs.objects.filter(
        published_date__lte=timezone.now()) .order_by('-published_date')

    return render(request, "get_bugs.html", {'bugs': bugs})


def get_bug_detail(request, pk):
    """ Show details about single bug
    based on single post id """
    bug = get_object_or_404(Bugs, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "get_bug_detail.html", {'bug': bug})


def create_or_edit_bug(request, pk=None):
    """ View that allows to create or edit bug """
    bug = get_object_or_404(Bugs, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)

        if form.is_valid():
            bug = form.save(commit=False)
            bug.username = request.user
            bug.created_date = timezone.now()
            bug = form.save()

            return redirect(get_bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'create_or_edit_bug.html', {'form': form})
