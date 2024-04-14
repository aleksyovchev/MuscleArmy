document.addEventListener('DOMContentLoaded', function () {
    const navbarLinks = document.querySelectorAll('.sub-nav a');

    navbarLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            const navbarHeight = document.querySelector('.navbar').offsetHeight;

            if (targetSection) {
                const offsetPosition = targetSection.offsetTop - navbarHeight;
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});
