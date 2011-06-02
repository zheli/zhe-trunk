/*
 * jQuery statusmessageQ plugin
 * @requires jQuery v1.4.2 or later
 *
 * Copyright (c) 2010 M. Brown (mbrowniebytes A gmail.com)
 * Licensed under the Revised BSD license:
 * http://www.opensource.org/licenses/bsd-license.php
 * http://en.wikipedia.org/wiki/BSD_licenses 
 *
 * Versions:
 * 0.4 - 2010-02-22
 *       added clear_msgs()
 * 0.3 - 2010-01-10
 *       restructured code per jquery plugin guidelines
 *       added warn_about_old_browser()
 * 0.2 - 2010-01-05
 *       start timeout after show
 *       show wrapper just before add messages rather than first action
 *       commented code 
 * 0.1 - 2009-06-29
 *       initial
 * 
 * usage:
 *  $(document).ready( function() {';
 *      $.fn.statusmessageQ({"message":"message to show", "type":"info"});';
 *  });
 *
 */
 
(function($) {
$.fn.statusmessageQ = function(options) {
	
	$.fn.statusmessageQ.show_msg(options);			
	
	return this;
}; // end statusmessageQ()	
	
	
$.fn.statusmessageQ.clear_msgs = function(options) {
	var opts = $.extend(true, $.fn.statusmessageQ.defaults, options);

	$('div#statusmessage_wrapper').find('div.statusmessage_icon').unbind('click');
	
	if (opts.quick_clear) {	
		$('div.statusmessage_wrapper').html('');
	} else {
		$('div.statusmessage_wrapper div.statusmessage').each(function(index) {
			var message = $(this);
			if (opts.hide == 'fadeOut') {
				message.fadeOut(opts.hidetime).remove();
			} else {
				message.hide(opts.hidetime).remove();
			} 
		});
	}
		
	if ($('div.statusmessage').length == 0) {
		$('div.statusmessage_wrapper').hide();
	} 		
}; // end clear_msgs()

// build, bind, show message 
$.fn.statusmessageQ.show_msg = function (options) {
	var opts = $.extend(true, $.fn.statusmessageQ.defaults, options);

	if (opts.decode) {
		opts.message = decodeURIComponent(opts.message);
	}
	
	// check for existing wrapper; else if none, add to top of body
	var message_wrapper = $('div.statusmessage_wrapper');
	if (message_wrapper.length == 0) {  
		message_wrapper = $('<div class="statusmessage_wrapper"></div>');
		$(document).find('body').prepend(message_wrapper);
	}
	
	// determine type, icon, css, etc
	var type = '';
	var close;
	if (opts.type == 'error') {
		type = 'statusmessage_error';
		close = $('<div class="statusmessage_error_icon statusmessage_icon"></div>');
	} else if (opts.type == 'warn') {
		type = 'statusmessage_warn';
		close = $('<div class="statusmessage_warn_icon statusmessage_icon"></div>');
	} else if (opts.type == 'info') {
		type = 'statusmessage_info';
		close = $('<div class="statusmessage_info_icon statusmessage_icon"></div>');		
	} else {
		// alert('Error: Unknown status message type ['+opts.type+']\n'+opts.message);
		return false;
	}
	
	// allow msg to be cleared by clicking on icon
	close.bind('click', function(e) {
		$(this).parent('div').remove();
		if ($('div.statusmessage').length == 0) {
			message_wrapper.hide();
		}
	});
	
	var occurrences = '';
	if (opts.occurrences > 0) {
		occurrences = '('+opts.occurrences+') ';
	}

	// build msg
	var message = $('<div class="statusmessage '+type+'">'+occurrences+opts.message+'</div>');
	message.prepend(close);
	
	// show wrapper; if was hidden on page load
	message_wrapper.show();

	// show new msg
	if (opts.show == 'fadeIn') {
		message_wrapper.append(message.hide().fadeIn(opts.showtime));   
	} else {
		message_wrapper.append(message.hide().show(opts.showtime)); 
	}
	
	// auto clear msg, if set
	if (opts.timeout > 0) {
		setTimeout(function() {
			if (opts.hide == 'fadeOut') {
				message.fadeOut(opts.hidetime).remove();
			} else {
				message.hide(opts.hidetime).remove();
			}
			if ($('div.statusmessage').length == 0) {
				message_wrapper.hide();
			}           
		}, opts.timeout);
	}	
}; // end show_msg()

// helper function to warn user about using browser which will not work well or at all
// minimize showing by settings opts.waob_nag  <= 100
// disable showing by setting opts.waob to false in statusmessageQ call
//   toggled perhaps by storing in cookie, or in a server db users table
$.fn.statusmessageQ.warn_about_old_browser = function (options) {
	// parse user agent string and warn user about old and ancient browsers
	// provides link to get latest browser
	// parses firefox, ie, opera, safari, chrome
	
	var opts = $.extend(true, $.fn.statusmessageQ.defaults, options);
	
	if (!opts.waob) {
		return true;
	} else {
		// if cookie plugin available, then show the warning on first load, then check nag %
		// else if no cookie plugin, rely on nag % or control of caller
		if ($.cookie && !$.cookie('statusmessageQ_waob')) {
			$.cookie('statusmessageQ_waob', 1);
		} else if (Math.floor(Math.random() * 99 + 1) < opts.waob_nag) {
			return true;
		}
	}
	
	// user agents checks for firefox and msie snagged from:
	// http://www.javascriptkit.com/javatutors/navigator.shtml
	// other user agents snagged from:
	// http://www.useragentstring.com/
	var useragent = navigator.userAgent;
	var msg = '';
	var version = '';		


	if (/Firefox\/(\d+\.\d+)/.test(useragent)) {
		version = new Number(RegExp.$1);
		if (version < 3) {
			msg = opts.waob_msg_ancient;
		} else if (version < 3.6) {
			msg = opts.waob_msg;				
		} else {
			return false;
		}
		msg = msg.replace(/<browser\/>/g, 'FireFox');
		msg = msg.replace(/<download>/, '<a href="http://www.mozilla.com/en-US/firefox/" target="_browser">');
		
	} else if (/MSIE (\d+\.\d+);/.test(navigator.userAgent)) { 
		version = new Number(RegExp.$1);
		if (version < 7) {
			msg = opts.waob_msg_ancient;		
		} else if (version < 8) {
			msg = opts.waob_msg;
		} else {
			return false;
		}
		msg = msg.replace(/<browser\/>/g, 'Internet Explorer');
		msg = msg.replace(/<download>/, '<a href="http://www.microsoft.com/nz/windows/internet-explorer/" target="_browser">');
		
	} else if (/Opera.*Version(\d+\.\d+)/.test(navigator.userAgent)) {
		version = new Number(RegExp.$1);
		if (version < 10) {
			msg = opts.waob_msg;
		} else {
			return false;
		}
		msg = msg.replace(/<browser\/>/g, 'Opera');
		msg = msg.replace(/<download>/, '<a href="http://www.opera.com/" target="_browser">');
		
	} else if (/Chrome\/(\d+\.\d+)/.test(navigator.userAgent)) {
		version = new Number(RegExp.$1);
		if (version < 4) {
			msg = opts.waob_msg;
		} else {
			return false;
		}
		msg = msg.replace(/<browser\/>/g, 'Chrome');
		msg = msg.replace(/<download>/, '<a href="http://www.google.com/chrome" target="_browser">');
		
	} else if (/Version\/(\d+\.\d+).*Safari$/.test(navigator.userAgent)) {
		version = new Number(RegExp.$1);
		if (version < 4) {
			msg = opts.waob_msg;
		} else {
			return false;
		}
		msg = msg.replace(/<browser\/>/g, 'Safari');
		msg = msg.replace(/<download>/, '<a href="http://www.apple.com/safari/" target="_browser">');
	} else {
		return false;
	}
	msg = msg.replace(/<version\/>/, version);
	msg = msg.replace(/<\/download>/, '</a>');
	
	var options = {
		'type': 'warn',
		'message': msg
	};		
	options = $.extend(true, opts, options);
	$.fn.statusmessageQ.show_msg(options);
	
	return true;
}; // end warn_about_old_browser()
	

$.fn.statusmessageQ.defaults = {
	'type': 'info',	// info, warn, error; matches css
	'message': '',	// text to display
	'occurrences': 0, // number of times message was repeated; only shown if > 0
	'timeout': 0,	// ms;  > 0 to have status msg automatically disappear ie growl; 
					// independent of showtime ie make larger than showtime if > 0
	'show': 'fadeIn', // fadeIn, show; animation to use on show
	'showtime': 1234,	// ms
	'hide': 'fadeOut', // fadeOut, hide; animation to use on hide
	'hidetime': 1234,	// ms
	'decode': true,	// true|false; if msg has been uri encoded; should be safe to keep true
	
	'quick_clear': false, // true|false; true - clear all messages; false - clear/hide each message
	
	'waob': true, // true|false; warn_about_old_browser;
	'waob_nag': 5, // 0-100; percent chance to nag user about old browser; 
	'waob_msg': 'Your browser (<browser/> <version/>) is out of date. It may not display all features of this and other websites. <download>Grab the latest <browser/></download>',
	'waob_msg_ancient': 'Your browser (<browser/> <version/>) is really out of date. It WILL NOT display all features of this and other websites. <download>Grab the latest <browser/></download>'
}; // end $.fn.statusmessageQ.defaults{}

})(jQuery);
