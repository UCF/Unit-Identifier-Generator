$(document).ready(function(){

	/* Enable form submit button if Javascript is enabled: */
	$('input#form_submit').removeAttr('disabled');
	

	/* Default values for preview dimensions for hidden fields */
	var uid_span_w = 0,
		uid_span_h = 0,
		uid_fontsize = 12,
		muid_span_w = 0,
		muid_span_h = 0,
		muid_fontsize = 16,
		vuid_span_w = 0,
		vuid_span_h = 0,
		vuid_fontsize = 0;

	
	/* Default values for capital letter to regular letter size ratios: */
	var uid_caps_ratio = 1.31,
		muid_caps_ratio = 1.2,
		vuid_caps_ratio = 1.325;


	/* Set UID as default preview in toggle buttons */
	$('#previewlink_uid').button('toggle');	
	
	
	/* Define functions that adjust the UID, MUID and VUID previews: */
	
	var uid_adjust = function() {
		var uid_div = $('#uid_text');
		var uid_span = $('#uid_text .preview_textwrap');
		
		uid_div.textfill({ minFontPixels: 12, maxFontPixels: 12 });
	
		// Create faux small-caps:
		uid_span.each(function() {
			var uid_html = uid_span.html();
			if ($('#uid_text .preview_textwrap .preview_upper').length < 1) {
				$(this).html(uid_html.replace(/([A-Z])/g, '<span class="preview_upper">$1</span>'));
			}
		});
		$('#uid_text span.preview_upper').css('font-size', (uid_span.css('font-size').slice(0,-2)) * uid_caps_ratio +'px');
	}
	
	var muid_adjust = function() {
		var muid_div = $('#muid_text'),
			muid_span = $('#muid_text .preview_textwrap'),
			muid_text = muid_span.text(),
			muid_words = muid_text.split(' '),
			muid_wordcount_mid = Math.round(muid_words.length / 2),
			muid_text_length = muid_text.length;
		
		// 2 words or less: force baseline down
		if (muid_words.length <= 2) {
			muid_div.css('line-height', '44px');
		}
		else {
			muid_div.css('line-height', '13.75px');
			// 3 or more words: Force a line break:
			muid_words.splice(muid_wordcount_mid,0,'<br/>');
			muid_span.html(muid_words.join(' '));
		}
		
		// Create faux small-caps:
		muid_span.each(function() {
			var muid_html = muid_span.html();
			if ($('#muid_text span.preview_textwrap span.preview_upper').length < 1) {
				$(this).html(muid_html.replace(/([A-Z])/g, '<span class="preview_upper">$1</span>'));
			}
		});
		$('#muid_text span.preview_upper').css('font-size', (muid_span.css('font-size').slice(0,-2)) * muid_caps_ratio +'px');
	}
	
	var vuid_adjust = function() {
		var vuid_div = $('#vuid_text');
		vuid_div.textfill({ minFontPixels: 16, maxFontPixels: 32 });
		
		var	vuid_span = $('#vuid_text .preview_textwrap');
		vuid_fontsize = parseInt(vuid_span.css('font-size').slice(0,-2));
		
		// Create faux small-caps:
		vuid_span.each(function() {
			var vuid_html = vuid_span.html();
			if ($('#vuid_text span .preview_upper').length < 1) {
				$(this).html(vuid_html.replace(/([A-Z])/g, '<span class="preview_upper">$1</span>'));
			}
		});
		$('#vuid_text span.preview_upper').css('font-size', (vuid_span.css('font-size').slice(0,-2)) * vuid_caps_ratio +'px');
			
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
			muid_span_upscale_ratio = full_size_width / muid_preview_width;		
		
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
	
	
	/* Switch in/out logo previews */
	
	$('#previewlink_uid').click(function() {
		// Remove active class from current active preview div and fade out:
		$('.preview_active').hide().removeClass('preview_active');
		// Fade in new active preview div
		$('#uid_img').fadeIn().addClass('preview_active');
		uid_adjust();
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
		
	
	/* Textfill + adjustments onload */
	
	uid_adjust();
	muid_adjust();
	vuid_adjust();
	hidden_field_update();


	/* Strip HTML characters from incoming input */
	
	$('#id_unit_name').keypress(function() {
	    var strClean = $(this).val().replace(/<|>|=|\*|\/|\\|\{|\}/, '');
		strClean.slice(0,-1); // Backspace to prevent excess spaces
	    $(this).val(strClean);
	});
	

	/* Textfill + adjustments on keyup */
	
    $('#id_unit_name').keyup(function() {
    	$('.textfill span').html(this.value);
    	uid_adjust();
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