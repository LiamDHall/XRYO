// Fix Filter to Site Header if Scrolled Pasted

$(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    var docHeight = $(document).height();
    var windowHeight = $(window).height()
    var footerHeight = $('.footer').height();

    targetPos = docHeight - windowHeight - footerHeight


    if(scroll > targetPos){
        $('.post-form-container').addClass('unfix');
    }
    else {
        $('.post-form-container').removeClass('unfix');
    }
});