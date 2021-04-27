// Set the correct colour of country input
var selectedCountry = $('#id_default_country').val();

// Onload if no country selected set colour of text to silver
if(!selectedCountry) {
    $('#id_default_country').css('color', 'silver');
}

// Listen for when country input's selection changes
$('#id_default_country').change(function() {
    // Get the value of selected
    selectedCountry = $(this).val();

    /* 
        Determine what colour to turn the text based on if
        a country is selected or not
    */
    if(!selectedCountry) {
        $(this).css('color', 'silver');
    
    }

    else {
        $(this).css('color', 'black');
    }
});