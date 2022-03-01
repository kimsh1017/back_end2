'use strict';

const toggleBtn = document.querySelector('.header .logoAndTitle .bar');
const toggleMenu = document.querySelector('.header .menu');

toggleBtn.addEventListener('click', () => {
    toggleMenu.classList.toggle('active');
    toggleBtn.classList.toggle('active');
});