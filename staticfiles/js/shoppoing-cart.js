const shoppingCart = document.getElementById("shoppingCart");
const overlayShoppingCart = document.querySelector(".overlay-shopping-cart");

shoppingCart.addEventListener("click", () => {
    overlayShoppingCart.style.display = overlayShoppingCart.style.display === "block" ? "none" : "block";
});


