const navButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('nav-btns')[0]

navButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})