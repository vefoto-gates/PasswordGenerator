document.addEventListener("DOMContentLoaded", function () {
    const generateButton = document.getElementById("generate-btn");
    generateButton.addEventListener("click", generatePassword);

    function generatePassword() {
        const length = document.getElementById("password-length").value;
        const useSpecialChars = document.getElementById("use-special-chars").checked;
        const memorable = document.getElementById("memorable").checked;

        // Your password generation logic here

        const passwordResult = document.getElementById("password-result");
        passwordResult.textContent = "Generated Password: [Your Generated Password]";
    }
});
