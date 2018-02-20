$(document).ready(function() {

$('button').on('click'), function(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
            url: '/choice_made/',
            type: 'GET',
            data: { post_id : element.attr("data-id")},

            success: function(response) {
                element.html(' ' + response);
            }
            });
};
});