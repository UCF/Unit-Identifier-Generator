$(document).ready(function(){
	$('#previewlink_uid').click(function() {
		// Remove active class from current active preview div and fade out:
		$('.preview_active').fadeOut().removeClass('preview_active');
		// Fade in new active preview div
		$('#uid_img').fadeIn().addClass('preview_active');
	})
	$('#previewlink_muid').click(function() {
		$('.preview_active').fadeOut().removeClass('preview_active');
		$('#muid_img').fadeIn().addClass('preview_active');
	})
	$('#previewlink_vuid').click(function() {
		$('.preview_active').fadeOut().removeClass('preview_active');
		$('#vuid_img').fadeIn().addClass('preview_active');
	})
})