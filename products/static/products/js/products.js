// Swaps the main product image on selection 
$('.img-thumbnail').on('click', function() {
    $('.display-image').prop('src', this.src);
});

// Fix Filter to Site Header if Scrolled Pasted
var filterBottom = $('.filters').offset().top

$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    var siteHeaderHeight = $('.site-header').height() 
    var filterTopPos = filterBottom - siteHeaderHeight
    if(scroll > filterTopPos){
        $('.filters').addClass('attach-to-header')
        $('.filters').css('top', `${siteHeaderHeight}px`)
    }
    else {
        $('.filters').removeClass('attach-to-header')
        $('.filters').removeAttr("style");
    }
});