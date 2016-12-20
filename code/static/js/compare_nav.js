/**
 * Created by Bo on 2016/11/12.
 */

!function ($) {

    var defaults = {
        offset: 300,
        animate: 1000,
    };

    function isScrolledIntoView(elem) {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height() ;
        //alert('docview ' + docViewTop + ' , ' + docViewBottom);

        var elemTop = $(elem).offset().top;
        var elemBottom = elemTop + $(elem).height();
        //alert('elem ' + elemTop + ' , ' + elemBottom);

        var situation1 = (docViewTop >= elemTop) && (docViewBottom >= elemBottom) && (elemBottom > docViewTop)
        var situation2 = (docViewTop >= elemTop) && (docViewBottom < elemBottom)

        return (situation1 || situation2);
    }

    $.fn.jumpto = function (options) {
        // $.extend means to merge the parameters
        var settings = $.extend({}, defaults, options),
            // el = function's caller
            el = $(this),
            selectors = "";
        selectors += "#" + "DATA" + ", ";
        selectors += "#" + "DT" + ", ";
        selectors += "#" + "KNN" + ", ";
        selectors += "#" + "SVM" + ", ";
        selectors += "#" + "LR" + ", ";
        selectors += "#" + "Summarize" + ", ";

        redrawMenu = function () {
            //alert(selectors.slice(0,9));
            $(selectors.slice(0,-2)).each(function (index) {
                //alert($(this));
                if (isScrolledIntoView($(this))) {
                    $(".sub a").removeClass("set").parent().find(" a[href='#" + $(this).attr("id") + "']").addClass("set");
                    var ulpositionY = index * 38;
                    $(".sub ul").css("background-position","80px " + ulpositionY + "px");
                }
            });
            if ($(document).scrollTop() > settings.offset) {
                $(".sub").addClass("fixed");
                //alert($(".main").width())
                var right = $("#detail_frame").width() - $(".main").width();
                right = right / 2;
                $(".sub.fixed").css("right",right +"px");
            } else {
                $(".sub").removeClass("fixed");
                $(".sub").css("right","0px");
            }
        }

        $(window).scroll(function () {
            redrawMenu()
        });

    }
}(window.jQuery);


