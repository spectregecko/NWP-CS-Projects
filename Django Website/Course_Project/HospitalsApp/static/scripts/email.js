document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector("form");
    form.addEventListener("submit", function(e) {
        // Email validation.
        let email = document.querySelector('input[name="receiver"]');
        email.style.backgroundColor = "white";
        if (!(email.value).match(/^[a-zA-Z0-9][a-zA-Z0-9_\.]+[a-zA-Z0-9]@[a-zA-Z]+\.[a-zA-Z]{2,3}$/)) {
            e.preventDefault();
            alert("Please enter a valid email!");
            email.style.backgroundColor = "rgb(255, 175, 175)";
        }
    });
});