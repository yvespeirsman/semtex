$( document ).ready(function() {
    $('.table > tbody > tr').click(function() {
	console.log(this.id);
	window.location = this.id;
    });
});