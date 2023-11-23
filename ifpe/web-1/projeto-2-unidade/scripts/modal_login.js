
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