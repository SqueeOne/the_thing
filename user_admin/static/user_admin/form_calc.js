jQuery('.divide-form').on('change keyup check', '.form-control', function() {
    var sum = 0;
    var $time = parseFloat(jQuery('.hours-worked').text());
    var $alertdiv = jQuery("<div class='alert alert-danger'><p>Boooo hooo hooo</p></div>");
    jQuery('.form-control').each(function(){
        sum += +jQuery(this).val();
        if(sum>$time) {
            jQuery('.form-control').css('background-color', "red");
            jQuery('.btn').prop('disabled', true);
            
            jQuery('.alertz').append($alertdiv);
        } else {
            jQuery('.btn').prop('disabled', false);
            jQuery('.form-control').css('background-color', "#ffffff");
        }
    });
    
});


