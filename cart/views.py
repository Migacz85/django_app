from django.shortcuts import render, redirect, reverse, get_object_or_404
from bugs.views import get_issue_detail
from bugs.models import Issues
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    """  A view that renders the cart contents page """
    return render(request, "cart.html", {"simple_form": 1})


def add_to_cart(request, id):
    """ Add a feature ticket to the cart"""
    quantity = int(request.POST.get('quantity'))

    # issues = get_object_or_404(Issues, id=id)
    # issues.views -= 1
    # issues.save()

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    cart[id] = quantity
    request.session['cart'] = cart
    return redirect(get_issue_detail, id)


def remove_ticket(request, id):
    """Removes a ticket from the cart page"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_ticket_in_issue(request, id):
    """Removes a ticket from the cart page"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(get_issue_detail, id)
