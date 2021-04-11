$(document).ready(function() {

$('#id1').click(function (e){
    alert('При нажатии на кнопку потребуется залогиниться ')
})
$('#id2').click(function (a){
    x = $('#exampleInputPassword1').val()
    if (x.length<8){
    alert('Пароль должен содержать как минимум 8 знаков')
        e.preventDefault() //если имя маленькое,то останавливает процесс
    }
})
    $('#id3').click(function(e){
        $.post('obmen',
            {
                'n': 4
            }, function(response){
            alert(response.num)
            }
        );
    })
    $( "#log_form" ).blur(function(e) {
        $.post('uniq',
            {
                'login': $( "#log_form" ).val()
            }, function(response){
            if(response.exist==1){
                alert('Такой пользователь уже существует')
            }
            }
        );
    })

});