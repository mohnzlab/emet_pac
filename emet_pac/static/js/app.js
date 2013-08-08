$(document).ready(function() {
	// Desactiva el campo de texto noMer
	$('#noMer').focusout(function() {
		$('#noMer').prop('disabled', true);
		$('#btnNuevoMer').tooltip('show');
		$('input[name=NoActa]').val($(this).val());
	});
	// Activa el campo de texto noMer
	$('#btnNuevoMer').click(function() {
		$('#noMer').removeAttr('disabled');
		$('#btnNuevoMer').tooltip('destroy');
		$('#noMer').val('');
		$('input[name=noMer]').val('');
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
	// Cambia el mensaje de error de un campo requerido
	$.validator.messages.required = 'Este campo es requerido.';
	// Funcion para validar formularios
	$('#formN').validate({
		rules: {
			noMer: {
				required: true
			},
			votosValidos: {
				required: true
			},
			votosNulos: {
				required: true
			},
			votosBlancos: {
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
						alert(data.msg);
						bloquearControles(form);	
					} else if (data.codigo == 2) {
						alert(data.msg);
					}
				}
			});
			return false;
		}
	});

	// Funcion para bloquear los controles del formulario actual

	function bloquearControles(form) {
		$(form).find('input[name=NoActa]').val('');
		$(form).find('input[name=VotosValidos]').val('');
		$(form).find('input[name=VotosNulos]').val('');
		$(form).find('input[name=VotosBlancos]').val('');
		$(form).find('fieldset').prop('disabled', true);
	}
});