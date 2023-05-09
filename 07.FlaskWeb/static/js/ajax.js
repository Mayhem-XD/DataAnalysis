function changeQuote(){
    $.ajax({
        type: 'GET',
        url: '/change_quote',
        data: ' ',                           // 서버로 전달할 데이터
        success: function(msg){             // msg: 서버로부터 받은 데이터
            $('#quoteMsg').html(msg);
        }
    });
}
function change_addr(){
    $('#addrInput').attr('class','mt-2');           // input box가 보이게
}
function addrSubmit(){
    $('#addrInput').attr('class','mt-2 d-none');       // input box 안보이게
    let addr = $('#addrInputTag').val();
    $.ajax({
        type: 'GET',
        url: '/change_addr',
        data: {addr:addr},
        success: function(msg){
            $('#addr').html(msg);
        }

    });
}
function changWeather(){
    let addr = $('#addr').text();
    $.ajax({
        type: 'GET',
        url: '/change_weather',
        data: {addr:addr},
        success: function(result){
            $('#weather').html(result);
        }
    });

}
function changeProfile(){
    $('#imageInput').attr('class','mt-2');
}
function imageSubmit(){
    let imageInputValue = $('#image')[0];
    let formData = new FormData();
    formData.append('image',imageInputValue.files[0]);
    $.ajax({
        type: 'POST',
        url: '/change_profile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result){
            $('#imageInput').attr('class','mt-2 d-none');
            fname = 'http://127.0.0.1:5000/static/data/profile.png?q=' + result;
            $('#profile').attr('src',fname);
        }
    });
}
// function showHotplaces(){
//     $('#resDiv').attr('class','mt-2')
// }