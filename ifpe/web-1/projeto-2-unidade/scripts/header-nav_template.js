
document.addEventListener('DOMContentLoaded', function () {
    loadHeaderAndNav();
});

function loadHeaderAndNav() {
    fetch('html_templates/header-nav.html')
        .then(response => response.text())
        .then(html => {
        
            var container = document.getElementById('headerAndNavContainer');
            if (container) {
                container.innerHTML = html;
                document.getElementById('login_butao').addEventListener('click', function () {
                    document.getElementById('loginModal').style.display = 'block';
                  });
                  function fecharModal() {
                    document.getElementById('loginModal').style.display = 'none';
                  }
                  
                  window.onclick = function (event) {
                    if (event.target == document.getElementById('loginModal')) {
                      document.getElementById('loginModal').style.display = 'none';
                    }
                  };
            }
        })
        .catch(error => console.error('Error loading header and navigation:', error));
}
loginButton.addEventListener('click', function () {
    abrirModal();
});
