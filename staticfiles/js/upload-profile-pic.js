document.addEventListener('DOMContentLoaded', function () {
    const imageUpload = document.getElementById('imageUpload');
    const uploadOverlay = document.getElementById('uploadOverlay');
    const fileInput = document.getElementById('fileInput');
    const profilePicture = document.getElementById('profilePicture');

    imageUpload.addEventListener('mouseenter', function () {
        uploadOverlay.style.opacity = '1';
    });

    imageUpload.addEventListener('mouseleave', function () {
        uploadOverlay.style.opacity = '0';
    });

    fileInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                profilePicture.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
