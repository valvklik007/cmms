function changeFormHandler(id, id_but) {
	const form = document.getElementById(id);
	console.log(form.checkValidity());
	if (form.checkValidity()) {
		formSubmit(form, id_but);
		form.reset();
	}
};


function formSubmit(form, id_but) {
	// formElement = document.getElementById(formId);
	
	var url = form.getAttribute('action');
	var request = new XMLHttpRequest();
	request.open('POST', url, true);
	// request.onload = function() { // request successful
	// // we can use server response to our request now
	// };

	// request.onerror = function() {
	// 	// request failed
	// };

	but = document.getElementById(id_but);
	// console.log(but.getAttribute('name'), but.getAttribute('value'));
	
	form_new = new FormData(form);
	form_new.append(but.getAttribute('name'), but.getAttribute('value'));
	// parent = document.getElementById('parent');
	if (document.getElementById('parent')){
		new FormData(document.getElementById('parent')).forEach((value, key) => {
			form_new.append(key, value);
		});
	}
		

	request.send(form_new); // create FormData from form that triggered event
	// event.preventDefault();
}