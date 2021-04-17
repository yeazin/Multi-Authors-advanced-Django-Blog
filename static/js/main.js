
"use strict";
/*======== Doucument Ready Function =========*/
jQuery(document).ready(function () {

    //CACHE JQUERY OBJECTS
    var $window = $(window);

    $window.on( 'load', function () {

        $("#status").fadeOut();
        $("#preloader").delay(350).fadeOut("slow");
        $("body").delay(350).css({ "overflow": "visible" });

        
        /* Init Wow Js */
        new WOW().init();

        /*========== End Masonry Grid ==========*/

        /* Preloader */
        
        $("#status").fadeOut();
        $("#preloader").delay(350).fadeOut("slow");

        /* END of Preloader */

    });
    /*======= jQuery navbar on scroll =========*/


    $window.on('scroll' , function () {

        if ($(".navbar-default").add(".navbar-inverse").offset().top > 50) {
            $(".reveal-menu-home").addClass("sticky-nav");
            $(".reveal-menu-blog").addClass("sticky-nav-white");
        } else {
            $(".reveal-menu-home").removeClass("sticky-nav");
            $(".reveal-menu-blog").removeClass("sticky-nav-white");
        }
    });

	/*======= Main Slider Init =========*/

	var interleaveOffset = 0.5;
	var swiperOptions = {
  		loop: true,
  		speed: 3000,
  		grabCursor: true,
  		watchSlidesProgress: true,
  		mousewheelControl: true,
  		keyboardControl: true,
  		autoplay: true,
  		navigation: {
    		nextEl: ".swiper-button-next",
    		prevEl: ".swiper-button-prev"
  		},
  		autoplay: {
   	 		delay: 3000,
  		},
  		fadeEffect: {
    		crossFade: true
  		},
  		on: {
    		progress: function() {
      			var swiper = this;
      			for (var i = 0; i < swiper.slides.length; i++) {
        			var slideProgress = swiper.slides[i].progress;
        			var innerOffset = swiper.width * interleaveOffset;
        			var innerTranslate = slideProgress * innerOffset;
        			swiper.slides[i].querySelector(".slide-inner").style.transform =
        			"translate3d(" + innerTranslate + "px, 0, 0)";
      			}
    		},
    		touchStart: function() {
      			var swiper = this;
      			for (var i = 0; i < swiper.slides.length; i++) {
        			swiper.slides[i].style.transition = "";
      			}
    		},
    		setTransition: function(speed) {
      			var swiper = this;
      			for (var i = 0; i < swiper.slides.length; i++) {
        			swiper.slides[i].style.transition = speed + "ms";
        			swiper.slides[i].querySelector(".slide-inner").style.transition =
        			speed + "ms";
      			}
    		}
  		}
	};

	var swiperOptions1 = {
  		loop: true,
  		speed: 3000,
  		grabCursor: true,
  		watchSlidesProgress: true,
  		mousewheelControl: true,
  		keyboardControl: true,
  		navigation: {
    		nextEl: ".swiper-button-next",
    		prevEl: ".swiper-button-prev"
  		},
  		autoplay: {
    		delay: 300000,
  		},
  		fadeEffect: {
    		crossFade: true
  		},
  		on: {
    		progress: function() {
      			var swiper = this;
      			for (var i = 0; i < swiper.slides.length; i++) {
        			var slideProgress = swiper.slides[i].progress;
        			var innerOffset = swiper.width * interleaveOffset;
        			var innerTranslate = slideProgress * innerOffset;
        			swiper.slides[i].querySelector(".slide-inner").style.transform =
        			"translate3d(" + innerTranslate + "px, 0, 0)";
      			}
    		},
    		touchStart: function() {
      			var swiper = this;
      			for (var i = 0; i < swiper.slides.length; i++) {
        			swiper.slides[i].style.transition = "";
      			}
    		},
    		setTransition: function(speed) {
      			var swiper = this;
      			for (var i = 0; i < swiper.slides.length; i++) {
        			swiper.slides[i].style.transition = speed + "ms";
       	 			swiper.slides[i].querySelector(".slide-inner").style.transition =
        			speed + "ms";
      			}
    		}
  		}
	};

	var swiper = new Swiper(".swiper-container-1", swiperOptions1);
	var swiper = new Swiper(".swiper-container", swiperOptions);

    /*======= Banner Resize with window size =========*/

    $window.on( 'resize', function () {
        var bodyheight = $(this).height();
        $("#mt_banner").height(bodyheight);
    }).resize();

    // back to top

    
    $(window).on( 'scroll' , function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    
    // scroll body to 0px on click
    $('#back-to-top').on( 'click' , function () {
        $('#back-to-top').tooltip('hide');
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
        
    $('#back-to-top').tooltip('show');

    /*======== One Page Scrolling ======= */

    $("#navigation").onePageNav({
        currentClass: "active",
        changeHash: true,
        scrollSpeed: 1000,
        scrollThreshold: 0.5,
        filter: "",
        easing: "swing",
        begin: function () {
            //I get fired when the animation is starting
        },
        end: function () {
            //I get fired when the animation is ending
        },
        scrollChange: function ($currentListItem) {
            //I get fired when you enter a section and I pass the list item of the section
        }
    });

    /*======== Isotope Filter Script =========*/

    var mt_personal = window.mt_personal || {},
        $win = $(window);

        mt_personal.Isotope = function () {

        // 4 column layout
        var isotopeContainer = $(".isotopeContainer");
        if (!isotopeContainer.length || !jQuery().isotope) return;
        $win.on('load' , function(){
            isotopeContainer.isotope({
                itemSelector: ".isotopeSelector"
            });
            $(".mt_filter").on("click", "a", function (e) {
                $(".mt_filter ul li").find(".active").removeClass("active");
                $(this).addClass("active");
                var filterValue = $(this).attr("data-filter");
                isotopeContainer.isotope({ filter: filterValue });
                e.preventDefault();
            });
        });

    };

    mt_personal.Isotope();

    /*======== End Contact Form ========*/

    // Search in header.
        if( $('.search-icon').length > 0 ) {
            $('.search-icon').on('click', function(e){
              e.preventDefault();
              $('.search-box-wrap').slideToggle();
            });
        }

 // accordian

    if ($('.accrodion-grp').length) {
        var accrodionGrp = $('.accrodion-grp');
        accrodionGrp.each(function () {
            var accrodionName = $(this).data('grp-name');
            var Self = $(this);
            var accordion = Self.find('.accrodion');
            Self.addClass(accrodionName);
            Self.find('.accrodion .accrodion-content').hide();
            Self.find('.accrodion.active').find('.accrodion-content').show();
            accordion.each(function() {
                $(this).find('.accrodion-title').on('click', function () {
                    if ($(this).parent().hasClass('active') === false ) {                   
                        $('.accrodion-grp.'+accrodionName).find('.accrodion').removeClass('active');
                        $('.accrodion-grp.'+accrodionName).find('.accrodion').find('.accrodion-content').slideUp();
                        $(this).parent().addClass('active');                    
                        $(this).parent().find('.accrodion-content').slideDown();        
                    };
                    

                });
            });
        });
        
    };

$("#contactform").validate({      
    submitHandler: function() {
      
      $.ajax({
        url : 'mail/contact.php',
        type : 'POST',
        data : {
          name : $('input[name="full_name"]').val(),
          email : $('input[name="email"]').val(),
          phone : $('input[name="phone"]').val(),
          comments : $('textarea[name="comments"]').val(),
        },
        success : function( result ){
          $('#contactform-error-msg').html( result );
          $("#contactform")[0].reset();
        }     
      });

    }
  });

/*======== Slick Slider =========*/

$('.slider-items').slick({
  infinite: true,
  autoplay: true,
  arrows: false,
  dots: false,
  speed:3000,
  slidesToShow: 2,
  slidesToScroll: 1,
  responsive: [
      {
      breakpoint: 767,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
      }
    }
  ]
});

$('.slider-foods').slick({
  infinite: true,
  autoplay: true,
  arrows: false,
  dots: false,
  speed:3000,
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
      {
      breakpoint: 991,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        infinite: true,
        }
      },  
      {
      breakpoint: 767,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
      }
    }
  ]
});

$('.slider-sports').slick({
  infinite: true,
  autoplay: true,
  arrows: true,
  dots: false,
  speed:1500,
  slidesToShow: 1,
  slidesToScroll: 1,
});

$('.slider-insta').slick({
  infinite: true,
  autoplay: true,
  arrows: false,
  dots: false,
  speed:3000,
  slidesToShow: 8,
  slidesToScroll: 2,
  responsive: [
      {
      breakpoint: 991,
      settings: {
        slidesToShow: 4,
      }
    },
    {
      breakpoint: 500,
      settings: {
        slidesToShow: 2,
      }
    }
  ]
});

$('.slider-store').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-thumbs'
});
$('.slider-thumbs').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.slider-store',
  dots: false,
  centerMode: true,
  arrows: true,
  focusOnSelect: true
});

$('.slider-shop').slick({
  infinite: true,
  autoplay: true,
  arrows: true,
  dots: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  responsive: [
      {
      breakpoint: 900,
      settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
      }
      },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
      }
    }
  ]
});

}(jQuery));


$(function () {
    $('a[href="#search"]').on('click', function(event) {
        event.preventDefault();
        $('#search').addClass('open');
        $('#search > form > input[type="search"]').focus();
    });
    
    $('#search, #search button.close').on('click keyup', function(event) {
        if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
            $(this).removeClass('open');
        }
    });
    
    
    //Do not include! This prevents the form from submitting for DEMO purposes only!
    $('form').submit(function(event) {
        event.preventDefault();
        return false;
    })
});
