/* =========================================================
   PROJET BOOTSTRAP - script.js
   Petites interactions JavaScript (sans framework)
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

  /* 1. Marquer le lien de navigation actif selon la page courante */
  const pageActuelle = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".navbar-nav .nav-link").forEach(function (lien) {
    lien.classList.remove("active");
    if (lien.getAttribute("href") === pageActuelle) {
      lien.classList.add("active");
    }
  });

  /* 2. Formulaire de contact : validation Bootstrap + spinner + alerte */
  const formulaireContact = document.getElementById("formulaireContact");
  if (formulaireContact) {
    formulaireContact.addEventListener("submit", function (event) {
      event.preventDefault();
      event.stopPropagation();

      if (!formulaireContact.checkValidity()) {
        formulaireContact.classList.add("was-validated");
        return;
      }

      const boutonEnvoyer = document.getElementById("boutonEnvoyer");
      const spinner = document.getElementById("spinnerEnvoi");
      const alerteSucces = document.getElementById("alerteSucces");

      // On affiche le spinner pendant 1.2s pour simuler un envoi
      spinner.classList.remove("d-none");
      boutonEnvoyer.disabled = true;

      setTimeout(function () {
        spinner.classList.add("d-none");
        boutonEnvoyer.disabled = false;
        alerteSucces.classList.remove("d-none");
        alerteSucces.classList.add("show");
        formulaireContact.reset();
        formulaireContact.classList.remove("was-validated");
      }, 1200);
    });
  }

  /* 3. Galerie : remplir la modale avec l'image cliquée */
  const modaleGalerie = document.getElementById("modaleGalerie");
  if (modaleGalerie) {
    modaleGalerie.addEventListener("show.bs.modal", function (event) {
      const declencheur = event.relatedTarget;
      const src = declencheur.getAttribute("data-src");
      const titre = declencheur.getAttribute("data-titre");
      modaleGalerie.querySelector("#imageModale").setAttribute("src", src);
      modaleGalerie.querySelector(".modal-title").textContent = titre;
    });
  }

});
