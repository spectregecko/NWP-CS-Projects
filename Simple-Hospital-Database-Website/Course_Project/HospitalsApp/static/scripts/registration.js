document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector("form");
    form.addEventListener("submit", function(e) {
        // Username validation.
        let username = document.querySelector('input[name="username"]');
        username.style.backgroundColor = "white";
        if (!(username.value).match(/^[a-zA-Z0-9@.+-_]+$/)) {
            e.preventDefault();
            alert("Please enter a valid username!");
            username.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // First name validation.
        let first_name = document.querySelector('input[name="first_name"]');
        first_name.style.backgroundColor = "white";
        if (!(first_name.value).match(/^[a-z]+$/i) && first_name.value) {
            e.preventDefault();
            alert("Please enter a valid alphabetic name!");
            first_name.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Last name validation.
        let last_name = document.querySelector('input[name="last_name"]');
        last_name.style.backgroundColor = "white";
        if (!(last_name.value).match(/^[a-z]+$/i) && last_name.value) {
            e.preventDefault();
            alert("Please enter a valid alphabetic name!");
            last_name.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Email validation.
        let email = document.querySelector('input[name="email"]');
        email.style.backgroundColor = "white";
        if (!(email.value).match(/^[a-zA-Z0-9][a-zA-Z0-9_\.]+[a-zA-Z0-9]@[a-zA-Z]+\.[a-zA-Z]{2,3}$/) && email.value) {
            e.preventDefault();
            alert("Please enter a valid email!");
            email.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Password validation.
        let password1 = document.querySelector('input[name="password1"]');
        let password2 = document.querySelector('input[name="password2"]');
        password1.style.backgroundColor = "white";
        password2.style.backgroundColor = "white";
        if  (password1.value != password2.value) {
            e.preventDefault();
            alert("Passwords do not match!");
            password2.style.backgroundColor = "rgb(255, 175, 175)";
        }
        else if (!(password1.value).match(/^[A-Za-z\d@$!%*#?&-]{8,}$/)) {
            e.preventDefault();
            alert("Please enter a valid password!");
            password1.style.backgroundColor = "rgb(255, 175, 175)";
            password2.style.backgroundColor = "rgb(255, 175, 175)";
        }
    });
});