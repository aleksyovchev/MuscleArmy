document.addEventListener('DOMContentLoaded', function () {
    const profileContainer = document.getElementById('profileContainer');
    const uploadOverlay = document.getElementById('uploadOverlay');
    const fileInput = document.getElementById('fileInput');
    const profilePicture = document.getElementById('profilePicture');

    profileContainer.addEventListener('mouseenter', function () {
        uploadOverlay.style.opacity = '1';
    });

    profileContainer.addEventListener('mouseleave', function () {
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
