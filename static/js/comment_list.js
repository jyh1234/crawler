window.onload = function(){
	var oLibrary = document.getElementsByTagName('h3')[0].innerHTML;
	library_process = oLibrary.split('-');
	var library = '';
	var processed = '';
	var page_current = document.getElementById('page_current');
	if (library_process[0] === '低分库'){
		library = 'low';
	}
	else{
		library = 'high';
	}
	if (library_process[1] === '已处理'){
		processed = 'processed';
	}
	else{
		processed = 'unprocessed';
	}


	$.ajax({
	    url:'http://127.0.0.1:8000/function/comment_list/',// 跳转到 action
	    data:{
			library:library,
			process:processed,
			page_current:parseInt(page_current.innerHTML),
			itemperpage:10,
	    },
	    type:'post',
	    cache:false,
	    dataType:'json',
	    success:function(data) {
	        if(data.msg ==="success" ){
	            var page_all = document.getElementById('page_all');
				page_all.innerHTML = data.pages;
				draw_list(10,data.items);
	        }else{
	            alert("加载失败");
	        }
	     },
	     error : function() {
	          // view("异常！");
	          alert("异常！");
	     }
	});
}


function draw_list(num,comment){
	var oLibrary = document.getElementsByTagName('h3')[0].innerHTML;
	library_process = oLibrary.split('-');
	var library = '';
	if (library_process[0] === '低分库'){
		library = 'low';
	}
	else{
		library = 'high';
	}
	var count = 0;
	var oComment = document.getElementsByClassName('comment_list')[0];
	oComment.innerHTML = '';
	for(count=0;count<num;count++){
		var new_row = document.createElement('tr');
		var id = document.createElement('td');
		id.className = 'id';
		var catch_time = document.createElement('td');
		catch_time.className = 'catch_time';
		var comment_time = document.createElement('td');
		comment_time.className = 'comment_time';
		var score = document.createElement('td');
		score.className = 'score';
		var operation = document.createElement('td');
		var btn = document.createElement('input');
		btn.type = 'button';
		btn.onclick = function(){
			var comment_current_id = this.parentNode.parentNode.children[0].innerText;
			console.log('ccid',comment_current_id);
			$.ajax({    
				url:'http://127.0.0.1:8000/function/count1/',// 跳转到 action
				data:{
					comment_id:comment_current_id,
				},
				type:'post',    
				cache:false,    
				dataType:'json',    
				success:function(data) {
					if(data.msg ==="success" ){
						var comment_id = data.comment_id;
						if(data.library === "low"){
							window.location.href = "http://127.0.0.1:8000/function/comment_content_"+data.library+"_"+
								data.process+"/" + "?comment_id=" + comment_id;
						}
						else{
							window.location.href = "http://127.0.0.1:8000/function/comment_content_"+data.library+"_"+
								data.process+"/" + "?comment_id=" + comment_id;
						}
					}
				},    
				error:function() {      
					alert("异常",comment_current_id);
				}    
			});
		};
		id.innerHTML = comment[count].id;
		catch_time.innerHTML = comment[count].catch_time;
		comment_time.innerHTML = comment[count].comment_time;
		score.innerHTML = comment[count].final_score;
		btn.value = '查看';
		operation.appendChild(btn);
		new_row.appendChild(id);
		new_row.appendChild(catch_time);
		new_row.appendChild(comment_time);
		new_row.appendChild(score);
		new_row.appendChild(operation);
		oComment.appendChild(new_row)
	}
}

function page_up(){
	var oLibrary = document.getElementsByTagName('h3')[0].innerHTML;
	library_process = oLibrary.split('-');
	var library = '';
	var processed = '';
	var page_current = document.getElementById('page_current');
	if (library_process[0] === '低分库'){
		library = 'low';
	}
	else{
		library = 'high';
	}
	if (library_process[1] === '已处理'){
		processed = 'processed';
	}
	else{
		processed = 'unprocessed';
	}
	x = parseInt(page_current.innerHTML);
	if (x>1){
		x -= 1;
		page_current.innerHTML = x;
		$.ajax({    
		    url:'http://127.0.0.1:8000/function/comment_list/',// 跳转到 action
		    data:{
				library:library,
				process:processed,
				page_current:parseInt(page_current.innerHTML),
				itemperpage:10,
		    },    
		    type:'post',    
		    cache:false,    
		    dataType:'json',    
		    success:function(data) {    
		        if(data.msg ==="success" ){
		            var page_all = document.getElementById('page_all');
		        	page_all.innerHTML = data.pages;
		        	draw_list(10,data.items);
		        }else{    
		            alert("加载失败");
		        }   
		     },    
		     error:function() {    
		          // view("异常！");    
		          alert("异常！");    
		     }    
		}); 
	}
	else{
		this.disabled = true;
	}
}

function page_down(){
	var oLibrary = document.getElementsByTagName('h3')[0].innerHTML;
	library_process = oLibrary.split('-');
	var library = '';
	var processed = '';
	var page_current = document.getElementById('page_current');
	var page_all = parseInt(document.getElementById('page_all').innerHTML);
	if (library_process[0] === '低分库'){
		library = 'low';
	}
	else{
		library = 'high';
	}
	if (library_process[1] === '已处理'){
		processed = 'processed';
	}
	else{
		processed = 'unprocessed';
	}
	x = parseInt(page_current.innerHTML);
	if(x<page_all){
		x += 1;
		page_current.innerHTML = x;
		$.ajax({    
		    url:'http://127.0.0.1:8000/function/comment_list/',// 跳转到 action
		    data:{
				library:library,
				process:processed,
				page_current:parseInt(page_current.innerHTML),
				itemperpage:10,
		    },
		    type:'post',    
		    cache:false,    
		    dataType:'json',    
		    success:function(data) {    
		        if(data.msg ==="success" ){
		            var page_all = document.getElementById('page_all');
					page_all.innerHTML = data.pages;
					draw_list(10,data.items);
		        }else{    
		            alert("加载失败");
		        }    
		     },    
		     error : function() {    
		          // view("异常！");    
		          alert("异常！");    
		     }    
		}); 
	}
	else{
		this.disabled = true
	}
}