var adv = {};

document.addEventListener('DOMContentLoaded', function () {
    fetch('/getBestiary')
        .then(response => response.json())
        .then(data => {
            var container = document.getElementById('dropdown');

            data["data"].forEach(element => {
                var newElement = document.createElement('option')
                newElement.textContent = element
                newElement.value = element
                container.appendChild(newElement)
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

function submitForm() {
    document.getElementById("instBtn").disabled = true

    var data = document.getElementById('dropdown').value;

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'data=' + encodeURIComponent(data),
    })
        .then(response => response.text())
        .then(data => {
            var grid = document.getElementById("main-container");
            grid.innerHTML += data;
            document.getElementById("instBtn").disabled = false

        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("instBtn").disabled = false
        });
}

function rollDice(card_id, max) {

    var i = Math.floor(Math.random() * max) + 1;
    var card = document.getElementById(card_id);

    switch (adv[card_id]) {
        default:
        case undefined:
            card.children[0].children[2].children[1].children[2].textContent = `🎲 : ${i}`;
            break;
        case 2:
            var j = Math.floor(Math.random() * max) + 1;
            i = Math.max(i, j);
            card.children[0].children[2].children[1].children[2].textContent = `⏫🎲 : ${i}`;
            break;
        case -2:
            var j = Math.floor(Math.random() * max) + 1;
            i = Math.min(i, j);
            card.children[0].children[2].children[1].children[2].textContent = `⏬🎲 : ${i}`;
            break;

    }

    switch (i) {
        case 1:
            card.children[0].children[2].children[1].children[2].style.color = 'red';
            break;
        case max:
            card.children[0].children[2].children[1].children[2].style.color = 'green';
            break;
        default:
            card.children[0].children[2].children[1].children[2].style.color = 'lightgrey';
            break;
    }
}

function setAdv(card_id, i) {
    adv[card_id] = i
}
