document.getElementById('passwordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const length = document.getElementById('length').value;
    const uppercase = document.querySelector('input[name="uppercase"]').checked;
    const lowercase = document.querySelector('input[name="lowercase"]').checked;
    const numbers = document.querySelector('input[name="numbers"]').checked;
    const symbols = document.querySelector('input[name="symbols"]').checked;

    fetch('/generate-password', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({length, uppercase, lowercase, numbers, symbols})
    })
    .then(response => response.json())
    .then(data => {
        const display = document.getElementById('passwordDisplay');
        if (data.password) {
            display.textContent = data.password;
        } else {
            display.textContent = 'Error: ' + data.error;
        }
    })
    .catch(error => console.error('Error:', error));
});
