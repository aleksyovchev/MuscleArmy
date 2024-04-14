const carouselTrack = document.querySelector('.carousel-track');
const slides = document.querySelectorAll('.carousel-slide');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let slideWidth = slides[0].clientWidth;
let currentSlide = 0;
let offsetPercentage = 0;

function showSlide() {
    // Процент на допълнително отместване
    const calculatedOffset = (slideWidth * offsetPercentage) / 100; // Изчисление на отместването в пиксели
    carouselTrack.style.transform = `translateX(-${slideWidth * currentSlide + calculatedOffset}px)`;
}

prevBtn.addEventListener('click', () => {
    if (currentSlide > 0) {
        currentSlide--;
        offsetPercentage = offsetPercentage - 3
        showSlide();
    }
});

nextBtn.addEventListener('click', () => {
    if (currentSlide < slides.length - 3) {
        currentSlide++;
        offsetPercentage = offsetPercentage + 3
        showSlide();
    }
});

showSlide();