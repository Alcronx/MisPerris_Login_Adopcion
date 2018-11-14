function validar() {
    var nombre, email, run, fecha, telefono;
    nombre = document.getElementById("nombre").value;
    email = document.getElementById("email").value;
    run = document.getElementById("run").value;
    fecha = document.getElementById("fecha").value;
    telefono = document.getElementById("telefono").value;
    regiones = document.getElementById("regiones").value;
    comunas = document.getElementById("comunas").value;
    tipocasa = document.getElementById("TipoCasa").value;

    if (nombre === "") {
        alert("Ingrese el nombre");
        return false;
    }
    if (email === "") {
        alert("Ingrese el Email");
        return false;
    }
    if (run === "") {
        alert("Ingrese el Rut");
        return false;
    }
    if (run.length > 10 || run.length < 8) {
        alert("Ingrese un rut valido");
        return false;
    }
    if (fecha === "") {
        alert("Ingrese la fecha");
        return false;
    }
    if (telefono.length < 9 || telefono.length > 9) {
        alert("Ingrese un numero de telefono valido, anteponga un 9 al numero.");
        return false;
    }
    if (telefono === "") {
        alert("Ingrese el telefono");
        return false;
    }
}