function enableEditing() {
    const formElements = document.querySelectorAll('#userForm input, #userForm select, #userForm textarea');
    formElements.forEach(element => {
        element.disabled = false;
    });
    document.querySelector('.edit-button').style.display = 'none';
    document.querySelector('.cancel-button').style.display = 'inline-block';
    document.querySelector('.delete-button').style.display = 'inline-block';
    document.querySelector('.save-button').style.display = 'inline-block';
}
