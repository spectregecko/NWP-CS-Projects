document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector('form[action="insertRecord.php"], form[action="updateRecord.php"]');
    form.addEventListener("submit", function(e) {
        // Item ID validation. Not really necessary as the validation is taken care in HTML.
        let ItemID = document.querySelector('input[name="ItemID"]');
        if (Number(ItemID.value) < 1 || Number(ItemID.value > 127)) {
            e.preventDefault();
            alert("Please enter a number within the range of 1 and 127 inclusive!");
        }

        // Price validation. Not really necessary as the validation is taken care in HTML.
        let Price = document.querySelector('input[name="Price"]');
        if (Number(Price.value) < 0 || Number(Price.value) > 999.99) {
            e.preventDefault();
            alert("Please enter a price that is less than $1000!");
        }

        // Units In Stock validation. Not really necessary as the validation is taken care in HTML.
        let UnitsInStock = document.querySelector('input[name="UnitsInStock"]');
        if (Number(UnitsInStock.value) < 0 || Number(UnitsInStock.value) > 32767) {
            e.preventDefault();
            alert("Please enter a smaller units in stock value!");
        }
    });
});