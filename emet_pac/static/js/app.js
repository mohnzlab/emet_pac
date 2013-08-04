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
			//alert($('input[name=idPresidente]').val());
			/*$(form).ajaxSubmit({ // create an AJAX call...
						data: $(form).serialize(), // get the form data
						type: $(form).attr('method'), // GET or POST
						url: $(form).attr('action'), // the file to call
						success: function(response) { // on success..
							//$('#mensaje').html(response); // update the DIV
							aler('Correcto');
							bloquearControles(form);
                }
            });*/
			//return false;
			 $.ajax({ // create an AJAX call...
                data: $(form).serialize(), // get the form data
                type: $(form).attr('method'), // GET or POST
                url: $(form).attr('action'), // the file to call
                success: function(response) { // on success..
                    alert('Correcto');
					bloquearControles(form);
                }
            });
			/*form.preventDefault();

			$.post($(form).attr('method'), $(form).serialize(), function(data) {
				if (data.codigo == 1) {
					alert(data.msg);
					document.location = $(form).attr('action');
				} else if (data.codigo == 2) {
					alert(data.msg);
				}
			}, 'json');*/
		}

	});

	// Funcion para bloquear los controles del formulario actual

	function bloquearControles(form) {
		$(form).find("fieldset").prop('disabled', true);
	}
});