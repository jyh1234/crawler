window.onload = function(){
	var low_processed = document.getElementById('low_processed');
	var low_unprocessed = document.getElementById('low_unprocessed');
	var high_processed = document.getElementById('high_processed');
	var high_unprocessed = document.getElementById('high_unprocessed');
	var url = window.location.href;
	var userid = url.split("=")[1];
	$.ajax({    
	    url:'http://127.0.0.1:8000/function/count/',// 跳转到 action
	    data:{
			userid:userid,
	    },    
	    type:'post',    
	    cache:false,    
	    dataType:'json',    
	    success:function(data) {    
	        if(data.msg == "success"){       
	            low_processed.innerHTML = data.low_processed;
				low_unprocessed.innerHTML = data.low_unprocessed;
				high_processed.innerHTML = data.high_processed;
				high_unprocessed.innerHTML = data.high_unprocessed;
	        }else if(data.msg == "failure") {    
	            low_processed.innerHTML = "加载失败";
	            low_unprocessed.innerHTML = "加载失败";
	            high_processed.innerHTML = "加载失败";
	            high_unprocessed.innerHTML = "加载失败";  
	        }    
	     },    
	     error : function() {       
	          alert("异常！");    
	     }    
	}); 
}

function save_train(){
	var info = document.getElementById('info_display');
	$.ajax({
	    url:'http://127.0.0.1:8000/function/save_train/',// 跳转到 action
	    data:{
			msg:"save_and_train",
	    },
	    type:'post',
	    cache:false,
	    dataType:'json',
	    success:function(data) {
	        if(data.msg == "success"){
	            info.innerHTML = "数据已保存并训练!";
	        }
			else {
	            info.innerHTML = "操作失败";
	        }
	     },
	     error : function() {
	          alert("异常！");
	     }
	});
}

function rejudge(){
	var info = document.getElementById('info_display');
	$.ajax({
	    url:'http://127.0.0.1:8000/function/sys_all/',// 跳转到 action
	    data:{
			msg:"rejudge",
	    },
	    type:'post',
	    cache:false,
	    dataType:'json',
	    success:function(data) {
	        if(data.msg == "success"){
	            info.innerHTML = "系统重新已打分!";
	        }
			else {
	            info.innerHTML = "操作失败";
	        }
	     },
	     error : function() {
	          alert("异常！");
	     }
	});
}

function show_accuracy(){
	var info = document.getElementById('info_display');
	$.ajax({
	    url:'http://127.0.0.1:8000/function/precision/',// 跳转到 action
	    data:{
			msg:"accuracy",
	    },
	    type:'post',
	    cache:false,
	    dataType:'json',
	    success:function(data) {
	        if(data.msg == "success"){
	            info.innerHTML = data.accuracy;
	        }
			else {
	            info.innerHTML = "操作失败";
	        }
	     },
	     error : function() {
	          alert("异常！");
	     }
	});
}