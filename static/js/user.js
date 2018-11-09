// $(document).ready(function(e){
//     return "undefined" == typeof pe || e && pe.event.triggered === e.type ? void 0 : pe.event.dispatch.apply(c.elem, arguments)
// })
$(document).ready(function () {
    user(); //顶部栏用户显示下拉框
    navTab(); //导航栏切换效果
    }
);

function user(){
    $('#navList').hide(); //打开页面隐藏下拉列表
    $('#user').mouseover ( //鼠标滑过导航栏目时
        function(){
            $('#navList').show(); //显示下拉列表
            // $(this).css({'color':'red','background-color':'orange'}); //设置导航栏目样式，醒目
        });
    $('#user').mouseout(function(){
            $('#navList').hide(); //鼠标移开后隐藏下拉列表
        }
    );
    $('#navList').mouseover( //鼠标滑过下拉列表自身也要显示，防止无法点击下拉列表
        function(){
            $('#navList').show();
        });
    $('#user').mouseout(function(){
            $('#navList').hide();
            // $('#user').css({'color':'white','background-color':'black'}); //鼠标移开下拉列表后，导航栏目的样式也清除
        }
    );
    $('dd').mouseover( //鼠标滑过下拉列表是改变当前栏目样式
        function(){
            $(this).css({'background-color':'rgb(30,159,255)'});
        });
    $('dd').mouseout(function(){
            $('dd').css({'background-color':'',fontWeight:''});
        }
    );
}

function navTab() {
    $('ul.navigation li').click(
        function () {
            $('ul.navigation li').toggleClass('layui-this');
            // console.log(this);
        }
    )
}