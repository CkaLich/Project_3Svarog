document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // LANGUAGE SWITCH
    // =========================
    const langBtn = document.getElementById("langBtn");
    const dropdown = document.getElementById("langDropdown");
    const langForm = document.getElementById("langForm");
    const languageInput = document.getElementById("languageInput");

    if (langBtn && dropdown && langForm && languageInput) {

        // Öffnen / schließen
        langBtn.addEventListener("click", function () {
            dropdown.classList.toggle("hidden");
        });

        // Sprache wählen
        dropdown.querySelectorAll("[data-lang]").forEach(item => {

            item.addEventListener("click", function () {

                languageInput.value = this.dataset.lang;
                langForm.submit();
            });
        });

        // Klick ausserhalb
        document.addEventListener("click", function (e) {

            if (
                !langBtn.contains(e.target) &&
                !dropdown.contains(e.target)
            ) {
                dropdown.classList.add("hidden");
            }
        });
    }


    // =========================
    // MENU
    // =========================
    const menuBtn = document.getElementById("menuBtn");
    const mainMenu = document.getElementById("mainMenu");

    if (menuBtn && mainMenu) {

        // Öffnen / schließen
        menuBtn.addEventListener("click", function () {
            mainMenu.classList.toggle("hidden");
        });

        // Klick ausserhalb
        document.addEventListener("click", function (e) {

            if (
                !menuBtn.contains(e.target) &&
                !mainMenu.contains(e.target)
            ) {
                mainMenu.classList.add("hidden");
            }
        });
    }

});
