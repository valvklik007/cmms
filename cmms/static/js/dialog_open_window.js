function openDialog(url) {
	let dialog = document.getElementById('dialog_open_option');
	let iframe = document.getElementById('dialogIframe');	
	iframe.src = url;  // Замените на нужный URL
	dialog.showModal();
}

function update_table() {
	url = `/add_option/modelitme/?id=${document.getElementById("manufactureritme").value}`;
	let response = fetch(url)
		.then(response => response.text())
		.then(html => {
			if (document.getElementById("modelitme")){
				lastText = document.getElementById("modelitme").innerText;
				console.log('123123123')
			}
		});
}

if (document.getElementById('modelitme')){
	update_table();
}


function closeDialog() {
	document.getElementById('dialog_open_option').close();
	document.getElementById('dialogIframe').src = '';

	if (document.getElementById("modelitme")){
		selectElement_new = document.getElementById("modelitme").innerText;
		if (selectElement_new !== lastText) {
			update_table();
	 }
	 
	}
	
}


window.addEventListener("message", (event) => {
	if (event.data === "closeDialog") {
			closeDialog();
	}
}, false);


function open_windows(data){
	window.open(
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
					lastText = document.getElementById("modelitme").innerText;
					// manufactureritme
					document.getElementById('manufactureritme').value = manufacturer;
				}, 100);
			}
		}
	});
}