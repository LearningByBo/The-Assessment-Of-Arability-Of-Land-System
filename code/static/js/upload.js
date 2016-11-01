$(document).ready(function(){
	if(isLogin()){
		if(window.File && window.FileList && window.FileReader){
			$("#button-text").css("display","block");
      		$("#file_upload").bind("change",function(){
      			fileSelected($(this).get(0));
      		});
      		$("#file_upload2").bind("change",function(){
      			fileSelected($(this).get(0));
            });
        } else{
        	initUpload("file_upload",208,59,"");
        	initUpload("file_upload2",208,59,"");
        }
	}else{
		$(".upload_btn_index").html("<div id='file_upload-button' class='uploadify-button'><span class='uploadify-button-text'></span></div>");
		//$("#upload").html("<div id='file_upload-button' class='uploadify-button'><span class='uploadify-button-text'></span></div>");
		$(".uploadify-button").bind("click",function(){
			MGR.showLogin();
		})
	}
	$(".upload_detail_btn").bind("click",function(){
		$(this).next().show();
	});
	$(".tips_close").bind("click",function(){
		$(this).parent().parent().parent().hide();
	});
});


function switchSize(size)
{
	size = parseInt(size);
	var unit = size + "B";
	if(size > 1048576) {
		size = Math.round(size / 1048576);
		unit = size+"MB";
	}else if(size > 1024) {
		size = Math.round(size / 1024);
		unit = size+"KB";
	}
	return unit;
}


function isLogin()
{
	var user = $("#is_login").val();
	if(user != "" && user != null){
		return true;
	}else{
		return false;
	}
}

//定时器标志
var ti = null;

//h5的上传
function fileSelected(obj){
	var file = obj.files[0];
	if(file){
		var fileSize = 0;
		if (file.size > 1024 * 1024){
        	var size = Math.round(file.size*100/(1024*1024))/100;
            fileSize = (Math.round(file.size*100/(1024*1024))/100).toString() + 'MB';
        }else{
			fileSize = (Math.round(file.size*100/1024)/100).toString() + 'KB';
        }
		checkUpload(file.size,function(){
			var fd = new FormData();
			fd.append("fil", obj.files[0]);
			var xhr = new XMLHttpRequest();
			$("#h5-queue-item").find("[class='close']").bind("click",function(){
            	xhr.abort();
            });
			xhr.upload.addEventListener("progress", uploadProgress, false);
			xhr.addEventListener("load", uploadComplete, false);
			xhr.addEventListener("error", uploadFailed, false);
			xhr.addEventListener("abort", uploadCanceled, false);
			xhr.open("POST", "file/uploadfile");//请修改成自己的接口
			xhr.send(fd);
			var id = $("#h5Show")
			id.find("[id='fileName']").html("["+fileSize+"] "+file.name);
			id.attr("display","block");
			id.find("[class='data']").html("-上传中");
			showDialog.show({id:"h5Show",bgcolor:"#000000",opacity:60});
		});
      	/*if(errorCode == 0){
			var fd = new FormData();
			fd.append("fil", obj.files[0]);
			var xhr = new XMLHttpRequest();
			$("#h5-queue-item").find("[class='close']").bind("click",function(){
            	xhr.abort();
            });
			xhr.upload.addEventListener("progress", uploadProgress, false);
			xhr.addEventListener("load", uploadComplete, false);
			xhr.addEventListener("error", uploadFailed, false);
			xhr.addEventListener("abort", uploadCanceled, false);
			xhr.open("POST", "/file/uploadfile");//请修改成自己的接口
			xhr.send(fd);
			var id = $("#h5Show")
			id.find("[id='fileName']").html("["+fileSize+"] "+file.name);
			id.attr("display","block");
			id.find("[class='data']").html("-上传中");
			showDialog.show({id:"h5Show",bgcolor:"#000000",opacity:60});

        }*/
	}
}

	function uploadProgress(evt) {
        if (evt.lengthComputable) {
          var percentComplete = Math.round(evt.loaded * 100 / evt.total);
           $("#progressbar").css("width",percentComplete+ "%");
        }
      }

      function uploadComplete(evt) {
    	var data = evt["currentTarget"]["response"];
        //上传完成
        var id = $("#h5Show")
        id.find("[class='data']").html("-跳转中");
        var d = $.parseJSON(data);
        if(d.result != "success"){
        	
        	if(d.type == "html") {
        		showDialog.show({id:"file_upload_fail",bgcolor:"#000000",opacity:60});
        		$("#word_fail").html(d.info);
        		
        	}else {
        		showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
        		$("#check_word_fail").html(d.info);
        	}
        }else{
        	$("#file_upload-queue").find(".cancel").css("display","none");
        	//showDialog.show({id:"file_upload_suc",bgcolor:"#000000",opacity:60});
			ti = timeCount();
        	$("#md5").val(d.md5);
        	$("#fuid").val(d.fuid);
   	    	location.href = "file/showdetail?pk="+d.fuid
        }
      }


      function uploadFailed(evt) {
		//文件上传失败
		showDialog.hide();
		showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
        $("#check_word_fail").html("上传失败");
      }

      function uploadCanceled(evt) {
        showDialog.hide();
      }
function checkUpload(size,func)
{
	$.post("file/check",{"filesize":size},function(obj){
		switch(obj.status) {
			case 2:
				$("#upgrade_word").html("您当天分析文件总数超过"+obj.data+"份，如需分析更多文件，请升级为高级用户。");
				showDialog.show({id:"User_upgrade",bgcolor:"#000000",opacity:60});
				break;
			case 3:
				MGR.showLogin();
				break;
			case 4:
				$("#upgrade_word").html("您上传文件大小超过"+obj.data+"MB，如需分析更大的文件，请升级为高级用户。");
				showDialog.show({id:"User_upgrade",bgcolor:"#000000",opacity:60});
				break;
			case -1:
				showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
				$("#check_word_fail").html(obj.info);
				break;
			default:
				if(func != undefined && func !="") {
					func();
				}
				break;
		}
	},"json");
}
//flash的上传
function initUpload(obj,width,height,text){
	var CookieStr = document.cookie; 
	var arr = CookieStr.split(";");
	for(var i = 0;i<arr.length;i++){
		var str = arr[i].split("=")[0];
		if($.trim(str) == "skey"){
			var skey = arr[i].split("=")[1];
		}else if($.trim(str) == "uin"){
			var uin = arr[i].split("=")[1];
		}

	}
	$("#"+obj).uploadify({
		'swf'      : 'Assets/swf/uploadify.swf',
        'uploader' : 'file/uploadfile',
        'queueID'  : 'some_file_queue',
        'fileObjName' : 'fil',
		'buttonText' : "",
		'multi'    : false,
		'height'   : height,
        'width'    : width,
		'auto'     : false,
		"buttonText":text,
		'removeCompleted':false,
		'requeueErrors': false,
		'removeTimeout': 0,
		'formData' :{'skey':skey,'uin':uin},//传参
		'progressData':true,
		//'fileTypeExts' : '*.APK;*.EXE;*.DLL;*.SYS;*.RAR;*.ZIP;*.MSI',		
		'overrideEvents':['onSelectError'],
		'onFallback' : function() {
			showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
			$("#check_word_fail").html("未安装flash播放器或播放器版本不兼容");
			$("#upload_txt_div").html("漏洞检测");
        },
        'onSelect':function(file){
        	checkUpload(file.size,function(){
        		$("#"+obj).uploadify("upload");
        		var id = "some_file_queue";
            	$("#"+id).find("[class='fileName']").html("["+switchSize(file.size)+"] "+file.name);
            	$("#"+id).find("[class='data']").html("-上传中");
    			showDialog.show({id:id,bgcolor:"#000000",opacity:60});
    		});
        	return false;
		},
		"onDialogOpen":function(){
			var id = "some_file_queue";
			$("#"+id).html("");
			$("#"+id).css("z-index",999999);
		},
		'onCancel':function(file){
			$("#"+obj).uploadify('cancel', '*')
			showDialog.hide();
		},
		"onUploadError":function(file, errorCode, errorMsg, errorString){
			if(errorCode != "-280") {
				showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
				$("#check_word_fail").html("文件被使用中，请关闭后重新上传！");
			}
			
		},
		'onSelectError':function(file, errorCode, errorMsg){
			switch(errorCode){
				case -110:
					//showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
					//$("#check_word_fail").html("文件体积不能超过30M，请重新选择！");
                    break;
                case -120:
                	showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
    				$("#check_word_fail").html("文件访问权限受限或没有内容！");
                    break;
                case -130:
                	showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
    				$("#check_word_fail").html("您上传的文件类型不支持");
                    break;
                default:
                	showDialog.show({id:"check_fail",bgcolor:"#000000",opacity:60});
					$("#check_word_fail").html("上传失败");
                	break;
			}
		},
		'onUploadSuccess':function(file,data,response){
			var id = "some_file_queue";
			$("#"+id).find("[class='data']").html("-跳转中");
			var d = $.parseJSON(data);
			if(d.result != "success"){		
				showDialog.show({id:"file_upload_fail",bgcolor:"#000000",opacity:60});
				$("#word_fail").html(d.info);
			}else{
				$("#"+id).find(".cancel").css("display","none");
				//showDialog.show({id:"file_upload_suc",bgcolor:"#000000",opacity:60});
				ti = timeCount();
				$("#md5").val(d.md5);
				$("#fuid").val(d.fuid);
				location.href = "file/showdetail?pk="+d.fuid
			}
			}
	});
}