//  Swiper JS
var mySwiper = new Swiper('.swiper-container', {

    // Optional Parameters
    slidesPerView: 4,
    slidesPerGroup: 4,
    
    spaceBetween: 10,
    direction: 'horizontal',
    loop: false,

    // Navigation Arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // Pagination
    pagination: {
        el: '.swiper-pagination',
    },
});