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

// Sort Toggler
$('.sort__btn').on('click', function() {
    var sortBtn = $(this);
    var currentUrl = new URL(window.location);
    var sortKey = sortBtn.val();
    if(sortKey != "reset"){
        var sort = sortKey.split("_")[0];
        var direction = sortKey.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    }
    else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})
