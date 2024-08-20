$(document).ready(function(){
    $('.lang-button').click(function(){
        var selectedLang = $(this).data('lang');
        $.ajax({
            url:'/home/change-language/',
            data:{lang:selectedLang},
            success:function(response){
                if (response.success){
                    location.reload();
                }else{
                    alert('Field To change Language');
                }
            },
            error:function(){
                alert('An error occurred while changing the language');
            }
        });
    });
});