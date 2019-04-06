/*
	Typify by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/
src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js";
  var lines = [];

(function($) {

	skel.breakpoints({
		xlarge:	'(max-width: 1680px)',
		large:	'(max-width: 1280px)',
		medium:	'(max-width: 980px)',
		small:	'(max-width: 736px)',
		xsmall:	'(max-width: 480px)'
	});




	$(function() {




		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 100);
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on medium.
			skel.on('+medium -medium', function() {
				$.prioritize(
					'.important\\28 medium\\29',
					skel.breakpoint('medium').active
				);
			});

			$("#getstarted").click(function(){
				$("#diagnoseform").toggle();
			})

			$("#search").click(function(){
					var client = $("#clientid1").val();
				//	alert("Client ID: " + client);

					$.ajax({
        type: "GET",
        url: "https://raw.githubusercontent.com/b300631/McHacks6/master/diagnosis.csv?token=AmrVUGiAHz619YrD1QrylA-Wy0n3o-A7ks5cX6_NwA%3D%3D",
        dataType: "text",
        success: function(data) {processData(data);}
     });


		 function processData(allText) {
		     var allTextLines = allText.split(/\r\n|\n/);
		     var headers = allTextLines[0].split(',');
		   //var lines = [];

		     for (var i=1; i<allTextLines.length; i++) {
		         var data = allTextLines[i].split(',');
		         if (data.length == headers.length) {
		             var tarr = [];
		             for (var j=0; j<headers.length; j++) {
		                 tarr.push(headers[j]+":"+data[j]);
		             }
		             lines.push(tarr);
		         }
		     }

				  //alert(lines);
				 for (var k=1; k<lines.length;k++) {
								//alert(lines[k]);
                var str = lines[k].toString();
            //  alert(str);
								if (str.indexOf(client) >= 0) {
									//		alert("found");
                  var d = str.split(" ");
                  var curr = lines[k] + "<br>" + "Diagnosis: ";
                //  $("h6").after(lines[k] + "<br>" + "Diagnosis: ");
                    //alert(d[1]);
                //    alert(d[1].toString().match(/\d+/)[0]);
                //    alert(parseFloat(d[1].toString()));
              //    alert(curr);

                  if (parseInt(d[1].toString().match(/\d+/)[0],10)>0) {
                  //  alert("i");
                    $("h6").after(curr + "Infection ");
                  }
                  if (parseInt(d[2].toString().match(/\d+/)[0],10)>0) {
                //    alert("o");
                    $("h6").after(curr + "Obesity ");
                  }
                  if (parseInt(d[3].toString().match(/\d+/)[0],10)>0) {
                //    alert("dia");
                    $("h6").after(curr + "Diabetes ");
                  }
                  if (parseInt(d[4].toString().match(/\d+/)[0],10)>0) {
                //    alert("dys");
                    $("h6").after(curr + "Dyslipidemia ");
                  }


          //    alert("end");
								}
				 }

		 	//	console.log(lines);
		 }

		// alert(lines);




/*
					$.get("https://raw.githubusercontent.com/b300631/McHacks6/master/test.csv?token=AmrVUH2fZ0ulP-JesJrJLyurDEHVMSsdks5cX6cjwA%3D%3D",function(data){

						// "https://www.w3.org/TR/PNG/iso_8859-1.txt",function(data)
						alert(data);
	   			$("#analysis").html("<p>" + data.replace(/\n/g, "<br />" + " </p>"));

				});
				alert("here");

				var htmlString = $("#analysis").html();
				var words = htmlString.split("<br>");
// split based on br

				for(var i=0; i < words.length; i++) {
					// Infection	Obesity	Diabetes	Dyslipidemia
						if (words[i].toLowerCase().indexOf(client) >= 0) {

							var test = words[i].replace("<p>","");
							test = test.replace("</p>","");
							var diseases = test.split(",");


								if (parseInt(diseases[1])>0) {
									alert("Infection");
								}
								if (parseInt(diseases[2])>0) {
									alert("Obesity");
								}
								if (parseInt(diseases[3])>0) {
									alert("Diabetes");
								}
								if (parseInt(diseases[4])>0) {
									alert("Dyslipidemia");
								}

					//			$("#analysis").remove();
					//			$("h6").after(test); //IT WORKS
						}
			}
			//	alert("end");

			*/

				});


	});


	$("#diagnose").click(function(){
		var b = $("#bmi").val();
		alert("diagnose clicked");


	});




})(jQuery);
