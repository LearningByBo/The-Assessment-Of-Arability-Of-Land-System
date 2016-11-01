//ÿ�λ���һ��
$(function(){
	if(isSupportStyle()) {
		$('#dowebok').fullpage({
			//sectionsColor: ['#0A1629','#0A1629','#0A1629','#0A1629','#0A1629'],//����ÿҳ��ɫ
			scrollBar:true,
			navigation: true,
			fitToSection:false,
			scrollOverflow:false,
			//loopBottom:true,
			afterLoad: function(anchorLink, index){
			    if(index == 1){
			    	removeSectionClass();
					$('.section1').find('.slogan').addClass('animation1');
					$('.section1').find('.upload_tips').addClass('animation2_1');
				    $('.section1').find('.upload').addClass('animation2');
			    }
				if(index == 2){
					removeSectionClass();
				    $('.section2').find('.pic').addClass('animation1');
				    $('.section2').find('.pic_bottom').addClass('animation2');
				    $('.section2').find('.text_title').addClass('animation3');
				    $('.section2').find('.text_info').addClass('animation4');
				}
				if(index == 3){
					removeSectionClass();
				    $('.section3').find('.pic').addClass('animation1');
				    $('.section3').find('.pic_bottom').addClass('animation2');
				    $('.section3').find('.text_title').addClass('animation3');
				    $('.section3').find('.text_info').addClass('animation4');
				    //alert("11");
				}
				if(index == 4){
					removeSectionClass();
				    $('.section4').find('.pic').addClass('animation1');
				    $('.section4').find('.pic_bottom').addClass('animation2');
				    $('.section4').find('.text_title').addClass('animation3');
				    $('.section4').find('.text_info').addClass('animation4');
				}
				if(index == 5){
					removeSectionClass();
			        $('.section5').find('.slogan').addClass('animation1');
			        $('.section5').find('.upload_tips').addClass('animation2_1');
	                $('.section5').find('.upload').addClass('animation2');
	                
			    }

			},
			onLeave: function(index, direction){
			     if(index == '1'){
				    $('.section1').find('.slogan').removeClass('animation1');
	                $('.section1').find('.upload').removeClass('animation2');
	                $('.section1').find('.upload_tips').removeClass('animation2_1');

			    }
				if(index == '2'){;
				   $('.section2').find('.pic').removeClass('animation1');
				   $('.section2').find('.pic_bottom').removeClass('animation2');
				   $('.section2').find('.text_title').removeClass('animation3');
				   $('.section2').find('.text_info').removeClass('animation4');
				}
				if(index == '3'){
				   $('.section3').find('.pic').removeClass('animation1');
				   $('.section3').find('.pic_bottom').removeClass('animation2');
				   $('.section3').find('.text_title').removeClass('animation3');
				   $('.section3').find('.text_info').removeClass('animation4');
				}
				if(index == '4'){
				   $('.section4').find('.pic').removeClass('animation1');
				   $('.section4').find('.pic_bottom').removeClass('animation2');
				   $('.section4').find('.text_title').removeClass('animation3');
				   $('.section4').find('.text_info').removeClass('animation4');
				}
				if(index == '5'){
			   		$('.section5').find('.slogan').removeClass('animation1');
	                $('.section5').find('.upload').removeClass('animation2');
	                $('.section5').find('.upload_tips').removeClass('animation2_1');
			    }
			}
		});
	}else{
		$('#dowebok').fullpage({
			scrollBar:true,
			scrollOverflow:false,
			navigation: true,
			afterRender:function(){
				$(".slogan").removeClass("slogan").addClass("slogan_noaction");
				$(".upload").addClass("upload_noaction");
				$('.pic').removeClass('.pic').addClass('pic_noaction');
				$('.pic_bottom').removeClass('.pic_bottom').addClass('pic_bottom_noaction');
				$('.text_title').removeClass('.text_title').addClass('text_title_noaction');
				$('.text_info').removeClass('.text_info').addClass('text_info_noaction');
				$(".upload_tips").addClass("upload_tips_noaction");
				
			}
		});
	}
});
	function isSupportStyle(){
		var element = document.createElement("div");
		if(("transition" in element.style)||("-webkit-transition" in element.style)||
			("-moz-transition" in element.style)||("-o-transition" in element.style))
			return true;
		else return false;
	}
		function removeSectionClass(){
			   $('.pic').removeClass('animation1');
			   $('.pic_bottom').removeClass('animation2');
			   $('.text_title').removeClass('animation3');
			   $('.text_info').removeClass('animation4');
			   $(".slogan").removeClass("animation1");
			   $(".upload").removeClass("animation2");
			   $(".upload_tips").removeClass("animation2_1");
			   $(".tips_frame").hide();
		}
     //�������ǿ���
        ;(function(){
            var starListBox = $('.mod-star-list');
            //var sectionBox = $('.mod-bg-layer');
            starListBox.height(4000);
            var starListInner = starListBox.find('.inner');
            var meteorSeed = 100;
            var meteorHTML = '<div class="meteor"><div class="box"></div></div>';
            var starListHeight = starListBox.height();
            var starListWidth = starListBox.width();

            for(var i=0; i<meteorSeed; i++){
                var meteorEl = $(meteorHTML);
                var scaleRandom = Math.random() * 1.2 + 0.3;
                var rotateRandom = Math.random() * 10 - 2.5 + 'deg';
				meteorEl.css({
					'-webkit-transform': 'scale(' + scaleRandom + ') rotate(' + rotateRandom + ')',
					'-moz-transform': 'scale(' + scaleRandom + ') rotate(' + rotateRandom + ')',
					'transform': 'scale(' + scaleRandom + ') rotate(' + rotateRandom + ')',
					'top': (Math.random()+Math.floor(i/20)) * 800 + 'px',
					'right': Math.random() * starListWidth + 'px'
				});
                meteorEl.find('.box').css({
                    '-webkit-animation-delay': Math.random() * 10 +'s',
                    '-moz-animation-delay': Math.random() * 10 +'s',
                    'animation-delay': Math.random() * 10 +'s',
                    '-webkit-animation-duration': Math.random() * 2 + 3 +'s',
                    '-moz-animation-duration': Math.random() * 2 + 3 +'s',
                    'animation-duration': Math.random() * 2 + 3 +'s'
                });
                meteorEl.appendTo(starListInner).waypoint(function(direction) {
                    $(this).find('.box').addClass('action');
                }, {
                    offset: '100%',
                    triggerOnce: true
                });
            }

        })();
