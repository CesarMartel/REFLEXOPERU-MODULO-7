document.addEventListener("DOMContentLoaded", function () {
    const inputBusqueda = document.getElementById("busqueda");
    const tabla = document.querySelector("table");

    if (!inputBusqueda || !tabla) return;

    inputBusqueda.addEventListener("input", function () {
        const texto = this.value.toLowerCase().trim();
        const filas = tabla.querySelectorAll("tbody tr");

        for (let fila of filas) {
            const celdas = fila.getElementsByTagName("td");
            let coincide = false;

            if (!isNaN(texto) && texto !== "") {
                coincide = celdas[0]?.textContent.toLowerCase().includes(texto);
            } else {
                for (let i = 1; i < celdas.length; i++) {
                    if (celdas[i].textContent.toLowerCase().includes(texto)) {
                        coincide = true;
                        break;
                    }
                }
            }

            fila.style.display = coincide ? "" : "none";
        }
    });
});
