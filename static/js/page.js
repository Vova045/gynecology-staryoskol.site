// Показ модуля спросить
const div = document.querySelectorAll('.ask_modal_content')[0];
document.querySelector('#ask_button').addEventListener('click', function () {
    div.style.display = 'flex';
})
var selection3 = document.querySelector('#ask_button2') !== null;
if (selection3) {
    document.querySelector('#ask_button2').addEventListener('click', function () {
        div.style.display = 'flex';
    })
}
document.querySelectorAll('.ask_modal_close')[0].addEventListener('click', function () {
    div.style.display = 'none';
})
// Показ модуля перезвонить
const div2 = document.querySelectorAll('.recall_content')[0];

document.querySelector('#recall_button').addEventListener('click', function () {
    div2.style.display = 'flex';
})
var selection = document.querySelector('#recall_button2') !== null;
if (selection) {
    document.querySelector('#recall_button2').addEventListener('click', function () {
        div2.style.display = 'flex';
    })
}
var selection2 = document.querySelector('#recall_button3') !== null;
if (selection2) {
    document.querySelector('#recall_button3').addEventListener('click', function () {
        div2.style.display = 'flex';
    })
}

document.querySelectorAll('.recall_close')[0].addEventListener('click', function () {
    div2.style.display = 'none';
})

if (document.querySelectorAll('.data_sent_content')[0]) {
    document.querySelectorAll('.data_sent_close')[0].addEventListener('click', function () {
        document.querySelectorAll('.data_sent_content')[0].style.display = 'none';
    })
}
