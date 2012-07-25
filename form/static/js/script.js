$(document).ready(function(){

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
		
		var	vuid_span = $('#vuid_text span'),
			vuid_fontsize = parseInt(vuid_span.css('font-size').slice(0,-2));
			
		// If the font size has changed, change the line height: 
		vuid_span.css('line-height', vuid_fontsize+'px');
	}
	
	
	/* Define updates to hidden form field values */
	
	var hidden_field_update = function() {
		
		$('#uid_fontsize').val(Math.round($('#uid_text span').css('font-size').slice(0,-2)));
		$('#muid_fontsize').val(Math.round($('#muid_text').css('font-size').slice(0,-2)));
		$('#vuid_fontsize').val(Math.round($('#vuid_text span').css('font-size').slice(0,-2)));
		
		$('#uid_span_w').val($('#uid_text span').actual('width'));
		$('#muid_span_w').val($('#muid_text span').actual('width'));
		$('#vuid_span_w').val($('#vuid_text span').actual('width'));
		
		$('#uid_span_h').val($('#uid_text span').actual('height'));
		$('#muid_span_h').val($('#muid_text span').actual('height'));
		$('#vuid_span_h').val($('#vuid_text span').actual('height'));
		
		if ($('#muid_text span br').length > 0) {
			$('#muid_linebreak').val('y');
		}
		else {
			$('#muid_linebreak').val('n');
		}
	}
	
	/* Default dept. name */
	
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
    	$('#uid_text').textfill({ minFontPixels: 10, maxFontPixels: 13 });
		muid_adjust();
		vuid_adjust();
		hidden_field_update();
    });

})