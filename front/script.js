const dropdown = document.getElementById('methodsDropdown');

function listMethods() {
    fetch('http://localhost:8000/list_methods')
        .then(response => response.json())
        .then(data => {
            // const dropdown = document.getElementById('methodsDropdown');
            data.methods.forEach(method => {
                const option = document.createElement('option');
                option.value = method;
                option.text = method;
                dropdown.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching methods:', error));
}
listMethods();

function requestScore() {
    const dropdown = document.getElementById('methodsDropdown');
    const score = document.getElementById('score');

    method = dropdown.value;
    fetch('http://localhost:8000/methods/' + method + '/score')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            score.innerText = data.data.score;
        })
        .catch(error => console.error('Error fetching score:', error));
}
