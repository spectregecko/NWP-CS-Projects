// Disables validation if the back button is clicked.
let allowValidation = true;
function disableValidation() {
    allowValidation = false;
}

document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector("form");
    form.addEventListener("submit", function(e) {
        // Email validation.
        let email = document.querySelector('input[name="email"]');
        email.style.backgroundColor = "white";
        if (!(email.value).match(/^[a-zA-Z0-9][a-zA-Z0-9_\.]+[a-zA-Z0-9]@[a-zA-Z]+\.[a-zA-Z]{2,3}/) && allowValidation) {
            e.preventDefault();
            alert("Please enter a valid email!");
            email.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Password validation.
        let password = document.querySelector('input[name="password"]');
        let confirm = document.querySelector('input[name="confirm"]');
        password.style.backgroundColor = "white";
        confirm.style.backgroundColor = "white";
        if  ((password.value != confirm.value) && allowValidation) {
            e.preventDefault();
            alert("Passwords do not match!");
            confirm.style.backgroundColor = "rgb(255, 175, 175)";
        }
        else if (!(password.value).match(/^[0-9]?[a-zA-Z]+[0-9]?(-[0-9]?[a-zA-Z]+[0-9]?)+/) && allowValidation) {
            e.preventDefault();
            alert("Please enter a valid passphrase!\n\nA valid passphrase must have two or more words separated by a dash with an optional number at the start or end of the words.\n\nExample: Hello1-Thanos-4FunDay");
            password.style.backgroundColor = "rgb(255, 175, 175)";
            confirm.style.backgroundColor = "rgb(255, 175, 175)";
        }
    });
});