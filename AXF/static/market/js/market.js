$(function () {
    var index = $.cookie('index')
    console.log(index)

    $('.type-slider li').eq(index).addClass('active')

    $('.type-slider li').click(function () {

        // $(this).addClass('active')
        $.cookie('index',$(this).index(),{expires:3,path:'/'})
    })

    var categoryShow=false
   $('#category-bt').click(function () {
       // if (categoryShow){
       //      categoryShow=false
       //     $('.category-view').hide()
       // }else{
       //      categoryShow=true
       //     $('.category-view').show()
       // }
       categoryShow = !categoryShow
       categoryShow ? categoryViewShow() : categoryViewHide()
   })
    function categoryViewShow() {
        $('.category-view').show()
        $('#category-bt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')

        sortViewhide()
        sortShow=false
    }
    function categoryViewHide() {
        $('.category-view').hide()
        $('#category-bt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')

    }
    var sortShow = false
    $('#sort-bt').click(function () {
        sortShow = ! sortShow
        sortShow ? sortViewShow():sortViewhide()

    })
    function sortViewShow() {
        $('.sort-view').show()
        $('#sort-bt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')

        categoryViewHide()
        categoryShow=false
    }
    function sortViewhide() {
        $('.sort-view').hide()
        $('#sort-bt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }

    $('.bounce-view').click(function () {
        categoryViewHide()
        categoryShow=false

        sortViewhide()
        sortShow=false
    })
})


