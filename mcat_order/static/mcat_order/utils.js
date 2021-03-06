function fire_request(container_id, url) { 
    var container = '#'+container_id;
	$(container).html('<br /><br /><br /><i class="fa fa-spinner fa-4x fa-spin"></i><br /><br /><br />');
	$.ajax({
		type: "GET",
		dataType: "html",
		url: url,
		success: function (content) {
			$(container).html(content);
			},
		error: function(xhr, textStatus, errorThrown) {
	        console.log("Error: "+errorThrown+xhr.status+xhr.responseText);
	        }
    	});
	}

function add_to_cart(url) {
	$('#cart').slideToggle();
	$('#cart_icon').removeClass('hidden');
	fire_request('cart',url);
	$('#order_btn').addClass('disabled');
	$('#order_btn').removeClass('btn-blue');
	$('#order_btn').addClass('btn-default');
	if (screen.width < 768) {
		window.location.hash = '#cart';
	}
}
function load_cart_actions(url) {
	fire_request('cart_actions',url);
}

function add_more_to_cart(url) {
	fire_request('cart',url);
}

function remove_from_cart(url) {
	fire_request('cart',url);
}

function toggle_cart() {
	$('#cart').slideToggle();
}

function clear_cart(url) {
	fire_request('cart',url);
	$('#cart_icon').hide();
	$('#cart').delay(1000).slideToggle();
}

function order(url) {
	$('#cart').load(url);
}

function accept_summary() {
	$('#delivery').show();
	window.location.hash = '#delivery';
	$('#summary_btn').toggleClass('btn-primary btn-default');
	$('#summary_btn').prepend('<i class="fa fa-check fa-lg text-success"></i>&nbsp;');
}

function accept_delivery() {
	$('#final_order').show();
	window.location.hash = '#final_order';
	$('#delivery_btn').toggleClass('btn-primary btn-default');
	$('#delivery_btn').prepend('<i class="fa fa-check fa-lg text-success"></i>&nbsp;');
}

