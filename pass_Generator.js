// This program is contributed by Gaurav Mandal

function generatePassword(length = 12, useLowercase = true, useUppercase = true, useDigits = true, useSpecialChars = true) {
    let characters = '';

    if (useLowercase) {
        characters += 'abcdefghijklmnopqrstuvwxyz';
    }
    if (useUppercase) {
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    }
    if (useDigits) {
        characters += '0123456789';
    }
    if (useSpecialChars) {
        characters += '!@#$%^&*()_-+=<>?';
    }

    if (!(useLowercase || useUppercase || useDigits || useSpecialChars)) {
        throw new Error("At least one character set (lowercase, uppercase, digits, special chars) must be selected.");
    }

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters.charAt(randomIndex);
    }

    return password;
}

// Example usage:
const password = generatePassword(16, true, true, true, true);
console.log(password);

// This code is contributed by Gaurav Mandall (https://www.linkedin.com/in/gauravmandall/)