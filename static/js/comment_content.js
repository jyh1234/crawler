window.onload = function(){
	var oLibrary = document.getElementsByTagName('h2')[0];
	var library = '';
	var comment_id = document.getElementById('comment_id');
	var catch_time = document.getElementById('catch_time');
	var comment_time = document.getElementById('comment_time');
	var catch_address = document.getElementById('catch_address');
	var comment_content = document.getElementById('comment_content');
	var sys_score = document.getElementById('sys_score');
	var arti_score = document.getElementById('arti_score');
	var current_url = window.location.href;
	var current_id = current_url.split('=')[1];
	if (oLibrary.innerHTML.search("低") != -1){
		library = "low";
	}
	else{
		library = "high";
	}

	$.ajax({    
	    url:'http://127.0.0.1:8000/function/comment_content/',// 跳转到 action
	    data:{
			comment_id:current_id,
			library:library,
	    },    
	    type:'post',    
	    cache:false,    
	    dataType:'json',    
	    success:function(data) {    
	        if(data.msg =="success" ){    
	            comment_id.innerHTML = data.dic[0].comment_id;
				catch_time.innerHTML = data.dic[0].catch_time;
				comment_time.innerHTML = data.dic[0].comment_time;
				catch_address.innerHTML = data.dic[0].catch_address;
				comment_content.innerHTML = data.dic[0].comment_content;
				sys_score.innerHTML = data.dic[0].sys_score;
				arti_score.innerHTML = data.dic[0].arti_score;
				var count=data.dic[0].manager;
				get_manager(count.length,count)
	        }else{    
	            comment_id.innerHTML = "获取失败";
	            catch_time.innerHTML = "获取失败";
	            comment_time.innerHTML = "获取失败";
	            catch_address.innerHTML = "获取失败";
	            sys_score.innerHTML = "获取失败";
				arti_score.innerHTML = "获取失败";
				comment_content.innerHTML = "获取失败";
	        }    
	     },    
	     error : function() {    
	          // view("异常！");    
	          alert("异常！");    
	     }    
	});
}

function get_manager(number,manager){
	var oSelect = document.getElementsByClassName('manage_people')[0];
	for (var i = 0 ; i < manager.length ; i++){
		var person = document.createElement('option');
		person.innerHTML = manager[i];
		oSelect.appendChild(person);
	}
}

function submit_newscore(){
	var new_score = document.getElementById('new_score');
	var current_id = document.getElementById('comment_id');
	var arti_score = document.getElementById('arti_score');
	$.ajax({
	    url:'http://127.0.0.1:8000/function/submit_newscore/',// 跳转到 action
	    data:{
			comment_current_id:current_id.innerHTML,
			new_score:new_score.value,
	    },    
	    type:'post',    
	    cache:false,    
	    dataType:'json',    
	    success:function(data) {    
	        if(data.msg =="success" ){    
	            alert('修改成功');
	            arti_score.innerHTML = new_score.value;
	        }else{    
	            alert('修改失败');
	        }    
	     },    
	     error : function() {    
	          // view("异常！");    
	          alert("异常！");    
	     }    
	});
}

function send_message(){
	var current_id = document.getElementById('comment_id');
	var managers = document.getElementById('manage_people');
	manager = managers.options[managers.selectedIndex].innerHTML;
	$.ajax({
	    url:'http://127.0.0.1:8000/function/send_message/',// 跳转到 action
	    data:{
			comment_current_id:current_id.innerHTML,
			manager:manager,
	    },    
	    type:'post',    
	    cache:false,    
	    dataType:'json',    
	    success:function(data) {    
	        if(data.msg =="success" ){    
	            alert('发送成功');
	        }else{    
	            alert('发送失败');
	        }    
	     },    
	     error : function() {    
	          // view("异常！");    
	          alert("异常！");    
	     }    
	});
}

function changeitems(btn){
	var oLibrary = document.getElementsByTagName('h2')[0];
	if (oLibrary.innerHTML.search("低") != -1){
		var library = "low";
	}
	else{
		var library = "high";
	}
	if (oLibrary.innerHTML.search("已") != -1){
		var process = "processed";
	}
	else{
		var process = "unprocessed";
	}
	if(btn.value == "上一条"){
		var target = "previous";
	}
	else{
		var target = "next";
	}


	var comment_id = document.getElementById('comment_id');
	var catch_time = document.getElementById('catch_time');
	var comment_time = document.getElementById('comment_time');
	var catch_address = document.getElementById('catch_address');
	var comment_content = document.getElementById('comment_content');
	var sys_score = document.getElementById('sys_score');
	var current_url = window.location.href;
	var current_id = current_url.split('=')[1];

	
	$.ajax({    
	    url:'http://127.0.0.1:8000/function/changeitems/',// 跳转到 action
	    data:{
			comment_current_id:current_id,
			library:library,
			target:target,
			process:process,
	    },    
	    type:'post',    
	    cache:false,    
	    dataType:'json',    
	    success:function(data) {
	    	console.log(data.msg);
	        if(data.msg == "index" ){
				window.location.href = ("http://127.0.0.1:8000/function/index/");
	        }else if(data.msg == "success"){
				window.location.replace('http://127.0.0.1:8000/function/comment_content_'+library+"_"+process+
					'/?comment_id=' + data.dic[0].comment_id);
	            comment_id.innerHTML = data.dic[0].comment_id;
				catch_time.innerHTML = data.dic[0].catch_time;
				comment_time.innerHTML = data.dic[0].comment_time;
				catch_address.innerHTML = data.dic[0].catch_address;
				comment_content.innerHTML = data.dic[0].comment_content;
				sys_score.innerHTML = data.dic[0].sys_score;
				var count=data.dic[0].manager;
				get_manager(count.length,count)
	        }else{
	        	comment_id.innerHTML = "获取失败";
	            catch_time.innerHTML = "获取失败";
	            comment_time.innerHTML = "获取失败";
	            catch_address.innerHTML = "获取失败";
	            sys_score.innerHTML = "获取失败";
	            comment_content.innerHTML = "获取失败";
			}
	     },    
	    error : function() {
	          // view("异常！");
	          alert("异常！");
	     }
	});
}