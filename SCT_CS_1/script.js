document.addEventListener('DOMContentLoaded', function() {
    const inputText = document.getElementById('inputText');
    const shiftValue = document.getElementById('shiftValue');
    const outputText = document.getElementById('outputText');
    const encryptBtn = document.getElementById('encryptBtn');
    const decryptBtn = document.getElementById('decryptBtn');

    let originalText = ''; // Stores the original text

    function cipher(text, shift, encrypt) {
        let result = '';
        for (let i = 0; i < text.length; i++) {
            let char = text[i];
            if (/[a-z]/i.test(char)) {
                const code = char.charCodeAt(0);
                const offset = code <= 90 ? 65 : 97;
                const direction = encrypt ? shift : -shift;
                result += String.fromCharCode(
                    ((code - offset + direction + 26) % 26) + offset
                );
            } else {
                result += char;
            }
        }
        return result;
    }

    encryptBtn.addEventListener('click', function() {
        originalText = inputText.value; // Store original text
        const shift = parseInt(shiftValue.value);
        
        if (originalText && shift >= 1 && shift <= 25) {
            outputText.value = cipher(originalText, shift, true);
        } else {
            alert('Please enter text and valid shift (1-25)');
        }
    });

    decryptBtn.addEventListener('click', function() {
        if (!originalText) {
            alert('Please encrypt text first');
            return;
        }
        
        const shift = parseInt(shiftValue.value);
        outputText.value = originalText; // Show the original stored text
    });
});