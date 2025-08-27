document.addEventListener("DOMContentLoaded", () => {
    const refreshButton = document.querySelector(".refresh-btn");
    const quoteText = document.querySelector(".quote-text");

    if (refreshButton && quoteText) {
        refreshButton.addEventListener("click", () => {
            // Reset the scroll position of the quote text container
            quoteText.scrollTop = 0;
        });
    }
});
