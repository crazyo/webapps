/*******************************************************/

/* Modal Window

/*******************************************************/

	

	$('.rbc-modalwindow-trigger').live('click', function(event) {

																									 

		var triggerelement = $(this);

		var targetelement = $(triggerelement).metadata().targetelement;

		var closebutton = $(targetelement+' .rbc-modalwindow-close');

		var closebuttonhidden = $(targetelement+' .rbc-modalwindow-close-hidden');

		

        function showModalWindow() {

			$(targetelement).fadeIn(200);

			$('body').prepend('<div class="rbc-modalwindow-mask">&nbsp;</div>');

			$(".rbc-modalwindow-mask").stop().animate({

				opacity: .5

				}, 100, function() {

			});

			

			$(closebutton).focus();

       	 }    

		 

		 function hideModalWindow() {

			$(".rbc-modalwindow-mask").stop().animate({

				opacity: 0

				}, 100, function() {

				$(".rbc-modalwindow-mask").remove();

			});

			$(targetelement).fadeOut(200);

			$(triggerelement).focus();			

		}

 

 		if ($(targetelement).css('display') == 'block') {

			hideModalWindow();

			return false;

		}

		

		if ($(targetelement).css('display') == 'none') {

			showModalWindow();

		}

		

	

		$('body').click(function(event) {

			if ((!$(event.target).closest('.rbc-modalwindow-inner2').length) && ($(targetelement).css('display') == 'block')) {

				hideModalWindow();

			};

		});

		

		$(closebutton).click(function(){

			hideModalWindow();

			return false;

		});

		$(closebuttonhidden).click(function(){

			hideModalWindow();

			return false;

		});

		$(closebuttonhidden).blur(function(){

			hideModalWindow();	

			return false;

		});



		return false;

		

	});