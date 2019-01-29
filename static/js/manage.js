window.onload = function(){
	var sum = 8;
	draw_table(sum);
}
function search(){
	var sum = '调接口获得数据';
	var sum = 1;
	document.getElementById('manage_content').innerHTML='';
	draw_table(sum);
}
function reset(){
	var sum = '调接口';
	var sum = 8;
	document.getElementById('manage_content').innerHTML='';
	draw_table(sum);
}

function draw_table(rows){
	var count = 0;
	var oContent = document.getElementById('manage_content');
	for(count=0;count<rows;count++){
		var new_row = document.createElement('tr');
		
		var new_n = document.createElement('td');
		var new_name = document.createElement('input');
		new_name.type = 'text';
		new_name.className = 'name';
		new_name.id = count + 'name';
		new_name.disabled = 'disabled';
		new_n.appendChild(new_name);
		
		var new_t = document.createElement('td');
		var new_tel = document.createElement('input');
		new_tel.type = 'tel';
		new_tel.className = 'tel';
		new_tel.id = count + 'tel';
		new_tel.disabled = 'disabled';
		new_t.appendChild(new_tel);
		
		var new_operation = document.createElement('td');
		
		var new_modify = document.createElement('input');
		new_modify.className = 'modify';
		new_modify.type = 'button';
		new_modify.value = '修改';
		new_modify.id = count + 'modify';
		
		new_modify.onclick = function(){
			var id_name = parseInt(this.id) + 'name';
			var id_tel = parseInt(this.id) + 'tel';
			var oName = document.getElementById(id_name);
			var oTel = document.getElementById(id_tel);
			if (this.value == "修改"){
				oName.style.backgroundColor = "white";
				oName.style.border = "1px solid gray"
				oName.disabled = false;
				oTel.style.backgroundColor = "white";
				oTel.style.border = "1px solid gray"
				oTel.disabled = false;
				this.value = "保存";
			}
			else{
				oName.style.backgroundColor = "transparent";
				oName.style.border = "none"
				oName.disabled = true;
				oTel.style.backgroundColor = "transparent";
				oTel.style.border = "none"
				oTel.disabled = true;
				this.value = "修改";
			}
		};
		
		var new_delete = document.createElement('input');
		new_delete.className = 'delete';
		new_delete.type = 'button';
		new_delete.value = '删除';
		new_delete.id = count + 'delete';
		new_delete.onclick = function(){
			this.parentNode.parentNode.remove();
		}
		
		new_operation.appendChild(new_modify);
		new_operation.appendChild(new_delete);
		
		new_name.value = 'haha';
		new_tel.value = '18874769035';
		
		new_row.appendChild(new_n);
		new_row.appendChild(new_t);
		new_row.appendChild(new_operation)
		oContent.appendChild(new_row);
		
		if (count%2 == 0){
			new_row.className = 'even';
		}
		else{
			new_row.className = 'odd';
		}
	}
}