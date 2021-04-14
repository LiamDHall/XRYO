/*
    Stripe Element 
    Soruce: https://stripe.com/docs/payments/accept-a-payment-synchronously
    Apdated style to match the rest of the form it will fit
    into.
*/
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: 'black',
        fontFamily: '"Montserrat", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: 'silver'
        }
    },
    invalid: {
        color: 'red',
        iconColor: 'red'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Validation Error Handler when the Card Element Input changes
card.on('change', function (event) {
    var errorContainer = document.getElementById('card-errors');
    if (event.error) {
        var errorMessage = `
            <span class="ml-2" role="alert"><i class="fas fa-times"></i></span>
            <span>${event.error.message}</span>
        `;
        $(errorContainer).html(errorMessage);
        $('#card-element').removeClass('mb-5');
    }
    
    else {
        errorContainer.textContent = '';
        $('#card-element').addClass('mb-5');
    }
});

/* 
    Form Submit Handler
    Source: https://stripe.com/docs/payments/accept-a-payment-synchronously
    Adpated for my needs.
*/
var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
    
    // Stops the form submitting
    ev.preventDefault();

    // Prevent multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorContainer = document.getElementById('card-errors');
            var errorMessaage = `
                <span role="alert"><i class="fas fa-times"></i></span>
                <span>${result.error.message}</span>`;
            $(errorContainer).html(errorMessaage);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});