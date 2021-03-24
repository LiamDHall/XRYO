// Swaps the main product image on selection 
$('.img-thumbnail').on('click', function() {
    $('.display-image').prop('src', this.src);
});