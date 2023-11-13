/* let locais = [".jamaica", ".bahamas", ".butao"];
let cont = 0;

function mostrar() {
    for (let i = 0; i < locais.length; i++) {
        let element = document.querySelector(locais[i]);
        element.style.display = i === cont ? "block" : "none";
    }

    cont = (cont + 1) % locais.length;

    setTimeout(mostrar, 10000);
}
mostrar();
 */

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  slideIndex++;
  
  if (slideIndex > slides.length) { 
    slideIndex = 1 
  }
  
  slides[slideIndex - 1].style.display = "block";  
  setTimeout(showSlides, 2000); // Mude 2000 para a quantidade desejada de milissegundos entre os slides
}
