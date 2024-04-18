BACKEND_URL = "http://localhost"
BACKEND_PORT = 8000

const dropdown = document.getElementById('methodsDropdown');
const score = document.getElementById('score');

function listMethods() {
    console.log("Listing methods...");

    fetch(`${BACKEND_URL}:${BACKEND_PORT}/list_methods`)
        .then(response => response.json())
        .then(data => {
            data.methods.forEach(method => {
                const option = document.createElement('option');
                option.value = method;
                option.text = method;
                dropdown.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching methods:', error);
            score.innerText = "Can't fetch methods"
        });
}
listMethods();

function requestScore() {

    method = dropdown.value;
    fetch(`${BACKEND_URL}:${BACKEND_PORT}/methods/${method}/score`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            score.innerText = data.data.score;
        })
        .catch(error => console.error('Error fetching score:', error));
}
