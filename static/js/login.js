// Mostrar senha
document.getElementById('show-password').addEventListener('change', function () {
    const passwordField = document.getElementById('password');

    // Checa se o checkbox de mostrar senha está marcado
    if (this.checked) {
        passwordField.type = 'text';
    } else {
        passwordField.type = 'password';
    }
});
