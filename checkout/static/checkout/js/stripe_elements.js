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
    var displayErrors = document.getElementsByClassName('form-errors');
    if (event.error) {
        var errorMessage = `
            <span class="ml-2" role="alert"><i class="fas fa-times"></i></span>
            <span>${event.error.message}</span>
        `;
        $(errorContainer).html(errorMessage);
        $(displayErrors).html(errorMessage);
        $('#card-element').removeClass('mb-5');
    }
    
    else {
        errorContainer.textContent = '';
        $(displayErrors).html('');
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
    // Disable card input and submit button
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // Add loading overlay
    $('#checkout-form').fadeToggle(100);
    $('#payment-overlay').fadeToggle(100);

    // Capture form data that can't be put into the payment_intent
    // Check if users chceked save info (True or False)
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Get csrf_token from the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var cache_url = '/checkout/cache_checkout_data/';

    // Post the date to cache url/view and then run form submission if valid
    $.post(cache_url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            // Insert error message to error div 
            if (result.error) {
                var displayErrors = document.getElementsByClassName('form-errors');
                var errorMessaage = `
                    <span role="alert"><i class="fas fa-times"></i></span>
                    <span>${result.error.message}</span>`;
                $(displayErrors).html(errorMessaage);

                // Remove loading overlay
                $('#checkout-form').fadeToggle(100);
                $('#payment-overlay').fadeToggle(100);

                // Re-active card input and submit button
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } 
            
            else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // On POST failure reload page
        // The error will be in django messages
        location.reload();
    });
});