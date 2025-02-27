function openDialog(url) {
	let dialog = document.getElementById('dialog_open_option');
	let iframe = document.getElementById('dialogIframe');	
	iframe.src = url;  // Замените на нужный URL
	if (document.getElementById("dialog_open_option")){
		lastText = document.getElementById("modelitme").innerText;
	}
	
	dialog.showModal();
	
}

function update_table() {	
	url = `/add_option/modelitme/?id=${document.getElementById("manufactureritme").value}`;
	let response = fetch(url)
		.then(response => response.text())
		.then(html => {
			if (document.getElementById("modelitme")){
				if (document.getElementById('dialog_open_option')){
					options_value = document.getElementById("modelitme");
					// lastText.innerText;
					setTimeout(()=>{						
						for(let option of options_value.options){
							if(option.value == start_select){
								option.selected = true;				
								// start_select = document.getElementById('modelitme').value;
								break;
							}
						}}, 500)
				}
			}
		});
}

if (document.getElementById('modelitme')){
	start_select = document.getElementById('modelitme').value;
	// lastText = document.getElementById("modelitme").innerText;
	document.getElementById('modelitme').addEventListener("change", async function(){
		start_select = document.getElementById('modelitme').value;
	})
}


if (document.getElementById('modelitme')){
	update_table();
}


function closeDialog() {
	document.getElementById('dialog_open_option').close();
	document.getElementById('dialogIframe').src = '';

	if (document.getElementById("modelitme")){
		selectElement_new = document.getElementById("modelitme").innerText;
		update_table();
	// 	if (selectElement_new !== lastText) {
	// 		update_table();
	//  }
	 
	}
	
}


window.addEventListener("message", (event) => {
	start_select = document.getElementById('modelitme').value;
	if (event.data === "closeDialog") {
			closeDialog(start_select);
	}
}, false);


function open_windows(data){
	start_select = document.getElementById('modelitme').value;
	newWindow = window.open(
			data,
			'popUpWindow','height=510,width=900,left=10,top=10,scrollbars=yes,menubar=no')
	return false;
}


if (document.getElementById('manufactureritme')){
	document.getElementById("manufactureritme").addEventListener("change", async function() {
		var manufacturer = this.value;
		let req = await fetch(`/add_option/modelitme/?id=${manufacturer}`);
		if (req.ok){
			if(document.getElementById("modelitme")){
				setTimeout(()=>{
					// lastText = document.getElementById("modelitme").innerText;
					// manufactureritme
					document.getElementById('manufactureritme').value = manufacturer;
				}, 500);
			}
		}
	});
}