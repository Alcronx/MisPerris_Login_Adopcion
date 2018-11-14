function ValidarResc() {
    var nombre,raza,descripcion;
    nombre = document.getElementById("nombreR").value;
    raza = document.getElementById("raza").value;
    descripcion = document.getElementById("descripcion").value;
    var fileInput = document.getElementById('ImagenR');
    var filePath = fileInput.value;


    if (nombre === "") {
        alert("Ingrese el nombre Señooooor");
        return false;
    }
    if (raza === "") {
        alert("Ingrese Raza del Animal Señooor");
        return false;
    }

    if (descripcion === "") {
        alert("Ingrese descripcion del Animal Señooooooor");
        return false;
    }
    if (filePath === '') {
        alert("Debe Ingresar Imagen");
        return false;
    }

}