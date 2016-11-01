
//邮箱告知
function email() {
	var md5 = $("#md5").val();
	var fuid = $("#fuid").val();
	$.post("Email/email",{"md5":md5,"fuid":fuid},function(result){
			showDialog.show({id:"file_upload_fail",bgcolor:"#000000",opacity:60});
			$("#word_fail").html(result.info);

	},"json");
}

//上传成功查看详细结果
function showDetail(){
	var md5 = $("#md5").val();
	window.location.href = "file/historylist"; 
}