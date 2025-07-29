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

        // Password validation.
        let password = document.querySelector('input[name="password"]');
        password.style.backgroundColor = "white";
        if (!(password.value).match(/^[A-Za-z\d@$!%*#?&-]{8,}$/)) {
            e.preventDefault();
            alert("Please enter a valid password!");
            password.style.backgroundColor = "rgb(255, 175, 175)";
        }
    });
});