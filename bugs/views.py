from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Issues, IssueUpvote, Comments
from .forms import BugForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django_app.settings import host_images_link
from django.contrib.auth.models import User


def get_bugs(request):
    """ Show list of all bugs """

    bugs = Issues.objects.filter(
        published_date__lte=timezone.now(),
        issue_type='Bug'
    ).order_by('-published_date')
    paginator = Paginator(bugs, 5)
    page = request.GET.get('page')
    bugs = paginator.get_page(page)

    return render(request, "get_bugs.html",
                  {'bugs': bugs,
                   'simple_form': 1,
                   'issue_name': 'bugs', }
                  )


def get_features(request):
    """ Show list of all bugs """

    issue = Issues.objects.filter(
        published_date__lte=timezone.now(),
        issue_type='Feature'
    ).order_by('-published_date')

    paginator = Paginator(issue, 5)
    page = request.GET.get('page')
    issue = paginator.get_page(page)

    return render(request, "get_bugs.html",
                  {'bugs': issue,
                   'simple_form': 1,
                   'issue_name': 'features', }
                  )


def get_issue_detail(request, pk):
    """ Show details about single bug based on single post id
    Show also all comments that are associated with single bug
    """
    comments = Comments.objects.filter(ticket=pk).order_by('created_date')
    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    comments = paginator.get_page(page)

    issue = get_object_or_404(Issues, pk=pk)
    upvote = IssueUpvote.objects.filter(upvoted_bug=issue)
    upvoted = False

    try:
        user = User.objects.get(username=request.user)
    except BaseException:
        user = None

    for item in upvote:
        if str(item) == str(user):
            upvoted = True

    """Is issue actuall in cart? """
    id = pk
    cart = request.session.get('cart', {})
    in_cart = cart.get(id, 0)

    issue = get_object_or_404(Issues, pk=pk)
    issue.views += 1
    issue.save()
    return render(request, "get_bug_detail.html",
                  {'bug': issue,
                   'comments': comments,
                   'host_images_link': host_images_link,
                   'simple_form': 1,
                   'in_cart': in_cart,
                   'upvoted': upvoted,
                   'issue_name': issue.issue_type,
                   }
                  )


@login_required
def create_or_edit_issue(request, pk=None):
    """ View that allows to create or edit bug """
    bug = get_object_or_404(Issues, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.username = request.user
            bug.created_date = timezone.now()
            bug = form.save()
            return redirect(get_issue_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
        title = 'Create or edit issue'
        return render(
            request, 'create_or_edit_bug.html',
            {
                'form': form, 'title': title,
                "simple_form": 1,
            }
        )


@login_required
def add_comment_issue(request, pk=None):
    """Add comment to issues"""
    bug = get_object_or_404(Issues, pk=pk)
    c = CommentForm(request.POST, request.FILES)
    if c.is_valid():
        instance = c.save(commit=False)
        instance.username = request.user
        instance.ticket = bug
        c.save()
        return redirect(get_issue_detail, bug.pk)
    title = "Add comment"
    return render(request, "create_or_edit_bug.html",
                  {'form': c, 'title': title,
                    'issue_name': bug.issue_type,
                    "simple_form": 1,
                   })


@login_required
def upvote_issue(request, pk=None):
    """View is adding or taking one vote for each issue"""

    issue = get_object_or_404(Issues, pk=pk)
    upvote = IssueUpvote.objects.filter(upvoted_bug=issue)

    try:
        user = User.objects.get(username=request.user)
    except BaseException:
        user = None

    upvoted = False
    for item in upvote:
        if str(item) == str(user):
            upvoted = True

    if not upvoted:
        try:
            u = get_object_or_404(
                IssueUpvote, upvoted_bug=issue, user=request.user)
        except BaseException:
            u = IssueUpvote()
        issue.upvotes += 1
        issue.save()
        u.upvoted_bug = issue
        u.user = request.user
        u.save()
    else:
        issue.upvotes -= 1
        issue.save()
        upvote.delete()

    return redirect(get_issue_detail, issue.pk)
