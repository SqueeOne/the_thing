jQuery(document).ready(function(){
    jQuery('#id_start_time').timepicker({
        'disableTextInput': true,
        'timeFormat': 'H:i:s',
        'disableTimeRanges': [
            ['0:30am', '5am'],
            ['10pm', '0:29am']
        ],
        'scrollDefault': 'now'
    });
    jQuery('#id_end_time').timepicker({
        'disableTextInput': true,
        'timeFormat': 'H:i:s',
        'disableTimeRanges': [
            ['0:30am', '5am'],
            ['10pm', '0:29am']
        ],
        'scrollDefault': 'now'
    });
});