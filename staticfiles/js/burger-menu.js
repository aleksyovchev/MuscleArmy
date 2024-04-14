const burgerMenu = document.getElementById("burger-menu");
const overlay = document.querySelector(".overlay");

burgerMenu.addEventListener("click", () => {
    overlay.style.display = overlay.style.display === "block" ? "none" : "block";
});

document.addEventListener('DOMContentLoaded', function() {
    var shopNow = document.querySelector('.has-submenu');
    var submenuShop = document.querySelector('.submenu-shop');

    shopNow.addEventListener('click', function() {
        if (submenuShop.style.display === 'none' || submenuShop.style.display === '') {
            submenuShop.style.display = 'block';
        } else {
            submenuShop.style.display = 'none';
        }
    });
});
