
function update_object_val(pk, val, in_val, el){
	var element = $("#"+el+pk);
	var btn = $("#"+el+"-btn-" + pk);
	element.value = val;
	if(val == in_val){
		btn.addClass('hidden-button');
	}else{ 
		btn.removeClass('hidden-button');
	};
	console.log(element.val());
}

function update_qty(pk){
	var qty = $("#qty" + pk);
	var val = qty.val();
	var url = '/products/ajax/update-inventory/' + pk + '/' + val + '/';
	$.ajax({
		url: url,
		statusCode: {
			404: function(){
				alert('Could not get URL: ' + this.url);
			},
		},
		success: function(data){
			alert(data);
			var btn = $("#qty-btn-" + pk);
			btn.hide();
		},
		fail : function(data){
			alert(data);
		},
	});
}

function update_selling(pk){
	var selling = $("#selling" + pk);
	var val = selling.val();
	console.log(val);
	var url = '/products/ajax/update-selling/' + pk + '/' + val + '/';
	$.ajax({
		url: url,
		statusCode: {
			404: function(){
				alert('Could not get URL: ' + this.url);
			},
		},
		success: function(data){
			alert(data);
			var btn = $("#selling-btn-" + pk);
			btn.hide();
		},
		fail : function(data){
			alert(data);
		},
	});
}