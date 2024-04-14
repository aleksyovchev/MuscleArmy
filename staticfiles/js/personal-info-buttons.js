let lastClickedButtonId = 'personalButton';
const regex = /^[a-z]+/;

function changeTab(clickedButtonId){
    if (lastClickedButtonId !== clickedButtonId) {
        let buttonElement = document.getElementById(clickedButtonId);
        buttonElement.style.backgroundColor = "#5fc90d";
        buttonElement.style.color = "white";
    
        let infoIdToShow = clickedButtonId.match(regex) + "Info";
        let infoElementToShow = document.getElementById(infoIdToShow);
        infoElementToShow.style.display = "flex";
    
        let lastOpenedElement = document.getElementById(lastClickedButtonId);
        lastOpenedElement.style.backgroundColor = "#dbdbdb";
        lastOpenedElement.style.color = "#ffffff";
        
        let infoIdToHide = lastClickedButtonId.match(regex) + "Info";
        let infoElementToHide = document.getElementById(infoIdToHide);
        infoElementToHide.style.display = "none";
    
        lastClickedButtonId = clickedButtonId;    
    }

    event.preventDefault();
}
