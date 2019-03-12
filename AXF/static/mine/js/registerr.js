$(function () {
    $('.register').width(innerWidth)

    $('#username input').blur(function () {
        var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");

        if($(this).val()=='')return

        if (reg.test($(this).val())){
            request_data={
                'username':$(this).val()
            }
            $.get('/axf/checkusername/',request_data,function (response) {
                console.log(response)
                if (response.status){
                    $('#username-t').attr('data-content','账号可用').popover('hide')
                    $('#username').removeClass('has-error').addClass('has-success')
                    $('#username>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')

                }else{
                    $('#username-t').attr('data-content',response.msg).popover('show')
                    $('#username').removeClass('has-error').addClass('has-error')
                    $('#username>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
                }
            })
        }
        else {
            $('#username-t').attr('data-content','账号格式错误').popover('show')
                    $('#username').removeClass('has-success').addClass('has-error')
                    $('#username>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }

    })
//    密码验证
    $('#password input').blur(function () {
        var reg = new RegExp("^[a-zA-Z0-9_]{6,10}$");
        if ($(this).val()=='')return

        if (reg.test($(this).val())){
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        }else{
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
        })
    $('#password-d input').blur(function () {
        if ($(this).val()=='')return
        var x_val=$('#password input').val()
        var y_val=$('#password-d input').val()

        if(x_val==y_val){
            $('#password-t').popover('hide')
            $('#password-d').removeClass('has-error').addClass('has-success')
            $('#password-d>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        }else{
             $('#password-t').popover('show')
            $('#password-d').removeClass('has-success').addClass('has-error')
            $('#password-d>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })


//    昵称验证
    $('#name input').blur(function () {
        // 空，不需要验证处理
        if ($(this).val() == '') return

        // 格式是否正确
        if ( $(this).val().length>=3 || $(this).val().length<=10 ){  // 符合
            $('#name').removeClass('has-error').addClass('has-success')
            $('#name>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {    // 不符合
            $('#name').removeClass('has-success').addClass('has-error')
            $('#name>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
    
    $('#subButton').click(function () {
        var isregister = true
        $('.register .form-group').each(function () {
            if(!$(this).is('.has-success')){
                isregister=false
            }
        })
        if (isregister){
            $('.register form').submit()
        }
    })
})