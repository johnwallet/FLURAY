$(document).ready(function () {
    $.each($('.radiochekbox'), function (index, val) {
        if($(this).find('input').prop('checked')===true){
            $(this).addClass('active');
        }
    });
    $(document).on('click', '.radiochekbox', function (event) {
        $(this).parents('.card-chekbox').find('.radiochekbox').removeClass('active');
        $(this).parents('.card-chekbox').find('.radiochekbox input').prop('checked', false);
        $(this).toggleClass('active');
        $(this).find('input').prop('checked', true);
        return false;
    });
    $(document).on('click', '.categories-in', function (){
        $('.categories-in--active').addClass('categories-in').removeClass('categories-in--active');
        $(this).addClass('categories-in--active').removeClass('categories-in');

        $('.form-rekvisites').toggleClass('active');
        $('.in-text').toggleClass('active');
        $('.in-box').toggleClass('active');
        $('.in-img-deposit').toggleClass('active');
        $('.in-img-withdrawal').toggleClass('active');
    });
    $(document).on('click', '#requsites-box-header1', function (){
        $('#requsites-box-content1').fadeToggle();
        $('#requsites-box-img1').toggleClass('transfor');
    });
    $(document).on('click', '#requsites-box-header2', function (){
        $('#requsites-box-content2').fadeToggle();
        $('#requsites-box-img2').toggleClass('transfor');
    });
    $(document).on('click', '#requsites-box-header3', function (){
        $('#requsites-box-content3').fadeToggle();
        $('#requsites-box-img3').toggleClass('transfor');
    });
    $(document).on('click', '#requsites-box-header4', function (){
        $('#requsites-box-content4').fadeToggle();
        $('#requsites-box-img4').toggleClass('transfor');
    });
    $(document).on('click', '#requsites-box-header5', function (){
        $('#requsites-box-content5').fadeToggle();
        $('#requsites-box-img5').toggleClass('transfor');
    });
    $(document).on('click', '#requsites-box-header6', function (){
        $('#requsites-box-content6').fadeToggle();
        $('#requsites-box-img6').toggleClass('transfor');
    });
    $(document).on('click', '#name-ps-1', function (){
        $('#card-ps-list-1').fadeToggle();
        $('#name-ps-img-1').toggleClass('transfor');
    });
    $(document).on('click', '#name-ps-2', function (){
        $('#card-ps-list-2').fadeToggle();
        $('#name-ps-img-2').toggleClass('transfor');
    });
    $(document).on('click', '#name-ps-3', function (){
        $('#card-ps-list-3').fadeToggle();
        $('#name-ps-img-3').toggleClass('transfor');
    });

    var cleavecard = new Cleave('#input-card', {
        creditCard: true,
    });




    // $(document).on('click', '#form-recvisites-tub', function (){
    //     $('#form-recvisites').attr("action", "/accounts/profile/rekvisitwallet/test");
    // });




});