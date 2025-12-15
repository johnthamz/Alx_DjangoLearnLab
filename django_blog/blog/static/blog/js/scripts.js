// Basic example script to demonstrate dynamic behavior
document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');

    // Example: highlight content div when page loads
    const contentDiv = document.querySelector('.content');
    if (contentDiv) {
        contentDiv.style.border = '1px solid #ccc';
        contentDiv.style.padding = '10px';
        contentDiv.style.backgroundColor = '#fff';
    }
});
