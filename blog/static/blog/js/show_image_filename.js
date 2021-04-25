// Show selected image filename
$('#image-new').change(function() {
    var file = $('#image-new')[0].files[0];
    $('#filename').text(`On save, image will be set to: ${file.name}`);
});