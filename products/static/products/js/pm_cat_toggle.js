// Toggle product managment categories
$('.pm-cat-btn').on('click', function() {
    $('.pm-cat-btn').removeClass('pm-cat-btn-selected');
    $(this).addClass('pm-cat-btn-selected');

    var value = $(this).val();
    if (value == 'all-products') {
        $('.pm-cat').removeClass('d-none');
    }

    else if (value == 'no-cat') {
        $('.pm-cat').addClass('d-none');
        $('#' + value).removeClass('d-none');
    }

    else {
        $('.pm-cat').addClass('d-none');
        $('#' + value).removeClass('d-none');
    }
});