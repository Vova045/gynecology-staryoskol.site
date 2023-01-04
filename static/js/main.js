// Показ модуля спросить
const div = document.querySelectorAll('.ask_modal_content')[0];

document.querySelectorAll('.ask_button')[0].addEventListener('click', function () {
    div.style.display = 'flex';
})
document.querySelectorAll('.ask_modal_close')[0].addEventListener('click', function () {
    div.style.display = 'none';
})
// Показ модуля перезвонить
const div2 = document.querySelectorAll('.recall_content')[0];

document.querySelectorAll('.recall_button')[0].addEventListener('click', function () {
    div2.style.display = 'flex';
})
document.querySelectorAll('.recall_button')[1].addEventListener('click', function () {
    div2.style.display = 'flex';
})
document.querySelectorAll('.recall_button')[2].addEventListener('click', function () {
    div2.style.display = 'flex';
})
document.querySelectorAll('.recall_close')[0].addEventListener('click', function () {
    div2.style.display = 'none';
})
// Раскрытие списка вопросов и ответов
const answer = document.querySelectorAll('.answer')[0];
const answer_plus = document.querySelectorAll('.plus')[0];
const answer_minus = document.querySelectorAll('.minus')[0];

document.querySelectorAll('.plus')[0].addEventListener('click', function () {
    answer.style.display = 'flex';
    answer_plus.style.display = 'none';
    answer_minus.style.display = 'flex';
})
document.querySelectorAll('.minus')[0].addEventListener('click', function () {
    answer.style.display = 'none';
    answer_plus.style.display = 'flex';
    answer_minus.style.display = 'none';
})
const answer1 = document.querySelectorAll('.answer')[1];
const answer_plus1 = document.querySelectorAll('.plus')[1];
const answer_minus1 = document.querySelectorAll('.minus')[1];

document.querySelectorAll('.plus')[1].addEventListener('click', function () {
    answer1.style.display = 'flex';
    answer_plus1.style.display = 'none';
    answer_minus1.style.display = 'flex';
})
document.querySelectorAll('.minus')[1].addEventListener('click', function () {
    answer1.style.display = 'none';
    answer_plus1.style.display = 'flex';
    answer_minus1.style.display = 'none';
})
const answer2 = document.querySelectorAll('.answer')[2];
const answer_plus2 = document.querySelectorAll('.plus')[2];
const answer_minus2 = document.querySelectorAll('.minus')[2];

document.querySelectorAll('.plus')[2].addEventListener('click', function () {
    answer2.style.display = 'flex';
    answer_plus2.style.display = 'none';
    answer_minus2.style.display = 'flex';
})
document.querySelectorAll('.minus')[2].addEventListener('click', function () {
    answer2.style.display = 'none';
    answer_plus2.style.display = 'flex';
    answer_minus2.style.display = 'none';
})
const answer3 = document.querySelectorAll('.answer')[3];
const answer_plus3 = document.querySelectorAll('.plus')[3];
const answer_minus3 = document.querySelectorAll('.minus')[3];

document.querySelectorAll('.plus')[3].addEventListener('click', function () {
    answer3.style.display = 'flex';
    answer_plus3.style.display = 'none';
    answer_minus3.style.display = 'flex';
})
document.querySelectorAll('.minus')[3].addEventListener('click', function () {
    answer3.style.display = 'none';
    answer_plus3.style.display = 'flex';
    answer_minus3.style.display = 'none';
})
const answer4 = document.querySelectorAll('.answer')[4];
const answer_plus4 = document.querySelectorAll('.plus')[4];
const answer_minus4 = document.querySelectorAll('.minus')[4];

document.querySelectorAll('.plus')[4].addEventListener('click', function () {
    answer4.style.display = 'flex';
    answer_plus4.style.display = 'none';
    answer_minus4.style.display = 'flex';
})
document.querySelectorAll('.minus')[4].addEventListener('click', function () {
    answer4.style.display = 'none';
    answer_plus4.style.display = 'flex';
    answer_minus4.style.display = 'none';
})
const answer5 = document.querySelectorAll('.answer')[5];
const answer_plus5 = document.querySelectorAll('.plus')[5];
const answer_minus5 = document.querySelectorAll('.minus')[5];

document.querySelectorAll('.plus')[5].addEventListener('click', function () {
    answer5.style.display = 'flex';
    answer_plus5.style.display = 'none';
    answer_minus5.style.display = 'flex';
})
document.querySelectorAll('.minus')[5].addEventListener('click', function () {
    answer5.style.display = 'none';
    answer_plus5.style.display = 'flex';
    answer_minus5.style.display = 'none';
})