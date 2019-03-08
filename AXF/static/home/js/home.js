$(function () {
    $('.home').width(innerWidth)
    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false
    });
    var mustbuySwiper = new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 5,
        freeMode: true

    })
})
