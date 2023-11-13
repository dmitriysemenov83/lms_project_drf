import stripe

from tutorial.models import Payment

stripe.api_key = " "


def get_session(serializer: Payment):
    course_title = serializer.course.title
    product = stripe.Product.create(name=course_title)
    price = stripe.Price.create(
        unit_amount=serializer.amount * 100,
        currency="rub",
        product=product.id,
    )
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
        # custom_email=serializer.user.email,
    )
    # send_payment_link_to_mail(session.url, serializer.user.email)
    return session

