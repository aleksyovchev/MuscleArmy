const image = document.getElementById('productLikeButton');
let originalSrc = 'static/images/unfilled-heart.svg';
let alternateSrc = 'static/images/filled-heart.svg';

image.addEventListener('click', function () {
    let currentSrc = image.getAttribute('src');
    let filename = currentSrc.split('/').pop();
    
    if (filename === originalSrc.split('/').pop()) {
        image.setAttribute('src', alternateSrc);
    } else if (filename === alternateSrc.split('/').pop()) {
        image.setAttribute('src', originalSrc);
    }
});