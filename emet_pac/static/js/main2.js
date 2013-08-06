$(function(){
	$('#formN').submit(function(e){
		e.preventDefault();

		$.post('ActaPresidente/', $(this).serialize(), function(data){
			if (data.codigo == 1)
			{
				alert(data.msg);
			} else if (data.codigo == 2) {
				alert(data.msg);
			}
		}, 'json');
	});
});