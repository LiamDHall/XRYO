// Swaps the main product image on selection 
$('.img-thumbnail').on('click', function() {
    $('.display-image').prop('src', this.src);
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

// Size Toggler
$('.size-btn').on('click', function() {
    console.log('i ran')
    $('.size-btn').removeClass('checked')
    $(this).addClass('checked')
    
    $(this).children('input').prop('checked', true)
})