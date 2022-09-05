const card = document.querySelector('.card');
const front = document.querySelector('.front');
const back = document.querySelector('.backimg');
const p = document.querySelector('.pulseDiv');
const b = document.querySelector('.body');
const l = document.querySelector('.linkSection');

// card.addEventListener('click', function() {
//     card.classList.toggle('flipped');
//     p.classList.toggle('unone');
//     b.classList.toggle('scroll');
//     l.classList.toggle("show");
//     // window.alert("sometext");
// });

front.addEventListener('click', function() {
    card.classList.toggle('flipped');
    p.classList.toggle('unone');
    b.classList.toggle('scroll');
    l.classList.toggle("show");
    // window.alert("sometext");
});
back.addEventListener('click', function() {
    card.classList.toggle('flipped');
    p.classList.toggle('unone');
    b.classList.toggle('scroll');
    l.classList.toggle("show");
    // window.alert("sometext");
});

const pay = document.querySelector('.pay');
const payDiv = document.querySelector('.payDiv');
pay.addEventListener('click', function() {
    payDiv.classList.toggle('expanded');
    pay.classList.toggle("less")
});