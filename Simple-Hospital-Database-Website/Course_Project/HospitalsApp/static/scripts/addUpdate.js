document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector("form");
    form.addEventListener("submit", function(e) {
        // Zip code validation.
        let zip_code = document.querySelector('input[name="zip_code"]');
        zip_code.style.backgroundColor = "white";
        if (!(zip_code.value).match(/^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d$/i) && !(zip_code.value).match(/^[0-9]{5}(?:[ -]?[0-9]{4})?$/)) {
            e.preventDefault();
            alert("Please enter a valid zip code!");
            zip_code.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Phone validation.
        let phone = document.querySelector('input[name="phone"]');
        phone.style.backgroundColor = "white";
        if (!(phone.value).match(/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/)) {
            e.preventDefault();
            alert("Please enter a valid phone number!");
            phone.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Type validation.
        let myType = document.querySelector('input[name="type"]');
        myType.style.backgroundColor = "white";
        if (myType.value.toUpperCase() != "PUBLIC" && myType.value.toUpperCase() != "PRIVATE" && myType.value.toUpperCase() != "NONPROFIT") {
            e.preventDefault();
            alert("Please enter a hospital type!");
            myType.style.backgroundColor = "rgb(255, 175, 175)";
        }

        // Email validation.
        let email = document.querySelector('input[name="email"]');
        email.style.backgroundColor = "white";
        if (!(email.value).match(/^[a-zA-Z0-9][a-zA-Z0-9_\.]+[a-zA-Z0-9]@[a-zA-Z]+\.[a-zA-Z]{2,3}$/)) {
            e.preventDefault();
            alert("Please enter a valid email!");
            email.style.backgroundColor = "rgb(255, 175, 175)";
        }
    });
});