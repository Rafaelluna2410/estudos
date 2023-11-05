let slideIndex = 0; 
let interval; 


showSlides(); 

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");

  if (n !== undefined) {
 
    slideIndex = n;
    clearInterval(interval); 
  }

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  slideIndex++;

  if (slideIndex > slides.length) {
    slideIndex = 1;
    clearInterval(interval);
  }

  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";

  interval = setInterval(function () {
    plusSlides(0);
  }, 5000);
}
