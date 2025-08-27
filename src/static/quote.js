document.addEventListener("DOMContentLoaded", () => {
    const refreshButton = document.querySelector(".refresh-btn");
    const quoteText = document.querySelector(".quote-text");

    if (quoteText) {
        // Reset the scroll position to the top on page load
        quoteText.scrollTop = 0;
    }

    if (refreshButton && quoteText) {
        refreshButton.addEventListener("click", () => {
            // Reset the scroll position of the quote text container
            quoteText.scrollTop = 0;
        });
    }
});
