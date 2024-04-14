let lastOpenedSectionId = 'productSectionWear';
function changeImage(newImageSrc, circleId, sectionToShowId, gridToShowId) {


    // Промяна на изображенията на останалите елементи
    var allCircles = document.querySelectorAll('.black-circle img');
    allCircles.forEach(circle => {
        if (circle.id !== circleId) {
            circle.src = circle.dataset.defaultSrc;
        }
    });

    var image = document.querySelector('#' + circleId + ' img');
    if (image) {
        image.src = newImageSrc;
    }

    // Проверка и скриване на последната отворена секция
    if (lastOpenedSectionId !== null && lastOpenedSectionId !== sectionToShowId) {
        var lastSectionToHide = document.getElementById(lastOpenedSectionId);
        var lastGridToHide = document.getElementById('productSectionGrid' + lastOpenedSectionId.slice(14)); // Тук се използва срязване на идентификатора
        if (lastSectionToHide && lastGridToHide) {
            lastSectionToHide.style.display = 'none';
            lastGridToHide.style.display = 'none';
        }
    }

    // Показване на новата секция и грид
    var sectionToShow = document.getElementById(sectionToShowId);
    var gridToShow = document.getElementById(gridToShowId);
    if (sectionToShow && gridToShow) {
        sectionToShow.style.display = 'block';
        gridToShow.style.display = 'grid';
    }

    lastOpenedSectionId = sectionToShowId; // Запазване на текущата секция като последно отворена

    event.preventDefault(); // Предотвратява стандартното поведение на връзката
}
