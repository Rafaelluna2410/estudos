
document.addEventListener('DOMContentLoaded', function () {
    loadFooter();
});
function loadFooter() {

    fetch('html_templates/footer.html')
        .then(response => response.text())
        .then(html => {
            var container = document.getElementById('footerContainer');
            if (container) {
                container.innerHTML = html;
            }
        })
        .catch(error => console.error('Error loading footer:', error));
}
