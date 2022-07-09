let countrySelected = $('#id_country').val();
if(!countrySelected) {
    $('#id_country').css('color', '#E92500');
}
$('#id_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#E92500');
    } else {
        $(this).css('color', '#E92500');
    }
});