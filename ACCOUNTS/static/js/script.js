/**
 * Created by Navneet Nandan on 16-10-2016.
 */
var main = function () {
    $('.user').click(function () {
        $('.user').removeClass("active");
        $(this).addClass("active");
    })
    $('.assignment_report_title').click(function () {
        $(".active").children('.assignment_report_description').hide();
        $(".active").removeClass("active");
        $(this).parent().children('.assignment_report_description').show();
        $(this).parent().addClass("active");

    })
    $('.prof-tab').click(function () {
        var id = $(this).attr('id');
        if(id=="student"){
            $('.tab-card').hide();
            $('.students-tab').show();
        }else if(id=="ta"){
            $('.tab-card').hide();
            $('.tas-tab').show();
        }else if(id=="assignment"){
            $('.tab-card').hide();
            $('.assignments-tab').show();
        }
        $('.prof-tab').removeClass("active");
        $(this).addClass("active");
    })
}
$(document).ready(main);