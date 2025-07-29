document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector("form");
    form.addEventListener("submit", function(e) {
        let search_filter = document.querySelector('select[name="searchFilter"]');
        let search_field = document.querySelector('input[name="response"]');
        search_field.style.backgroundColor = "white";

        // Type validation.
        if (search_filter.value === "type") {
            if (search_field.value.toUpperCase() != "PUBLIC" && search_field.value.toUpperCase() != "PRIVATE" && search_field.value.toUpperCase() != "NONPROFIT") {
                e.preventDefault();
                alert("Please enter a valid hospital type!\n\nValid hospital types are Public, Private, and Nonprofit.");
                search_field.style.backgroundColor = "rgb(255, 175, 175)";
            }
        }
    });

    let search_filter = document.querySelector('select[name="searchFilter"]');
    search_filter.addEventListener("change", function(e) {
        let search_field = document.querySelector('input[name="response"]');

        if (search_filter.value === "name") {
            search_field.placeholder = "Enter Name";
            search_field.maxLength = 100;
            search_field.value = "";
        }

        if (search_filter.value === "zipcode") {
            search_field.placeholder = "Enter Zip Code";
            search_field.maxLength = 10;
            search_field.value = "";
        }

        if (search_filter.value === "phone") {
            search_field.placeholder = "Enter Phone";
            search_field.maxLength = 14;
            search_field.value = "";
        }

        if (search_filter.value === "type") {
            search_field.placeholder = "Enter Type";
            search_field.maxLength = 9;
            search_field.value = "";
        }

        if (search_filter.value === "email") {
            search_field.placeholder = "Enter Email";
            search_field.maxLength = 50;
            search_field.value = "";
        }
    });
});