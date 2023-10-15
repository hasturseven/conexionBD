function guardarDatos() {
      // Aquí puedes realizar la llamada a la base de datos y, si se guarda correctamente, mostrar el mensaje.
      // Por ahora, simplemente mostraremos el mensaje sin procesar los datos.
      let mensaje = document.getElementById("mensaje");
      mensaje.style.display = "block";
    }

    function limpiarFormulario() {
      // Agrega lógica para limpiar los campos del formulario.
        let n_documento = document.getElementById("n_documento").value("");
        let nombre = document.getElementById("nombre").value("");
        let apellido = document.getElementById("apellido").value("");
        let direccion = document.getElementById("direccion").value("");
        let correo = document.getElementById("correo").value("");
        let telefono = document.getElementById("telefono").value("");
      // Por ahora, simplemente ocultaremos el mensaje.
      let mensaje = document.getElementById("mensaje");
      mensaje.style.display = "none";
    }

    function mostrarInfo() {
    let infoText = document.getElementById("info-text");
    if (infoText.style.display === "none") {
      infoText.style.display = "block";
    } else {
      infoText.style.display = "none";
    }
  }
