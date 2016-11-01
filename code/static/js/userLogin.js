try{
	document.domain = "qq.com";
}catch(e){}
//请求链接数据直接用,改造为动态数据后，将在initHTML中使用

var MGR = {
	settedWidth:0,
	customWidth:76,
	domReady:function(){},			//初始
	expires:0,
	loadJquery:false,
	Uname:null,
	cookie:{},
	showLogin:function(url){
		var appid = document.body.getAttribute("appid");
		$("#login_ifr").attr("src","");
		if($("#login_ifr").attr("src").indexOf("http") < 0){
			var b = window.location + "";
			b = b.indexOf("#") == -1 ? b: b.substring(0, b.indexOf("#"));
			if(typeof url != "undefined" && url != "") {
				url = encodeURIComponent(url+"?rd=")+encodeURIComponent(encodeURIComponent(b));
			}else {
				url = encodeURIComponent(b);
			}
			
			$("#login_ifr").attr("src", "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid="+appid+"&s_url="+ url)
		}
		showDialog.show({id:"loginframe",bgcolor:"#000000",opacity:60});
	},
	loginout:function(type){
		
		var e = MGR.cookie;
		e.domain = "qq.com";
		MGR.appcookie("skey", "", e);
		MGR.appcookie("uin", "", e);
		//window.location.reload();
		if(type){
			MGR.showLogin();
		}else{
			window.location.reload();
		}
	},
	appcookie:function(f, j, m){ 
		var expires = MGR.expires;
		if(typeof j == "undefined"){
			if(0 < document.cookie.length){
				var k = document.cookie.match(new RegExp("(^| )" + f + "=([^;]*)(;|$)"));
				return (null === k) ? "": k[2]
			}
			return ""
		}else{
			if(arguments.callee(f) == j){
				return
			}else{
				m = $.extend({
					expires: 1,
					path: "/",
					domain: window.document.location.hostname
				},
				m || {});
				if(j === null){
					j = "";
					m.expires = -1
				}
				var g = "";
				if(m.expires && (typeof m.expires == "number" || m.expires.toUTCString)){
					var h;
					if(typeof m.expires == "number"){
						h = new Date();
						h.setTime(h.getTime() + (m.expires * 1 * 60 * 60 * 1000))
					}else{
						h = m.expires
					}
					g = h.toUTCString()
				}
				var l = m.path ? "; path=" + (m.path) : "";
				var i = m.domain ? "; domain=" + (m.domain) : jQuery.getHost();
				var e = m.secure ? "; secure": "";
				document.cookie = f + "=" + j + "; path=" + l + "; domain=" + i + "; expires=" + g
			}
		}
	},
	getUinNum:function(f){
		var e = 0;
		if(f.charAt(0) == "o" || f.charAt(0) == "0"){
			e = e + 1;
			while (f.charAt(e) == "0"){
				e++
			}
			f = f.substr(e, f.length)
		}
		return f;
	},
	getUinInfo:function(){
		$.ajax({
			url: "Login/plogin?func=loginAll&refresh=0",
			dataType: "jsonp",
			jsonp: "loginAll",
			type: "get",
			cache: false,
			data: "uin=" + MGR.getUinNum(MGR.appcookie("uin")) + "&skey=" + MGR.appcookie("skey")
		})
	},
	checkLogin:function(){
		if(MGR.appcookie("uin")){
			return true;
		}else{
			return false;
		}			
	},
	titleStatus:function(a){
		var check = $("body").attr("check");
		if(encodeURIComponent(a.nick) != "undefined" && check != ""){
			MGR.Uname = MGR.htmlEncode(a.nick);
			$("#logined").show();
			$("#nologin").hide();
			var uid = MGR.getUinNum(MGR.appcookie("uin"));
			var img = '<img src="https://q4.qlogo.cn/g?b=qq&nk='+uid+'&s=40">';
			$("#userName .user_name").html(MGR.Uname);
			$("#userImg").html(img);
			//$("#login_nickname").html(MGR.htmlEncode(a.Uname));
			$("#login_nickname").html(img);
		}else{
			$("#nologin").show();
			//MGR.logout();
		}
	},
	init:function(){
		
		var d = document,
		expire = MGR.expires = new Date(( + new Date()) + 1 * 3600000),
		cookie = MGR.cookie = {expires:expire,path:"/",domain:window.document.location.host},
		nav = d.createElement("div"),
		ifrDiv = d.createElement("div"),
		initEvent=function(){
			
			if(MGR.checkLogin()){
				MGR.getUinInfo();
			}else{
				$("#nologin").show();
			}
			$("#logined").hover(function(){
				$("#userfold_frame").show();
			},function(){
				$("#userfold_frame").hide();
			});
			$("#changeaccouont").click(function(){
				MGR.loginout(true);
			})
			$("#changelogout").click(function(){
				MGR.loginout(false);
			})
		},
		initHeader=function(){
			
			ifrDiv.className = "loginframe";
			ifrDiv.id = "loginframe";
			ifrDiv.innerHTML = '<iframe name="login_ifr" id="login_ifr" frameborder="0" scrolling="no" width="100%" height="100%" src=""></iframe>';
			d.body.appendChild(ifrDiv);
		};
		initEvent();
		initHeader();
	},
	htmlEncode:function(sStr){
		sStr = sStr.replace(/&/g,"&amp;");
		sStr = sStr.replace(/>/g,"&gt;");
		sStr = sStr.replace(/</g,"&lt;");
		sStr = sStr.replace(/"/g,"&quot;");
		sStr = sStr.replace(/'/g,"&#39;");
		return sStr;
	},
	pageWidth:function() {
		return (document.documentElement && document.documentElement.scrollWidth) || document.body.scrollWidth;
	},
	showDiv:function(objid){
		showDialog.show({id:objid,bgcolor:"#000000",opacity:60});	
	}
}
function ptlogin2_onResize(a, b) {

    $("#loginframe").css({
        width: a + "px",
        height: b + "px",
        marginLeft : -a/2+ "px",
	    marginTop :-b/2+ "px"
    })
    
}
function ptlogin2_onClose() {
    showDialog.hide()
}
function loginAll(a){
	MGR.titleStatus(a);
}
function str2JSON(str) {
	eval('var __pt_json='+str);
	return __pt_json;
}
function ptlogin2_is_login()
{
	var user = $("body").attr("check");
	if(user != "" && user != null){
		return true;
	}else{
		return false;
	}
}
//初始化

MGR.init();

$(function(){

	if (typeof window.postMessage !== 'undefined') {
		window.onmessage = function(event) {
			var msg = event || window.event; // 兼容IE8
			var data;
			if (typeof JSON !== 'undefined') {
				
				data = JSON.parse(msg.data);
			}else {

				data = str2JSON(msg.data);
			}
			switch (data.action) {
				case 'close':
					ptlogin2_onClose();
				break;
				case 'resize':
					ptlogin2_onResize(data.width, data.height);
				break;
			}
		}
	}
})

$(document).ready(function(){
	$("#image2").bind("click",function(){
	    $("#orientation_tip").hide();
	});

	if (window.orientation == 0 || window.orientation == 180) {
		$("#orientation_tip").show();
	}
	
	$(window).bind('orientationchange',function(){
	    if (window.orientation == 0 || window.orientation == 180) {
	    	$("#orientation_tip").show();
	    }else{
	    	$("#orientation_tip").hide();
	    }
	});

});