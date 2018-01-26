jQuery('.divide-form').on('change', '.form-control', function() {
    var sum = 0;
    var timeLeft = parseFloat(jQuery('.hours-worked').text());;
    var $time = parseFloat(jQuery('.hours-worked').text());
    var $alertdiv = jQuery("<div class='alert alert-danger'><p>Število vnešenih ur je višje od količine oddelanih ur, prosim popravite znesek.</p></div>");
    jQuery('.form-control').each(function(){
        sum += +jQuery(this).val();
        timeLeft -= +jQuery(this).val();
        jQuery('.time-left').text(timeLeft).toString();
        if(sum>$time) {
            jQuery('.form-control').css('background-color', "red");
            jQuery('.btn').prop('disabled', true);
            jQuery('.alertz').append($alertdiv);
        } else if(sum<$time) {
            jQuery('.btn').prop('disabled', true);
            jQuery('.form-control').css('background-color', "#ffffff");
            jQuery('.alert').remove();
        } else {
            jQuery('.btn').prop('disabled', false);
            jQuery('.form-control').css('background-color', "#ffffff");
            jQuery('.alert').remove();
        }
    });
});