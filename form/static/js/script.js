$(document).ready(function(){

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
	})
	$('#previewlink_vuid').click(function() {
		$('.preview_active').hide().removeClass('preview_active');
		$('#vuid_img').fadeIn().addClass('preview_active');
	})

	/* Default dept. name */
	
	if (!($('#id_unit_name').text())) {
		$('.textfill span').text('Dept Name Here');
	}

	/* Textfill */
	
	$('#uid_text').textfill({ minFontPixels: 13, maxFontPixels: 13 });
    $('#vuid_text').textfill({ minFontPixels: 13, maxFontPixels: 36 });

    $('#id_unit_name').keyup(function() {
    	$('.textfill span').html(this.value);
    	$('#uid_text').textfill({ minFontPixels: 10, maxFontPixels: 13 });
	    $('#vuid_text').textfill({ minFontPixels: 18, maxFontPixels: 36 });
	
		/* MUID line height alterations */
		
		var muid_div = $('#muid_text'),
			muid_span = $('#muid_text span'),
			muid_text = muid_span.text(),
			muid_words = muid_text.split(' '),
			muid_wordcount_mid = Math.round(muid_words.length / 2);
		/* 2 words or less: force baseline down */
		if (muid_words.length <= 2) {
			muid_div.css('line-height', '44px');
		}
		else {
			muid_div.css('line-height', '14.5px');
			/* 3 or more words: Force a line break: */
			muid_words.splice(muid_wordcount_mid,0,'<br/>');
			muid_span.html(muid_words.join(' '));
		}
		
		/* VUID line height altercations */
		
		var vuid_span = $('#vuid_text span'),
			vuid_text = vuid_span.text(),
			vuid_lettercount = vuid_text.length,
			vuid_wordcount = vuid_text.split(' ').length,
			vuid_lineheight = vuid_span.css('line-height'),
			vuid_fontsize = parseInt(vuid_span.css('font-size').slice(0,-2));
		/* If the font size has changed, change the line height: */
		vuid_span.css('line-height', vuid_fontsize+'px');
    });

})