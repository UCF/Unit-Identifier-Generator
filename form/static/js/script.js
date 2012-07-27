$(document).ready(function(){

	/* Default values for preview dimensions for hidden fields */
	var uid_span_w = 0,
		uid_span_h = 0,
		uid_fontsize = 13,
		muid_span_w = 0,
		muid_span_h = 0,
		muid_fontsize = 16,
		vuid_span_w = 0,
		vuid_span_h = 0,
		vuid_fontsize = 0;

	/* Set UID as default preview in toggle buttons */
	$('#previewlink_uid').button('toggle');	
	
	/* Define functions that adjust the MUID and VUID previews: */
	
	var muid_adjust = function() {
		var muid_div = $('#muid_text'),
			muid_span = $('#muid_text span'),
			muid_text = muid_span.text(),
			muid_words = muid_text.split(' '),
			muid_wordcount_mid = Math.round(muid_words.length / 2);
		// 2 words or less: force baseline down
		if (muid_words.length <= 2) {
			muid_div.css('line-height', '44px');
		}
		else {
			muid_div.css('line-height', '15.25px');
			// 3 or more words: Force a line break:
			muid_words.splice(muid_wordcount_mid,0,'<br/>');
			muid_span.html(muid_words.join(' '));
		}
	}
	
	var vuid_adjust = function() {
		var vuid_div = $('#vuid_text');
		vuid_div.textfill({ minFontPixels: 20, maxFontPixels: 36 });
		
		var	vuid_span = $('#vuid_text span');
		vuid_fontsize = parseInt(vuid_span.css('font-size').slice(0,-2));
			
		// If the font size has changed, change the line height: 
		vuid_span.css('line-height', vuid_fontsize+'px');
	}
	
	
	/* Define updates to hidden form field values */
	
	var hidden_field_update = function() {	
		
		/* The below if/else statements are necessary to properly get
		   the <span> dimensions if that parent <div> is hidden.
		*/
		
		// UID preview: 
		if (($('#uid_img').hasClass('preview_active')) == false) {
			$('#uid_img').show();
			uid_span_w = $('#uid_img span').width();
			uid_span_h = $('#uid_img span').height();
			$('#uid_img').hide();
		}
		else {
			uid_span_w = $('#uid_img span').width();
			uid_span_h = $('#uid_img span').height();
		}
		// MUID preview:
		if (($('#muid_img').hasClass('preview_active')) == false) {
			$('#muid_img').show();
			muid_span_w = $('#muid_img span').width();
			muid_span_h = $('#muid_img span').height();
			$('#muid_img').hide();
		}
		else {
			muid_span_w = $('#muid_img span').width();
			muid_span_h = $('#muid_img span').height();
		}
		// VUID preview:
		if (($('#vuid_img').hasClass('preview_active')) == false) {
			$('#vuid_img').show();
			vuid_span_w = $('#vuid_img span').width();
			vuid_span_h = $('#vuid_img span').height();
			vuid_fontsize = $('#vuid_text span').css('font-size').slice(0,-2);
			$('#vuid_img').hide();
		}
		else {
			vuid_span_w = $('#vuid_img span').width();
			vuid_span_h = $('#vuid_img span').height();
			vuid_fontsize = $('#vuid_text span').css('font-size').slice(0,-2);
		}
		
		
		/* Each value is determined by what is assumed to be
		   the value of the full-size raster output. (2000 wide)
		   These values need to be updated should the dimensions
		   of the generated logos ever change.
		*/
		
		var full_size_width = 2000,
			preview_width = 260,
			muid_preview_width = 450,
			span_upscale_ratio = full_size_width / preview_width,
			muid_span_upscale_ratio = full_size_width / muid_preview_width/*,
			uid_font_ratio = 5,
			muid_font_ratio = 6.25,
			vuid_font_ratio = 5.55*/;		
		
		$('#uid_fontsize').val(Math.round(uid_fontsize * span_upscale_ratio));
		$('#muid_fontsize').val(Math.round(muid_fontsize * muid_span_upscale_ratio));
		$('#vuid_fontsize').val(Math.round(vuid_fontsize * span_upscale_ratio));
		
		$('#uid_span_w').val(Math.round(uid_span_w * span_upscale_ratio));
		$('#muid_span_w').val(Math.round(muid_span_w * muid_span_upscale_ratio));
		$('#vuid_span_w').val(Math.round(vuid_span_w * span_upscale_ratio));
		
		$('#uid_span_h').val(Math.round(uid_span_h * span_upscale_ratio));
		$('#muid_span_h').val(Math.round(muid_span_h * muid_span_upscale_ratio));
		$('#vuid_span_h').val(Math.round(vuid_span_h * span_upscale_ratio));
		
		if ($('#muid_text span br').length > 0) {
			$('#muid_linebreak').val('y');
		}
		else {
			$('#muid_linebreak').val('n');
		}
	}
	
	
	/* Set default dept. name */
	
	if (!($('#id_unit_name').val())) {
		$('.textfill span').text('Unit Name Here');
		$('#id_unit_name').val('Unit Name Here');
	}
	else {
		$('.textfill span').text($('#id_unit_name').val());
	}
		
	
	/* Textfill + adjustments onload */
	
	$('#uid_text').textfill({ minFontPixels: 13, maxFontPixels: 13 });
	muid_adjust();
	vuid_adjust();
	hidden_field_update();
	

	/* Switch in/out logo previews */
	
	$('#previewlink_uid').click(function() {
		// Remove active class from current active preview div and fade out:
		$('.preview_active').hide().removeClass('preview_active');
		// Fade in new active preview div
		$('#uid_img').fadeIn().addClass('preview_active');
	})
	$('#previewlink_muid').click(function() {
		$('.preview_active').hide().removeClass('preview_active');
		$('#muid_img').fadeIn().addClass('preview_active');
		muid_adjust();
	})
	$('#previewlink_vuid').click(function() {
		$('.preview_active').hide().removeClass('preview_active');
		$('#vuid_img').fadeIn().addClass('preview_active');
		vuid_adjust();
	})


	/* Textfill + adjustments on keyup */
	
    $('#id_unit_name').keyup(function() {
    	$('.textfill span').html(this.value);
    	$('#uid_text').textfill({ minFontPixels: 13, maxFontPixels: 13 });
		muid_adjust();
		vuid_adjust();
		hidden_field_update();
    });


	/* Form on submit popup: */
	
	$('#form_submit').click(function(){
		setTimeout(function() {
			$('#submit_working').modal('show');
		}, 700)
	})
	
})