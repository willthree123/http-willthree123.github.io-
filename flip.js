const card = document.querySelector('.card');
const p = document.querySelector('.pulseDiv');
const b = document.querySelector('.body');

card.addEventListener('click', function() {
    card.classList.toggle('flipped');
    p.classList.toggle('unone');
    b.classList.toggle('scroll');
    // window.alert("sometext");
});