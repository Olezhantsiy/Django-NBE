const swiper = new Swiper(".swiper", {
    pagination: {
      el: ".swiper-pagination",
    },
    autoplay: {
        delay: 3000,
        disableOnInteraction: false
      },
      effect: "fade",
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
  });