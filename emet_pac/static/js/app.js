
$(document).ready(function() {
	// Cambiar el color del borde de la caja para ingreso de votos de diputados
	$(".cajaVotosDip").on('click', function() {
		$(this).css('border','1px solid green');
	});
	// Inicio de Sesion de Usuarios
	var formLogin = $("#frmLogin");
	$(formLogin).on('submit',function(){
		ocultarMensajes();
			$.ajax({
					data: $(formLogin).serialize(),
					type: $(formLogin).attr('method'),
					dataType: "json",
					url: $(formLogin).attr('action'),
					success: function(data) {
						if (data.codigo == 3) {
							mostrarMensaje(formLogin, "<span class='alertContenido'><strong>Alto!</strong> El usuario o contraseña ingresado no es valido.</span>", "alert-danger");
						} else if (data.codigo == 2) {
							mostrarMensaje(formLogin, "<span class='alertContenido'><strong>Alto!</strong> El usuario ingresado no esta activado.</span>", "alert-danger");
						} else if (data.codigo == 1) {
							window.location = '/main/';
						}
					}
				});
				return false;
	});
	// Desactiva el campo de texto noMer
	$('#noMer').focusout(function() {
		$('#noMer').prop('disabled', true);
		$('#btnNuevoMer').tooltip('show');
		$('input[name=NoActa]').val($(this).val());
	});
	// Activa el campo de texto noMer
	$('#btnNuevoMer').click(function() {
		$('#noMer').removeAttr('disabled');
		$('#noMer').focus();
		$('#btnNuevoMer').tooltip('destroy');
		$('#noMer').val('');
		$('input[name=noMer]').val('');
		ocultarMensajes();
		desbloquearControles(true);
	});

	// Funcion para aceptar solo numeros en input boxes
	$(".numero").keydown(function(event) {
		// Permitir: backspace, delete, tab, escape, y enter
		if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 || event.keyCode == 13 ||
			// Permitir: Ctrl+A
			(event.keyCode == 65 && event.ctrlKey === true) ||
			// Permitir: home, end, left, right
			(event.keyCode >= 35 && event.keyCode <= 39)) {
			// No hacer nada
			return;
		} else {
			//Asegurar que se ingresa un numero y detener keypress
			if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
				event.preventDefault();
			}
		}
	});
	//Obtener Id del form submited
	$("button[Id]").closest("button").on('click', function() {
		var id = "#" + $(this).closest("form").attr('id');

		$(id).validate({
			rules: {
				NoActa: {
					required: true
				},
				VotosValidos: {
					required: true
				},
				VotosNulos: {
					required: true
				},
				VotosBlancos: {
					required: true
				}
			},
			highlight: function(element) {
				$(element).closest('.form-group').removeClass('has-success').addClass('has-error');
			},
			success: function(element) {
				$(element).closest('.form-group').removeClass('has-error').addClass('has-success');
			},
			submitHandler: function(form) {
				$.ajax({
					data: $(form).serialize(),
					type: $(form).attr('method'),
					dataType: "json",
					url: $(form).attr('action'),
					success: function(data) {
						if (data.codigo == 1) {
							bloquearControles(form, false);
							mostrarMensaje(form, "<span class='alertContenido'><strong>Genial!</strong> El registro se guardo correctamente.</span>", "alert-success");
						} else if (data.codigo == 2) {
							mostrarMensaje(form, "<span class='alertContenido'><strong>Oh no :( !</strong> Ocurrio un error al guardar el registro, por favor comunicate con el administrador.</span>", "alert-danger");
						} else if(data.codigo == 3) {
							mostrarMensaje(form, "<span class='alertContenido'><strong>Alto!</strong> ERROR, Acta duplicada.</span>", "alert-danger");
						}
					}
				});
				return false;
			}
		});
	});


	// Cambia el mensaje de error de un campo requerido
	$.validator.messages.required = 'Este campo es requerido.';

	// Funcion para bloquear los controles del formulario actual

	function bloquearControles(form, isClean) {
		$(form).find('fieldset').prop('disabled', true);
		if (isClean) {
			$(form).find('input[name=NoActa]').val('');
			$(form).find('input[name=VotosValidos]').val('');
			$(form).find('input[name=VotosNulos]').val('');
			$(form).find('input[name=VotosBlancos]').val('');
		};
	}
	// Funcion para habilitar edicion en controles de ingreso de formulario
	function desbloquearControles(isClean) {
		var form = $('form');
		$(form).find('fieldset').prop('disabled',false);
		$(form).find('.form-group').removeClass('has-success');
		$(form).find('.form-group').removeClass('has-error');
		if (isClean) {
			$(form).find('input[name=NoActa]').val('');
			$(form).find('input[name=VotosValidos]').val('');
			$(form).find('input[name=VotosNulos]').val('');
			$(form).find('input[name=VotosBlancos]').val('');
		};
	}
	// Funcion para mostrar mensajes
	function mostrarMensaje(form, mensaje, tipo) {
		$(form).find(".alert").addClass(tipo).append(mensaje);
		$(form).find(".alert").slideDown(200);
	}

	// Funcion para ocultar mensajes
	function ocultarMensajes() {
		$(".alert").removeClass("alert-danger");
		$(".alertContenido").remove();
		$(".alert").slideUp(200);
	}



});