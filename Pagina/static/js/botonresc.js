$(document).ready(function () {
    $("#ImagenR").on("change", function (e) {

        var files = $(this)[0].files;
        var fileInput = document.getElementById('ImagenR');
        var filePath = fileInput.value;
        var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;

        if (files.length == 1 && allowedExtensions.exec(filePath)){
            var fileName = e.target.value.split('\\').pop();
            $("#Cambiotexto").text(fileName);
        }

        if (!allowedExtensions.exec(filePath)) {
            alert('Porfavor solo suba archivos con la extencion .jpeg/.jpg/.png/');
            fileInput.value = '';
        }
    });
});









