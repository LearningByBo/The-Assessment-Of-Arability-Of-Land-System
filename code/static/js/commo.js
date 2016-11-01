//上传成功倒计时

function timeCount(){
	var ti = null;
	var count = 120;
	$("#word_suc").append("<p class='countDown'><span id='countDown'>120</span>秒后窗口自动关闭...<span id='divProgressbar'></span></p>");
	
	//进度条
	$("#divProgressbar").progressbar({value: 0});
	ti = setInterval(function(){
		count--;
		$("#countDown").html(count);
		if(count < 0 ){
			clearInterval(ti);
			showDialog.hide();
			$("p[class='countDown']").remove();
			window.location.href = "file/historylist"
		}
		var newValue = $("#divProgressbar").progressbar("option", "value") + 5/6;
		$("#divProgressbar").progressbar("option", "value", newValue);
	}, 1000);
	return ti;
}
