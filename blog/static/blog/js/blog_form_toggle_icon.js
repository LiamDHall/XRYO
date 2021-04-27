// Toggle the words in blog form toggle button
$('#blog-toggle').on('click', function() {
    text = $(this).text();
    if (text != 'Cancel') {
        text = $(this).text('Cancel');
    }

    else {
        text = $(this).text('Post To Blog');
    }
});