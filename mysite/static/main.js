'use strict';

const toggleBtn = document.querySelector('.header .logoAndTitle .bar');
const toggleMenu = document.querySelector('.header .menu');

toggleBtn.addEventListener('click', () => {
    toggleMenu.classList.toggle('active');
    toggleBtn.classList.toggle('active');
});


/* image_change */
let active_img = 1;

const main_image = document.querySelector('.main_image .moving_image');
const image_button1 = document.querySelector('.main_image .image_bar .first');
const image_button2 = document.querySelector('.main_image .image_bar .second');
const image_button3 = document.querySelector('.main_image .image_bar .third');

const changeImage = function(image_id) {
    main_image.src = image_id;
}

function changeImage1(){
    changeImage("/static/image/test_1.png")
    image_button1.classList.toggle('active');

    if (active_img == 2){
        image_button2.classList.toggle('active');
    }
    else if(active_img == 3){
        image_button3.classList.toggle('active');
    }
    active_img = 1;
    setTimeout(()=> changeImage2() , 3000);
}

function changeImage2() {
    changeImage("/static/image/test_2.png")
    image_button2.classList.toggle('active');

    if (active_img == 1){
        image_button1.classList.toggle('active');
    }
    else if(active_img == 3){
        image_button3.classList.toggle('active');
    }
    active_img = 2;
    setTimeout(()=> changeImage3() , 3000);
}


function changeImage3() {
    changeImage("/static/image/test_3.png")
    image_button3.classList.toggle('active');

    if (active_img == 1){
        image_button1.classList.toggle('active');
    }
    else if(active_img == 2){
        image_button2.classList.toggle('active');
    }
    active_img = 3;
    setTimeout(()=> changeImage1() , 3000);
}

changeImage1();



//http://127.0.0.1:8000/static/image/everyone_1.png ok
//http://127.0.0.1:8000/mysite/static/image/everyone_1.png no


