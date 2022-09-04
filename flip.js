const card = document.querySelector('.card');
const p = document.querySelector('.pulseDiv');

card.addEventListener('click', function() {
    card.classList.toggle('flipped');
    p.classList.toggle('unone');
    // window.alert("sometext");
});