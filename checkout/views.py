from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm
from django.conf import settings
from bugs.models import Issues, IssueUpvote
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """Renders the checkout page. If post, payment is taken or
       error is returned  """

    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                total += quantity * 10
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")

                return redirect(reverse('cart_success'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()

    return render(request, "checkout.html", {
        "publishable": settings.STRIPE_PUBLISHABLE,
        "payment_form": payment_form,
        "simple_form": 1,
    })


@login_required
def cart_success(request):
    """Upvote all items in cart and clear cart.
    Even if the item was upvoted before from same user
    - one point still will be added.
    """

    cart = request.session.get('cart', {})
    upvote_list = []

    for id, quantity in cart.items():
        feature = get_object_or_404(Issues, pk=id)
        upvote_list.append(id)

    for id in upvote_list:
        feature_name = get_object_or_404(
            Issues, id=id)
        try:
            upvote = get_object_or_404(
                IssueUpvote, user=request.user,
                upvoted_feature=feature_name
            )
        except BaseException:
            upvote = IssueUpvote()

        upvote.user = request.user
        upvote.upvoted_bug = feature_name
        feature_name.upvotes += 1
        feature_name.save()
        upvote.save()

    request.session['cart'] = {}
    return redirect(reverse('get_features'))
