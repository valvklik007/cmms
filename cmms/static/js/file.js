file = document.getElementById('drop_file')
field  = document.querySelector('body')

field.addEventListener('dragover', (e) => {
    e.preventDefault();
    file.style.display = 'block';
});

file.addEventListener('dragleave', (e) => {
    e.preventDefault();
    file.style.display = 'none';
});

file.addEventListener('drop', e =>{
    e.preventDefault();
    file.style.display = 'none'
    document.getElementById('file').files = e.dataTransfer.files;
})