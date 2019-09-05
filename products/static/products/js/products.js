
function update_qty_val(pk, val){
	var qty = $("#qty" + pk);
	qty.value = val;
	var btn = $("#qty-btn-" + pk);
	btn.show();
	console.log(qty.val());
}

function update_selling_val(pk, val){
	var selling = $("#selling" + pk);
	selling.value = val;
	var btn = $("#selling-btn-" + pk);
	btn.show();
	console.log(selling.value);
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