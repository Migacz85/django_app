from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bugs, BugsUpvote, Comments
from .forms import BugForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def get_bugs(request):
    """ Show list of all bugs """

    bugs = Bugs.objects.filter(
        published_date__lte=timezone.now()) .order_by('-published_date')
    paginator = Paginator(bugs, 5)
    page = request.GET.get('page')
    bugs = paginator.get_page(page)

    return render(request, "get_bugs.html",
                  {'bugs': bugs, }
                  )


def get_bug_detail(request, pk):
    """ Show details about single bug based on single post id
    Show also all comments that are associated with single bug
    """
    comments = Comments.objects.filter(ticket=pk).order_by('created_date')
    paginator = Paginator(comments, 5)

    page = request.GET.get('page')
    comments = paginator.get_page(page)

    bug = get_object_or_404(Bugs, pk=pk)
    upvote = BugsUpvote.objects.filter(upvoted_bug=bug)

    if str(upvote) == '<QuerySet []>':
        upvoted = True
    else:
        upvoted = False

    bug = get_object_or_404(Bugs, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "get_bug_detail.html",
                  {'bug': bug,
                   'comments': comments,
                   'upvoted': upvoted}
                  )


@login_required
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
        title = 'Create or edit bug'
        return render(
            request, 'create_or_edit_bug.html',
            {'form': form, 'title': title}
        )


@login_required
def add_comment_bugs(request, pk=None):
    """Add comment to bugs"""
    bug = get_object_or_404(Bugs, pk=pk)
    c = CommentForm(request.POST, request.FILES)
    if c.is_valid():
        instance = c.save(commit=False)
        instance.username = request.user
        instance.ticket = bug
        c.save()
        return redirect(get_bug_detail, bug.pk)
    title = "Add comment"
    return render(request, "create_or_edit_bug.html", {'form': c, 'title': title})


@login_required
def upvote_bug(request, pk=None):
    """View is adding or taking one vote for each bug"""

    bug = get_object_or_404(Bugs, pk=pk)
    upvote = BugsUpvote.objects.filter(upvoted_bug=bug)

    if str(upvote) == '<QuerySet []>':
        try:
            u = get_object_or_404(
                BugsUpvote, upvoted_bug=bug, user=request.user)
        except BaseException:
            u = BugsUpvote()
        bug.upvotes += 1
        bug.save()
        u.upvoted_bug = bug
        u.user = request.user
        u.save()
    else:
        bug.upvotes -= 1
        bug.save()
        upvote.delete()

    return redirect(get_bug_detail, bug.pk)
