let locais = [".jamaica", ".bahamas", ".butao"];

let jamaica = document.querySelector(locais[0]);
let bahamas = document.querySelector(locais[1]);
let butao = document.querySelector(locais[2]);

jamaica.style.display = "none";
bahamas.style.display = "none";
butao.style.display = "none";

function mostrar() {
    for (let i = 0; i < locais.length; i++) {
        let element = document.querySelector(locais[i]);
        element.style.display = "block";
    }
}

setTimeout(mostrar, 5000);
