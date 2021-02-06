$(document).ready(function () {
    $(document).on('keyup', 'input', function (){
        if($(this).val()<0){
            $(this).val('0.00');
        }
    });

    function readURL(input) {

        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#avatar-img').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#id_avatar").change(function(){
        readURL(this);
    });

    //ЧЕКБОКСЫ
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
    $(document).on('click', '.btn-avatar-label', function (event) {
        $(this).toggleClass('succes');
    });
    $(document).on('click', '#chekbox-quickaplication', function () {
        $('#kriteri-fin-request-deposit').val('БЫСТРАЯ ЗАЯВКА');
    });
    $(document).on('click', '#chekbox-wincurse', function () {
        $('#kriteri-fin-request-deposit').val('ВЫГОДНЫЙ КУРС');
    });

    //ЧЕКБОКСЫ ПС
    $.each($('.block-checkbox'), function (index, val) {
       if($(this).find('input').prop('checked')===true){
           $(this).addClass('active');
       }
    });

    $(document).on('click', '.block-checkbox', function (event){
        if($(this).hasClass('active')){
            $(this).find('input').prop('checked', false);
        }else{
            $(this).find('input').prop('checked', true);
        }
        $(this).toggleClass('active')
    });

    // //КНОПКИ ПЕРЕКЛЮЧЕНИЕ РЕКВИЗИТЫ
    // $(document).on('click', '.categories-in', function (){
    //     $('.categories-in--active').addClass('categories-in').removeClass('categories-in--active');
    //     $(this).addClass('categories-in--active').removeClass('categories-in');
    //
    //     $('.form-rekvisites').toggleClass('active');
    //     $('.in-text').toggleClass('active');
    //     $('.in-box').toggleClass('active');
    //     $('.in-img-deposit').toggleClass('active');
    //     $('.in-img-withdrawal').toggleClass('active');
    // });
    //КНОПКИ СКРЫВАЮЩИЕ БЛОКИ С ПС ПОПОЛНЕНИЕ
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
    //ПОПОЛНЕНИЕ СМЕНА ЗНАЧЕНИЙ ЗАЯВКИ
    //БАНКИ
    $(document).on('click', '#sber-rub-deposit', function (){
        $('#name-fin-request-deposit').val('СБЕРБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('СБЕРБАНК')
        $('#span-range').text(list_min_range.sberbank_rub + ' - ' + list_max_range.sberbank_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.sberbank_rub + ' - ' + list_max_range.sberbank_rub + ' USD')
    });
    $(document).on('click', '#tinkoff-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ТИНЬКОФФ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ТИНЬКОФФ')
        $('#span-range').text(list_min_range.tinkoff_rub + ' - ' + list_max_range.tinkoff_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.tinkoff_rub + ' - ' + list_max_range.tinkoff_rub + ' USD')
    });
    $(document).on('click', '#alfabank-rub-deposit', function (){
        $('#name-fin-request-deposit').val('АЛЬФА БАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('АЛЬФА БАНК')
        $('#span-range').text(list_min_range.alfabank_rub + ' - ' + list_max_range.alfabank_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.alfabank_rub + ' - ' + list_max_range.alfabank_rub + ' USD')
    });
    $(document).on('click', '#vtb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ВТБ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ВТБ')
        $('#span-range').text(list_min_range.vtb_rub + ' - ' + list_max_range.vtb_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.vtb_rub + ' - ' + list_max_range.vtb_rub + ' USD')
    });
    $(document).on('click', '#raif-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РАЙФФАЙЗЕНБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РАЙФФАЙЗЕНБАНК')
        $('#span-range').text(list_min_range.raifaizen_rub + ' - ' + list_max_range.raifaizen_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.raifaizen_rub + ' - ' + list_max_range.raifaizen_rub + ' USD')
    });
    $(document).on('click', '#otkr-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ОТКРЫТИЕ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ОТКРЫТИЕ')
        $('#span-range').text(list_min_range.otkritie_rub + ' - ' + list_max_range.otkritie_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.otkritie_rub + ' - ' + list_max_range.otkritie_rub + ' USD')
    });
    $(document).on('click', '#psb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ПСБ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ПСБ')
        $('#span-range').text(list_min_range.psb_rub + ' - ' + list_max_range.psb_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.psb_rub + ' - ' + list_max_range.psb_rub + ' USD')
    });
    $(document).on('click', '#gazprom-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ГАЗПРОМБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ГАЗПРОМБАНК')
        $('#span-range').text(list_min_range.gazprombank_rub + ' - ' + list_max_range.gazprombank_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.gazprombank_rub + ' - ' + list_max_range.gazprombank_rub + ' USD')
    });
    $(document).on('click', '#standart-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РУССКИЙ СТАНДАРТ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РУССКИЙ СТАНДАРТ')
        $('#span-range').text(list_min_range.russtandart_rub + ' - ' + list_max_range.russtandart_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.russtandart_rub + ' - ' + list_max_range.russtandart_rub + ' USD')
    });
    $(document).on('click', '#rsb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РОССЕЛЬХОЗБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РОССЕЛЬХОЗБАНК')
        $('#span-range').text(list_min_range.rosselhoz_rub + ' - ' + list_max_range.rosselhoz_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.rosselhoz_rub + ' - ' + list_max_range.rosselhoz_rub + ' USD')
    });
    $(document).on('click', '#pochta-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ПОЧТА БАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ПОЧТА БАНК')
        $('#span-range').text(list_min_range.pochtabank_rub + ' - ' + list_max_range.pochtabank_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.pochtabank_rub + ' - ' + list_max_range.pochtabank_rub + ' USD')
    });
    $(document).on('click', '#rosbank-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РОСБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РОСБАНК')
        $('#span-range').text(list_min_range.rosbank_rub + ' - ' + list_max_range.rosbank_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.rosbank_rub + ' - ' + list_max_range.rosbank_rub + ' USD')
    });
    $(document).on('click', '#rnkb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РНКБ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РНКБ')
        $('#span-range').text(list_min_range.rnkb_rub + ' - ' + list_max_range.rnkb_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.rnkb_rub + ' - ' + list_max_range.rnkb_rub + ' USD')
    });
    $(document).on('click', '#mts-rub-deposit', function (){
        $('#name-fin-request-deposit').val('МТС БАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('МТС БАНК')
        $('#span-range').text(list_min_range.mtsbank_rub + ' - ' + list_max_range.mtsbank_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.mtsbank_rub + ' - ' + list_max_range.mtsbank_rub + ' USD')
    });
    //КОШЕЛЬКИ
    $(document).on('click', '#qiwi-rub-deposit', function (){
        $('#name-fin-request-deposit').val('QIWI RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('QIWI RUB')
        $('#span-range').text(list_min_range.qiwi_rub + ' - ' + list_max_range.qiwi_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.qiwi_rub + ' - ' + list_max_range.qiwi_rub + ' USD')
    });
    $(document).on('click', '#qiwi-usd-deposit', function (){
        $('#name-fin-request-deposit').val('QIWI USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('QIWI USD')
        $('#span-range').text(list_min_range.qiwi_usd + ' - ' + list_max_range.qiwi_usd + ' USD')
        $('#span-range-usd').text(list_min_range.qiwi_usd + ' - ' + list_max_range.qiwi_usd + ' USD')
    });
    $(document).on('click', '#payeer-rub-deposit', function (){
        $('#name-fin-request-deposit').val('PAYEER RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('PAYEER RUB')
        $('#span-range').text(list_min_range.payeer_rub + ' - ' + list_max_range.payeer_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.payeer_rub + ' - ' + list_max_range.payeer_rub + ' USD')
    });
    $(document).on('click', '#payeer-eur-deposit', function (){
        $('#name-fin-request-deposit').val('PAYEER EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('PAYEER EUR')
        $('#span-range').text(list_min_range.payeer_eur + ' - ' + list_max_range.payeer_eur + ' EUR')
        $('#span-range-usd').text(list_min_range.payeer_eur + ' - ' + list_max_range.payeer_eur + ' USD')
    });
    $(document).on('click', '#payeer-usd-deposit', function (){
        $('#name-fin-request-deposit').val('PAYEER USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('PAYEER USD')
        $('#span-range').text(list_min_range.payeer_usd + ' - ' + list_max_range.payeer_usd + ' USD')
        $('#span-range-usd').text(list_min_range.payeer_usd + ' - ' + list_max_range.payeer_usd + ' USD')
    });
    $(document).on('click', '#wm-rub-deposit', function (){
        $('#name-fin-request-deposit').val('WEBMONEY RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('WEBMONEY RUB')
        $('#span-range').text(list_min_range.webmoney_rub + ' - ' + list_max_range.webmoney_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.webmoney_rub + ' - ' + list_max_range.webmoney_rub + ' USD')
    });
    $(document).on('click', '#wm-eur-deposit', function (){
        $('#name-fin-request-deposit').val('WEBMONEY EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('WEBMONEY EUR')
        $('#span-range').text(list_min_range.webmoney_eur + ' - ' + list_max_range.webmoney_eur + ' EUR')
        $('#span-range-usd').text(list_min_range.webmoney_eur + ' - ' + list_max_range.webmoney_eur + ' USD')
    });
    $(document).on('click', '#wm-usd-deposit', function (){
        $('#name-fin-request-deposit').val('WEBMONEY USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('WEBMONEY USD')
        $('#span-range').text(list_min_range.webmoney_usd + ' - ' + list_max_range.webmoney_usd + ' USD')
        $('#span-range-usd').text(list_min_range.webmoney_usd + ' - ' + list_max_range.webmoney_usd + ' USD')
    });
    $(document).on('click', '#pm-btc-deposit', function (){
        $('#name-fin-request-deposit').val('PERFECT MONEY BTC');
        $('#val-deposit').text('BTC')
        $('#requisites-ps-name').text('PERFECT MONEY BTC')
        $('#span-range').text(list_min_range.pm_btc + ' - ' + list_max_range.pm_btc + ' BTC')
        $('#span-range-usd').text(list_min_range.pm_btc + ' - ' + list_max_range.pm_btc + ' USD')
    });
    $(document).on('click', '#pm-eur-deposit', function (){
        $('#name-fin-request-deposit').val('PERFECT MONEY EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('PERFECT MONEY EUR')
        $('#span-range').text(list_min_range.pm_eur + ' - ' + list_max_range.pm_eur + ' EUR')
        $('#span-range-usd').text(list_min_range.pm_eur + ' - ' + list_max_range.pm_eur + ' USD')
    });
    $(document).on('click', '#pm-usd-deposit', function (){
        $('#name-fin-request-deposit').val('PERFECT MONEY USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('PERFECT MONEY USD')
        $('#span-range').text(list_min_range.pm_usd + ' - ' + list_max_range.pm_usd + ' USD')
        $('#span-range-usd').text(list_min_range.pm_usd + ' - ' + list_max_range.pm_usd + ' USD')
    });
    $(document).on('click', '#paypal-rub-deposit', function (){
        $('#name-fin-request-deposit').val('PAYPAL RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('PAYPAL RUB')
        $('#span-range').text(list_min_range.paypal_rub + ' - ' + list_max_range.paypal_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.paypal_rub + ' - ' + list_max_range.paypal_rub + ' USD')
    });
    $(document).on('click', '#paypal-eur-deposit', function (){
        $('#name-fin-request-deposit').val('PAYPAL EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('PAYPAL EUR')
        $('#span-range').text(list_min_range.paypal_eur + ' - ' + list_max_range.paypal_eur + ' EUR')
        $('#span-range-usd').text(list_min_range.paypal_eur + ' - ' + list_max_range.paypal_eur + ' USD')
    });
    $(document).on('click', '#paypal-usd-deposit', function (){
        $('#name-fin-request-deposit').val('PAYPAL USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('PAYPAL USD')
        $('#span-range').text(list_min_range.paypal_usd + ' - ' + list_max_range.paypal_usd + ' USD')
        $('#span-range-usd').text(list_min_range.paypal_usd + ' - ' + list_max_range.paypal_usd + ' USD')
    });
    $(document).on('click', '#skrill-eur-deposit', function (){
        $('#name-fin-request-deposit').val('SKRILL EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('SKRILL EUR')
        $('#span-range').text(list_min_range.skrill_eur + ' - ' + list_max_range.skrill_eur + ' EUR')
        $('#span-range-usd').text(list_min_range.skrill_eur + ' - ' + list_max_range.skrill_eur + ' USD')
    });
    $(document).on('click', '#skrill-usd-deposit', function (){
        $('#name-fin-request-deposit').val('SKRILL USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('SKRILL USD')
        $('#span-range').text(list_min_range.skrill_usd + ' - ' + list_max_range.skrill_usd + ' USD')
        $('#span-range-usd').text(list_min_range.skrill_usd + ' - ' + list_max_range.skrill_usd + ' USD')
    });
    $(document).on('click', '#umoney-rub-deposit', function (){
        $('#name-fin-request-deposit').val('UMONEY RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('UMONEY RUB')
        $('#span-range').text(list_min_range.umoney_rub + ' - ' + list_max_range.umoney_rub + ' RUB')
        $('#span-range-usd').text(list_min_range.umoney_rub + ' - ' + list_max_range.umoney_rub + ' USD')
    });
    // КРИПТА
    $(document).on('click', '#btc-deposit', function (){
        $('#name-fin-request-deposit').val('BITCOIN');
        $('#val-deposit').text('BTC')
        $('#requisites-ps-name').text('BITCOIN')
        $('#span-range').text(list_min_range.btc + ' - ' + list_max_range.btc + ' BTC')
        $('#span-range-usd').text(list_min_range.btc + ' - ' + list_max_range.btc + ' USD')
    });
    $(document).on('click', '#ltc-deposit', function (){
        $('#name-fin-request-deposit').val('LITECOIN');
        $('#val-deposit').text('LTC')
        $('#requisites-ps-name').text('LITECOIN')
        $('#span-range').text(list_min_range.ltc + ' - ' + list_max_range.ltc + ' LTC')
        $('#span-range-usd').text(list_min_range.ltc + ' - ' + list_max_range.ltc + ' USD')
    });
    $(document).on('click', '#xmr-deposit', function (){
        $('#name-fin-request-deposit').val('MONERO');
        $('#val-deposit').text('XMR')
        $('#requisites-ps-name').text('MONERO')
        $('#span-range').text(list_min_range.xmr + ' - ' + list_max_range.xmr + ' XMR')
        $('#span-range-usd').text(list_min_range.xmr + ' - ' + list_max_range.xmr + ' USD')
    });
    $(document).on('click', '#etc-deposit', function (){
        $('#name-fin-request-deposit').val('ETHEREUM CLASSIC');
        $('#val-deposit').text('ETC')
        $('#requisites-ps-name').text('ETHEREUM CLASSIC')
        $('#span-range').text(list_min_range.etc + ' - ' + list_max_range.etc + ' ETC')
        $('#span-range-usd').text(list_min_range.etc + ' - ' + list_max_range.etc + ' USD')
    });
    $(document).on('click', '#dash-deposit', function (){
        $('#name-fin-request-deposit').val('DASH');
        $('#val-deposit').text('DASH')
        $('#requisites-ps-name').text('DASH')
        $('#span-range').text(list_min_range.dash + ' - ' + list_max_range.dash + ' DASH')
        $('#span-range-usd').text(list_min_range.dash + ' - ' + list_max_range.dash + ' USD')
    });
    $(document).on('click', '#xrp-deposit', function (){
        $('#name-fin-request-deposit').val('RIPPLE');
        $('#val-deposit').text('XRP')
        $('#requisites-ps-name').text('RIPPLE')
        $('#span-range').text(list_min_range.xrp + ' - ' + list_max_range.xrp + ' XRP')
        $('#span-range-usd').text(list_min_range.xrp + ' - ' + list_max_range.xrp + ' USD')
    });
    $(document).on('click', '#bch-deposit', function (){
        $('#name-fin-request-deposit').val('BITCOIN CASH');
        $('#val-deposit').text('BCH')
        $('#requisites-ps-name').text('BITCOIN CASH')
        $('#span-range').text(list_min_range.bch + ' - ' + list_max_range.bch + ' BCH')
        $('#span-range-usd').text(list_min_range.bch + ' - ' + list_max_range.bch + ' USD')
    });
    $(document).on('click', '#eth-deposit', function (){
        $('#name-fin-request-deposit').val('ETHEREUM');
        $('#val-deposit').text('ETH')
        $('#requisites-ps-name').text('ETHEREUM')
        $('#span-range').text(list_min_range.eth + ' - ' + list_max_range.eth + ' ETH')
        $('#span-range-usd').text(list_min_range.eth + ' - ' + list_max_range.eth + ' USD')
    });

    $('#requisites-ps-input').keyup(function (){
        var value = $(this).val();
        $('#requisites-fin-request-deposit').val(value);
    });

    $('#input-change').keyup(function (){
        var value = $(this).val();
        if(value === ''){
            value = 0;
        }
        if(value < 0){
            value = 0;
            $(this).val('')
        }
        $('#sum-fin-request-deposit').val(value);
    });

// РЕЗЕРВ МЕНЯЕМ НА ноль при загрузке
    $.each($('.block-reserv'), function (index, val) {
       if($(this).find('input').val()==='0E-8'){
           $(this).find('input').val('0.00000000');
       }
    });
});

//МАСКА НА ИНПУТ ДЛЯ ВВОДА КАРТЫ
$(document).ready(function () {
    var cleavecard = new Cleave('#input-card', {
        creditCard: true,
    });
});
