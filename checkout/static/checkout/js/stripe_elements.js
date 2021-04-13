/*
    Stripe Element 
    Soruce: https://stripe.com/docs/payments/accept-a-payment
    Apdated style to match the rest of the form it will fit
    into.
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
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