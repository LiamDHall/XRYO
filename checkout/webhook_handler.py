from django.http import HttpResponse


class StripeWH_Handler:
    """Handles webhooks recieved from Stripe
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles all generic or unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handles the webhook: payment_intent.succeeded from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handles the webhook: payment_intent.payment_failed from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
