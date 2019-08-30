var update_inventory = $("#update-inventory");
var inventory = $("#qty");

function update_qty_val(val){
	inventory.value = val;
}

update_inventory.on('click', function(){
	var url = '/products/ajax/update-inventory/' + this.value + '/' + inventory.value + '/';
	$.ajax({
		url: url,
		statusCode: {
			404: function(){
				alert('Could not get URL: ' + this.url);
			},
		},
		success: function(data){
			alert(data);
			inventory.value = data;
		},
		fail : function(data){
			alert(data);
		},
	});
})