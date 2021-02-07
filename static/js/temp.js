let defender = document.getElementById('defender')

document.querySelector('form.battle').addEventListener('submit', function (e) {

    //prevent the normal submission of the form
    e.preventDefault();

    console.log(defender.value);
});

console.log(ship.power)