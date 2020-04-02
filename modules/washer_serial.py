import time

from pyquery import PyQuery as pq
from modules import generate_coser_url, generate_post_url, dump_file
from utils import log


def get_items_info(html):
    h = html
    result = dict()

    content = pq(h)
    items = content('.item')

    for i in items:
        i = pq(i)

        title = i('img').attr('title')
        number = i('date').text().split(' ')

        log(title, number)
    return 0


def get_actor_name(content: pq):
    name = content('.pb10').text()
    other_info = [p.text() for p in content('p').items()]
    log(name, other_info)

    txt_content = '\n'.join([name, *other_info])
    dump_file(f'{name}-info.txt', txt_content, path=f'data', mode='w')

    log(txt_content)
    return name


def get_movie_info(content: pq, name):
    c = content
    csv_content = ""
    img = c('.photo-frame')('img')
    photo_info = [p for p in c('.photo-info').items()]

    for index, i in enumerate(img.items()):
        if index == 0:
            continue
        date = photo_info[index]('date')
        info = [d.text() for d in date.items()]
        seriea_no, publish_date = info
        title = i.attr('title')
        log(title, seriea_no, publish_date)
        csv_content += f'{seriea_no}\t{title}\t{publish_date}\n'
    dump_file(f'{name}.txt', csv_content, path=f'data')

    log(csv_content)


if __name__ == '__main__':
    content_html = """
    
  <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="renderer" content="webkit">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>avvr - 搜尋 - 影片 - JavBus</title>
<meta name="keywords" content="">
<meta name="description" content="">
<link rel="alternate" href="https://www.javbus.com/en/search/avvr&type=&parent=ce" hreflang="en" />
<link rel="alternate" href="https://www.javbus.com/ja/search/avvr&type=&parent=ce" hreflang="ja" />
<link rel="alternate" href="https://www.javbus.com/ko/search/avvr&type=&parent=ce" hreflang="ko" />
<link rel="alternate" href="https://www.javbus.com/search/avvr&type=&parent=ce" hreflang="zh" />
<link rel="alternate" href="https://www.javbus.com/search/avvr&type=&parent=ce" hreflang="x-default" />
<link rel="canonical" href="https://www.javbus.com/search/avvr&type=&parent=ce" />
<link href='https://www.javbus.com/css/bootstrap.min.css' rel='stylesheet'>
<link href='https://www.javbus.com/css/bootstrap-theme.min.css' rel='stylesheet'>
<link href='https://www.javbus.com/css/magnific-popup.css' rel='stylesheet'>
<link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/base.css?v=3.7'>
<link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/nav.overlay.css?v=3.9.8' >
<script src='https://www.javbus.com/js/jquery.min.js'></script>
<script src='https://www.javbus.com/js/bootstrap.min.js'></script>
<script src='https://www.javbus.com/js/jquery.magnific-popup.min.js'></script>
<script src='https://www.javbus.com/js/jquery.cookie.min.js'></script>
<script src='https://www.javbus.com/js/base.js'></script>
<script src='https://www.javbus.com/js/bootstrap-hover-dropdown.js'></script>
<!--[if lt IE 9]> <script src='https://www.javbus.com/js/html5shiv.min.js'></script><script src='https://www.javbus.com/js/respond.min.js'></script><![endif]-->
</head>
<body>
<script language="JavaScript">
var mod = 0;
var lang = 'zh';
var info = '搜尋 識別碼, 影片, 演員';
function searchs(obj){
	var searchinput = $("#"+obj);
	if(searchinput.val()=='')
	{
		$('#magnet-url-post').trigger("click");	
		   return false;
	}
	else
	{
		//$('#search-loading').show();
		window.open("https://www.javbus.com/search/"+encodeURIComponent($.trim(searchinput.val()))+"&type=&parent=ce");
	}
}

$(function(){
		
	var url ='https://www.javbus.com/ajax/search-modal.php?floor='+Math.floor(Math.random()*1000+1)+'&lang='+lang;
       $.ajax({url: url,type: 'GET',success: function(msg){
			$("#searchModal").append(msg);										  
	   }});
});
</script>
<div id="search-loading">
    <table class="search-loading-box" border="0" cellpadding="0" cellspacing="0">
        <tbody>
            <tr>
                <td align="center">
                    <table height="80" width="100%" border="0" cellpadding="0" cellspacing="0">
                        <tbody>
                            <tr>
                                <td height="40" align="center">
                                	<div class="search-loading-text">搜尋中...</div>
                                </td>
                            </tr>
                            <tr>
                                <td height="40" align="center">
                                    <img src="https://www.javbus.com/images/search_loading.gif" border="0">
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Modal Search -->
<div id="searchModal" class="modal fade" tabindex="-1" role="dialog"></div>

<nav class="navbar navbar-default navbar-fixed-top top-bar" style="z-index:900">
    <div class="container-fluid">
        <div class="navbar-header mh50">
            <a href="https://www.javbus.com/">
                <img class="hidden-xs" height="50" alt="JavBus" src="https://www.javbus.com/images/logo.png" style="height:40px; margin-top:5px;">
                <img class="visible-xs-inline" height="50" alt="JavBus" src="https://www.javbus.com/images/logo.png">
            </a>                                                 

            <div class="btn-group pull-right visible-xs-inline" role="group" style="margin:8px 8px 0 0;" onclick="window.location.href= '/forum/member.php?mod=logging&action=login&referer=%2F%2Fwww.javbus.com%2Fsearch%2Favvr%26type%3D%26parent%3Dce'">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <img class="avatar" style="width:22px; height:22px;" src="https://uc.javbus22.com/uc/avatar.php?uid=0&size=small">                 </button>
                            </div>
            

            <div class="btn-group pull-right visible-xs-inline" role="group" style="margin:8px 8px 0 0;">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <span class="glyphicon glyphicon-globe"></span>  <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" role="menu">
                    <li><a href="https://www.javbus.com/en/search/avvr&type=&parent=ce">English</a></li>
                    <li><a href="https://www.javbus.com/ja/search/avvr&type=&parent=ce">日本语</a></li>
                    <li><a href="https://www.javbus.com/ko/search/avvr&type=&parent=ce">한국의</a></li>
                    <li><a href="https://www.javbus.com/search/avvr&type=&parent=ce">中文</a></li>   
                </ul>
            </div>
 
 		             <div class="btn-group pull-right visible-xs-inline" role="group" style="margin:8px 8px 0 0;">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <span class="glyphicon glyphicon-magnet"></span>  <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" role="menu">
                	                    <li id="cellshowall"><a><span class="glyphicon glyphicon-film"></span> 全部影片</a></li>
                     
                </ul>
            </div>
        
		                      
 
        </div>
 
        <div id="navbar" class="collapse navbar-collapse">
            <div class="navbar-form navbar-left fullsearch-form">
                <div class="input-group">
                    <input id="search-input" type="text" class="form-control" placeholder="搜尋 識別碼, 影片, 演員">
                    <span class="input-group-btn">
                    <button class="btn btn-default" type="submit" onClick="searchs('search-input')">搜尋</button>
                    </span>
                </div>
            </div>
            <ul class="nav navbar-nav">
            	<li class="active"><a href="https://www.javbus.com/">有碼</a></li>                    
                <li><a href="https://www.javbus.com/uncensored">無碼</a></li>
                <li class="hidden-md hidden-sm"><!-- <div class="icon-new"></div> --><a href="https://www.javbus.one/">歐美</a></li>
				<li><a href="https://www.javbus.com/forum/">論壇</a></li>            	
                <li class="dropdown hidden-sm ">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false">類別 <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="https://www.javbus.com/genre">有碼類別</a></li>
                        <li><a href="https://www.javbus.com/uncensored/genre">無碼類別</a></li>				
                    </ul>
                </li>
                <li class="dropdown hidden-sm ">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false">女優 <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="https://www.javbus.com/actresses">有碼女優</a></li>
                        <li><a href="https://www.javbus.com/uncensored/actresses">無碼女優</a></li>				
                    </ul>
                </li>                
                <li class="dropdown"><a href="https://www.javbus.com/" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-menu-hamburger"></span></a>
                    <ul class="dropdown-menu" role="menu">
                    	<li class="visible-md-block visible-sm-block"><a href="https://www.avbus.one/">歐美</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/genre">有碼類別</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/uncensored/genre">無碼類別</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/actresses">有碼女優</a></li>
                        <li class="visible-sm-block"><a href="https://www.javbus.com/uncensored/actresses">無碼女優</a></li>                        
                        <li><a href="https://www.javbus.com/genre/hd">高清</a></li>
                        <li><a href="https://www.javbus.com/genre/sub">字幕</a></li>
                    </ul>
				</li> 
            </ul>
            
            <ul class="nav navbar-nav navbar-right" onclick="window.location.href= '/forum/member.php?mod=logging&action=login&referer=%2F%2Fwww.javbus.com%2Fsearch%2Favvr%26type%3D%26parent%3Dce'">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false"><img class="avatar" src="https://uc.javbus22.com/uc/avatar.php?uid=0&size=small"><span class="hidden-md hidden-sm ml5">登入</span> </a>
                                    </li>
            </ul>
            
            
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-globe" style="font-size:12px;"></span> <span class="hidden-md hidden-sm">English</span> <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="https://www.javbus.com/en/search/avvr&type=&parent=ce">English</a></li>
                        <li><a href="https://www.javbus.com/ja/search/avvr&type=&parent=ce">日本语</a></li>
                        <li><a href="https://www.javbus.com/ko/search/avvr&type=&parent=ce">한국의</a></li>
                        <li><a href="https://www.javbus.com/search/avvr&type=&parent=ce">中文</a></li>   
                    </ul>
                </li>
            </ul>

                        
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-magnet" style="font-size:12px;"></span> <span class="hidden-md hidden-sm">已有磁力</span> <span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                                            <li class="mypointer" id="showall"><a><span class="glyphicon glyphicon-film"></span> 全部影片</a></li>
					  
                    </ul>
                </li>
            </ul>
                        
        	              
        </div>
        <!--/.nav-collapse -->
    </div>
</nav>
<div class="row visible-xs-inline footer-bar">
    <div class="col-xs-3 text-center">
        <a id="menu" class="btn btn-default trigger-overlay"><span class="glyphicon glyphicon-align-justify"></span></a>
    </div>
    <div class="col-xs-3 text-center">
         </div>
    <div class="col-xs-3 text-center">
        </div>    
    <div class="col-xs-3 text-center">
        <a id="back" class="btn btn-default" href="javascript:window.history.back()"><span class="glyphicon glyphicon-share-alt flipx"></span></a>
    </div>    
</div>    
<script src='https://www.javbus.com/js/focus.js?v=8.7'></script>  <link rel='stylesheet' type='text/css' href='https://www.javbus.com/css/main.css'>
<script src='https://www.javbus.com/js/jquery.masonry.min.js'></script>
<div class="container-fluid">
    <div class="row">

<style type="text/css">
@media screen and (max-width: 1490px) { 
.ad-table {display:none;}  
} 
@media screen and (min-width: 1490px) { 
.ad-list {display:none;}  
}
</style>

<table class="ad-table">
	    <tr>
        <td><a href="https://www.29887111.com//?inviteCode=231" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_19.gif" width="728" height="90"></a></td>
        <td><a href="http://vip.988340.com:966/66055.html" target="_blank" rel="nofollow"><img src="/ads/yh_728x90_4.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://103.214.164.35/javbus.htm" target="_blank" rel="nofollow"><img src="/ads/ylg728x90_1.gif" width="728" height="90"></a></td>
        <td><a href="http://488.g88885555.com:8200/wy36.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_57.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://107.183.16.164:3369/busdmm.html" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_18.gif" width="728" height="90"></a></td>
        <td><a href="http://uidh78.com/?channelCode=02191221487174" target="_blank" rel="nofollow"><img src="/ads/hlqp_728x90_1.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://ky.g66667777.com:8001/dky02.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_54.gif" width="728" height="90"></a></td>
        <td><a href="https://www.lsy01.com" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_1.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://45.118.248.105:2888/62.html" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_20.gif" width="728" height="90"></a></td>
        <td><a href="https://88zn.cc/tuitui/21javbuss/" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_1.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://23.225.133.126:9999/javbus.htm" target="_blank" rel="nofollow"><img src="/ads/wns728x90_3.gif" width="728" height="90"></a></td>
        <td><script data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="708048" data-width="728" data-height="90"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":708048});</script></td>
    </tr>
        <tr>
        <td><a href="http://www.142904.com/javb.html" target="_blank" rel="nofollow"><img src="/ads/ylg728x90_2.gif" width="728" height="90"></a></td>
        <td><a href="https://www.yabo226.com/?i_code=9410072&" target="_blank" rel="nofollow"><img src="/ads/yb_728x90_4.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://vip.ky611ky611.com:8899/ky61.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_60.gif" width="728" height="90"></a></td>
        <td><a href="http://7799.g77776666.com:8200/cs35.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_49.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://45.10.209.134:3299/javbus.htm" target="_blank" rel="nofollow"><img src="/ads/wns728x90_4.gif" width="728" height="90"></a></td>
        <td><a href="http://888.w77777777.com:8188/b26.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_58.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://pai.504606.com:606/58603542.html" target="_blank" rel="nofollow"><img src="/ads/yh_728x90_3.gif" width="728" height="90"></a></td>
        <td><a href="http://172.246.105.58:6589/dmmbus.html" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_17.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="http://df.u77777777.com:8118/fa45.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_56.gif" width="728" height="90"></a></td>
        <td><a href="https://www.bobvip66.com/1581691845?agent_code=22124" target="_blank" rel="nofollow"><img src="/ads/bob_728x90_4.gif" width="728" height="90"></a></td>
    </tr>
                        
</table>


<div class="ad-list">
<div class="pb10 text-center bn728-93"><a href="https://www.29887111.com//?inviteCode=231" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_19.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://vip.988340.com:966/66055.html" target="_blank" rel="nofollow"><img src="/ads/yh_728x90_4.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://103.214.164.35/javbus.htm" target="_blank" rel="nofollow"><img src="/ads/ylg728x90_1.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://488.g88885555.com:8200/wy36.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_57.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://107.183.16.164:3369/busdmm.html" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_18.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://uidh78.com/?channelCode=02191221487174" target="_blank" rel="nofollow"><img src="/ads/hlqp_728x90_1.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://ky.g66667777.com:8001/dky02.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_54.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://www.lsy01.com" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_1.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://45.118.248.105:2888/62.html" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_20.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://88zn.cc/tuitui/21javbuss/" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_1.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://23.225.133.126:9999/javbus.htm" target="_blank" rel="nofollow"><img src="/ads/wns728x90_3.gif" width="728" height="90"></a></div> <div class="hidden-xs text-center"><script data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="708048" data-width="728" data-height="90"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":708048});</script></div> <div class="pb10 text-center bn728-93"><a href="http://www.142904.com/javb.html" target="_blank" rel="nofollow"><img src="/ads/ylg728x90_2.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://www.yabo226.com/?i_code=9410072&" target="_blank" rel="nofollow"><img src="/ads/yb_728x90_4.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://vip.ky611ky611.com:8899/ky61.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_60.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://7799.g77776666.com:8200/cs35.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_49.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://45.10.209.134:3299/javbus.htm" target="_blank" rel="nofollow"><img src="/ads/wns728x90_4.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://888.w77777777.com:8188/b26.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_58.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://pai.504606.com:606/58603542.html" target="_blank" rel="nofollow"><img src="/ads/yh_728x90_3.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://172.246.105.58:6589/dmmbus.html" target="_blank" rel="nofollow"><img src="/ads/znj_xyc_728x90_17.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="http://df.u77777777.com:8118/fa45.html" target="_blank" rel="nofollow"><img src="/ads/mw728x90_56.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://www.bobvip66.com/1581691845?agent_code=22124" target="_blank" rel="nofollow"><img src="/ads/bob_728x90_4.gif" width="728" height="90"></a></div></div>                

<div class="alert alert-info alert-dismissable alert-common" style="position:relative">
    <button type="button" class="close" style="position:absolute; right:8px; top:3px;" data-dismiss="alert" onclick='javascript:$.cookie("cnadd26", "off",{expires: 365,path: "/"})'>&times;</button>
    <div class="row">
    	<div class="col-xs-12 col-md-6 col-lg-3 text-center"><strong>永久域名：</strong><a href="https://www.javbus.com" target="_blank">https://www.javbus.com</a></div>
<div class="col-xs-12 col-md-6 col-lg-3 text-center"><strong>防屏蔽地址：</strong><a href="https://www.cdnbus.one" rel="nofollow">https://www.cdnbus.one</a></div><div class="col-xs-12 col-md-6 col-lg-3 text-center"><strong>防屏蔽地址：</strong><a href="https://www.seedmm.zone" rel="nofollow">https://www.seedmm.zone</a></div><div class="col-xs-12 col-md-6 col-lg-3 text-center"><strong>防屏蔽地址：</strong><a href="https://www.seedmm.one" rel="nofollow">https://www.seedmm.one</a></div>         	
	</div>
</div>     		


<div class="alert alert-success alert-common">
    <p><b>avvr - 搜尋 - 影片 - JavBus</b>&nbsp;：&nbsp;當前顯示<b><a class='mypointer' id='resultshowmag'>&nbsp;<span class='glyphicon glyphicon-magnet'></span>&nbsp;已有磁力&nbsp;6&nbsp;</a></b>&nbsp;部，可切換至<b><a class='mypointer' id='resultshowall'>&nbsp;<span class='glyphicon glyphicon-film'></span>&nbsp;全部影片&nbsp;153&nbsp;</a></b>&nbsp;部</div>

<div class="search-header">
    <ul class="nav nav-tabs">
      <li role="presentation" class="active"><a href="https://www.javbus.com/search/avvr&type=1">有碼影片 ( <span class='glyphicon glyphicon-magnet'></span> 6 / <span class='glyphicon glyphicon-film'></span> 153 ) </a></li>
      <li role="presentation" ><a href="https://www.javbus.com/uncensored/search/avvr&type=1">無碼影片 ( <span class='glyphicon glyphicon-magnet'></span> 0 / <span class='glyphicon glyphicon-film'></span> 0 ) </a></li>
      <li role="presentation" ><a href="https://www.javbus.com/searchstar/avvr">女優</a></li>
      <li role="presentation" ><a href="https://www.javbus.com/search/avvr&type=2">導演</a></li>
      <li role="presentation" ><a href="https://www.javbus.com/search/avvr&type=3">製作商</a></li>
      <li role="presentation" ><a href="https://www.javbus.com/search/avvr&type=4">發行商</a></li>
      <li role="presentation" ><a href="https://www.javbus.com/search/avvr&type=5">系列</a></li>
    </ul>
</div>

        <div id="waterfall">    
			<div id="waterfall">
        
            <div class="item">
                <a class="movie-box" href="https://www.javbus.com/AVVR-471">
                    <div class="photo-frame">
                        <img src="https://pics.javbus.com/thumb/6xi3.jpg" title="【VR】肉感美女による、こちらを癒やす気など毛頭なしでひたすらパイズリ＆尻コキで挟んだオチ●ポを一切離さないオイルマッサージ中出しSEX◆ 由來ちとせ">
                    </div>                     
					<div class="photo-info">                                   
						<span>【VR】肉感美女による、こちらを癒やす気など毛頭なしでひたすらパイズリ＆尻コキで挟んだオチ●ポを一切離さないオイルマッサージ中出しSEX◆ 由來ちとせ<br />
						<div class="item-tag">
                            <button class="btn btn-xs btn-primary" disabled="disabled" title="包含高清HD的磁力連結">高清</button> 			
                            						</div>                        	
						<date>AVVR-471</date> / <date>2019-01-04</date></span>
					</div>
                </a>
            </div>
        
            <div class="item">
                <a class="movie-box" href="https://www.javbus.com/AVVR-370">
                    <div class="photo-frame">
                        <img src="https://pics.javbus.com/thumb/6klp.jpg" title="【VR】隣の奥さん達に毎日毎日骨抜きにされながら精子を枯れるまで吸い取られている日々。中出しのSEXまで… 清城ゆき 共演 川上ゆう">
                    </div>                     
					<div class="photo-info">                                   
						<span>【VR】隣の奥さん達に毎日毎日骨抜きにされながら精子を枯れるまで吸い取られている日々。中出しのSEXまで… 清城ゆき 共演 川上ゆう<br />
						<div class="item-tag">
                            						</div>                        	
						<date>AVVR-370</date> / <date>2018-04-27</date></span>
					</div>
                </a>
            </div>
        
            <div class="item">
                <a class="movie-box" href="https://www.javbus.com/AVVR-355">
                    <div class="photo-frame">
                        <img src="https://pics.javbus.com/thumb/6k7a.jpg" title="【VR】花魁 人妻ヘルスで中出し本番されちゃった僕。 前田可奈子 共演 佐々木あき">
                    </div>                     
					<div class="photo-info">                                   
						<span>【VR】花魁 人妻ヘルスで中出し本番されちゃった僕。 前田可奈子 共演 佐々木あき<br />
						<div class="item-tag">
                            						</div>                        	
						<date>AVVR-355</date> / <date>2018-04-20</date></span>
					</div>
                </a>
            </div>
        
            <div class="item">
                <a class="movie-box" href="https://www.javbus.com/AVVR-353">
                    <div class="photo-frame">
                        <img src="https://pics.javbus.com/thumb/6k7t.jpg" title="【VR】全裸家政婦麻妃！！中出しSEXご奉仕性活日記！！！ 北条麻妃">
                    </div>                     
					<div class="photo-info">                                   
						<span>【VR】全裸家政婦麻妃！！中出しSEXご奉仕性活日記！！！ 北条麻妃<br />
						<div class="item-tag">
                            						</div>                        	
						<date>AVVR-353</date> / <date>2018-04-20</date></span>
					</div>
                </a>
            </div>
        
            <div class="item">
                <a class="movie-box" href="https://www.javbus.com/AVVR-335">
                    <div class="photo-frame">
                        <img src="https://pics.javbus.com/thumb/6j98.jpg" title="【VR】超肉弾おっぱい生中出しソープ 成海さやか 共演 村上涼子">
                    </div>                     
					<div class="photo-info">                                   
						<span>【VR】超肉弾おっぱい生中出しソープ 成海さやか 共演 村上涼子<br />
						<div class="item-tag">
                            						</div>                        	
						<date>AVVR-335</date> / <date>2018-04-06</date></span>
					</div>
                </a>
            </div>
        
            <div class="item">
                <a class="movie-box" href="https://www.javbus.com/AVVR-340">
                    <div class="photo-frame">
                        <img src="https://pics.javbus.com/thumb/6j9a.jpg" title="【VR】嫁の寝てる間に…こっそりネトラレ不倫中出しSEX 佐々木あき 共演 前田可奈子">
                    </div>                     
					<div class="photo-info">                                   
						<span>【VR】嫁の寝てる間に…こっそりネトラレ不倫中出しSEX 佐々木あき 共演 前田可奈子<br />
						<div class="item-tag">
                            						</div>                        	
						<date>AVVR-340</date> / <date>2018-04-06</date></span>
					</div>
                </a>
            </div>
</div>        </div>
    </div>
</div>
<script language="JavaScript">
    (function($) {
        $('#waterfall').masonry({
            itemSelector: ".item",
            isAnimated: false,
            isFitWidth: true
        });
    })(jQuery);
</script>



<table class="ad-table">
	    <tr>
        <td><script data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="365002" data-width="728" data-height="90"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":365002});</script></td>
        <td><a href="https://www.yabo226.com/?i_code=9410072&" target="_blank" rel="nofollow"><img src="/ads/yb_728x90_4.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="https://ipf001.com/?dc=MXGVR" target="_blank" rel="nofollow"><img src="/ads/bjqp_728x90_4.gif" width="728" height="90"></a></td>
        <td><a href="https://88zn.cc/tuitui/22javbusx/" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_2.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="https://www.lsy01.com" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_2.gif" width="728" height="90"></a></td>
        <td><a href="https://ipf001.com/?dc=JAVBUS" target="_blank" rel="nofollow"><img src="/ads/pf_728x90_2.gif" width="728" height="90"></a></td>
    </tr>
        <tr>
        <td><a href="https://www.bobvip66.com/1581691845?agent_code=22124" target="_blank" rel="nofollow"><img src="/ads/bob_728x90_3.gif" width="728" height="90"></a></td>
        <td><a href="https://funfree90.com/cn/cpcny/Register?aff=331974" target="_blank" rel="nofollow"><img src="/ads/ltt_728x90_10.jpg" width="728" height="90"></a></td>
    </tr>
          
</table>


<div class="ad-list">
<div class="hidden-xs text-center"><script data-cfasync="false" async src="https://poweredby.jads.co/js/jads.js"></script><ins id="365002" data-width="728" data-height="90"></ins><script type="text/javascript" data-cfasync="false" async>(adsbyjuicy = window.adsbyjuicy || []).push({"adzone":365002});</script></div> <div class="pb10 text-center bn728-93"><a href="https://www.yabo226.com/?i_code=9410072&" target="_blank" rel="nofollow"><img src="/ads/yb_728x90_4.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://ipf001.com/?dc=MXGVR" target="_blank" rel="nofollow"><img src="/ads/bjqp_728x90_4.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://88zn.cc/tuitui/22javbusx/" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_2.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://www.lsy01.com" target="_blank" rel="nofollow"><img src="/ads/ysapp_728x90_2.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://ipf001.com/?dc=JAVBUS" target="_blank" rel="nofollow"><img src="/ads/pf_728x90_2.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://www.bobvip66.com/1581691845?agent_code=22124" target="_blank" rel="nofollow"><img src="/ads/bob_728x90_3.gif" width="728" height="90"></a></div> <div class="pb10 text-center bn728-93"><a href="https://funfree90.com/cn/cpcny/Register?aff=331974" target="_blank" rel="nofollow"><img src="/ads/ltt_728x90_10.jpg" width="728" height="90"></a></div></div>
<footer class="footer hidden-xs">
	<div class="container-fluid">
        <p><a href="https://www.javbus.com/doc/terms">Terms</a> / <a href="https://www.javbus.com/doc/privacy">Privacy</a> / <a href="https://www.javbus.com/doc/usc">2257</a> / <a href="http://www.rtalabel.org/" target="_blank" rel="external nofollow">RTA</a> / <a href="javascript:bootstr(1);" r>廣告投放</a> / <a href="javascript:bootstr(2);" >聯絡我們</a><br /><a href="#formModal" id="adscontact" data-toggle="modal"></a>
        Copyright © 2013 JavBus. All Rights Reserved. All other trademarks and copyrights are the property of their respective holders. The reviews and comments expressed at or through this website are the opinions of the individual author and do not reflect the opinions or views of JavBus. JavBus is not responsible for the accuracy of any of the information supplied here.</p>
	</div>
</footer>
<div class="visible-xs-block footer-bar-placeholder"></div>

<script language=javascript>
    function bootstr(type){
    	ads = "廣告投放";
    	contact = "聯絡我們";
    	translate = "翻譯";
    	$("#adstype").val(type);
    	if(type==1){
    		$("#contactModalLab").html(ads);
    		$("#qqskype").show();
    		$("#transinfo").hide();
    		$("#translanguage").hide();
    		$("#mailcontent").show();		
    	}else if(type==2){
    		$("#contactModalLab").html(contact);
    		$("#qqskype").show();
    		$("#transinfo").hide();
    		$("#translanguage").hide();
    		$("#mailcontent").show();
    	}else if(type==3){
    		$("#contactModalLab").html(translate);
    		$("#qqskype").hide();
    		$("#transinfo").show();
    		$("#translanguage").show();
    		$("#mailcontent").hide();
    	}
    	$("#adscontact").trigger("click");
		getverifycode();    	
    };
    function getverifycode(){
       $('#verify').attr("src","/post/verify?"+Math.random()*10000);
    };
    function IsMail(mail){
     var remail= /^([a-zA-Z0-9_-])+(\.)?([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
     return(remail.test(mail));
    };
    function checkform(){
    	var post = true; 
      if($("#verifycode").val().length!=5){
    	  	alert("驗證碼輸入錯誤!") 
    		$("#verifycode").focus(); 
    		post = false;
    	  }
      if($("#contact").val().length>255){
    	  	alert("聯繫方式字數過多!") 
    		$("#contact").focus(); 
    		post = false;
    	  }
      
      if(!IsMail($("#mail").val())){
    	alert("請輸入正確的電郵地址!") 
     	$("#mail").focus(); 
        post = false;
      }
      
      if($("#intention").val().length>25500){
    	  	alert("投放意向字數過多!") 
    		$("#intention").focus(); 
    		post = false;
    	  }
    	  
      if($("#trans").val().length>255){
    	  	alert("Too many words in your language textbox!") 
    		$("#intention").focus(); 
    		post = false;
    	  }	  
      if(post== true){
    	  $("#modalclose").trigger("click");
    	  $("#postform").attr("action", "/post/contact");
    	  $("#postform").submit();
    	}
      return post;
    };
</script>

<script>
$("#showmag,#cellshowmag,#resultshowmag").click(function(){
	$.cookie("existmag", "mag",{expires:365,path:'/'}); 
	location.reload() 
});

$("#showall,#cellshowall,#resultshowall").click(function(){
	$.cookie("existmag", "all",{expires:365,path:'/'}); 
	location.reload() 
});
$("#showonline").click(function(){
	$.cookie("existmag", "online",{expires:365,path:'/'}); 
	location.reload() 
});
$(".info .mypointer").click(function(){
	var obj = $(this);
	var code = obj.attr('value');
	var token = $("#token").val();
	var e = "../ajax/addfavorite.php?code=" + encodeURIComponent(code) + "&token=" + encodeURIComponent(token) + "&floor=" + Math.floor(Math.random() * 1e3 + 1);
    $.ajax({
        url: e,
        type: "POST",
		//dataType: "json",
		cache:false,
        success: function (json) {
			//obj.html(json);
			ajaxobj=eval("("+json+")");
			if(ajaxobj.act=='err'){
				alert('收藏次數達上限，請稍候再試');	
			}else{
				obj.html(ajaxobj.act);
				obj.attr('value',ajaxobj.code);
				obj.attr('title',ajaxobj.title);
				$("#token").val(ajaxobj.token);
			}
        }
    });
});

$(".glyphicon-heart-empty").hover(function () {
    $(this).removeClass('glyphicon-heart-empty');
	$(this).addClass('glyphicon-heart');
}, function () {
    $(this).removeClass('glyphicon-heart');
    $(this).addClass('glyphicon-heart-empty');
});
$(".glyphicon-heart").hover(function () {
    $(this).removeClass('glyphicon-heart');
	$(this).addClass('glyphicon-heart-empty');
}, function () {
    $(this).removeClass('glyphicon-heart-empty');
    $(this).addClass('glyphicon-heart');
});
</script>

<!-- Modal Forms -->
<div id="formModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="formModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button id="modalclose" type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="contactModalLab">聯絡我們</h4>
            </div>
            <div class="modal-body">                     
                <form class="form-horizontal" name="postform" method="post" id="postform" enctype="multipart/form-data" >
                    <fieldset>
                                                <div class="form-group" id="qqskype">
                            <label class="col-sm-4 control-label" for="contact">QQ / Skype</label>
                            <div class="col-sm-6">
                                <input id="contact" name="contact" type="text" placeholder="" class="form-control">
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-4 control-label" for="mail">Email</label>
                            <div class="col-sm-6">
                                <input id="mail" name="mail" type="text" placeholder="" class="form-control">  
                            </div>
                        </div>
                        <div class="form-group" id="translanguage">
                            <label class="col-sm-4 control-label" for="trans">Your Language</label>
                            <div class="col-sm-6">
                                <input id="trans" name="trans" type="text" placeholder="" class="form-control">  
                            </div>
                        </div>
                        <div class="form-group" id="mailcontent">
                            <label class="col-sm-4 control-label" for="intention" id="inten-trans">內容</label>
                            <div class="col-sm-6">                     
                                <textarea id="intention" name="intention" rows="9" class="form-control"></textarea>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-4 control-label" for="verify">驗證碼</label>
                            <div class="col-sm-6">                     
                                <input type="text" id="verifycode" name="verifycode" style="width:50px"/>
                                <img id="verify" src="" style="cursor: pointer; vertical-align:middle;" onclick="getverifycode()"/>
                            </div>
                        </div>
                        <input type="hidden" id="adstype" name="adstype" value="1" />
                    </fieldset>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" button class="btn btn-primary" onclick="checkform()">送出</button>  
                <button type="button" button class="btn btn-default" data-dismiss="modal">關閉</button>
            </div>
        </div>
    </div>
</div>


<!-- ////////////////////////////////////////////////// -->
<div class="overlay overlay-contentscale">
    <div class="row">
        <div class="col-xs-12 text-center ptb20">
                 <div class="input-group col-xs-offset-2 col-xs-8">
                      <input id="search-input-mobile" type="text" class="form-control" placeholder="搜尋 識別碼, 影片, 演員">
                      <span class="input-group-btn">
                      <button class="btn btn-default" type="submit" onClick="searchs('search-input-mobile')">搜尋</button>
                      </span>
                 </div>
        </div>             
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/">有碼</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/uncensored">無碼</a></div>   
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/genre">有碼類別</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/uncensored/genre">無碼類別</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/actresses">有碼女優</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/uncensored/actresses">無碼女優</a></div>
		<div class="col-xs-6 text-center"><a href="https://www.javbus.one/">歐美</a></div>
        <div class="col-xs-6 text-center"><a href="https://www.javbus.com/forum/">論壇</a></div>
    
       <div class="col-xs-12 text-center overlay-close">
          <i class="glyphicon glyphicon-remove"></i>
       </div>  
    </div>
</div>
<script src='https://www.javbus.com/js/nav.overlay.js?v=10.30.3'></script>

<img src="http://cdn.rdrads.com/ipx_wYLiO7m31NUc1z1f.php" style="display:none">

</body>
</html>
"""
    get_items_info(content_html)
