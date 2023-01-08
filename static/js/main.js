// Показ модуля спросить
const div = document.querySelectorAll('.ask_modal_content')[0];
document.querySelector('#ask_button').addEventListener('click', function () {
    div.style.display = 'flex';
})
document.querySelector('#ask_modal_close').addEventListener('click', function () {
    div.style.display = 'none';
})
// Показ модуля перезвонить
const div2 = document.querySelectorAll('.recall_content')[0];

document.querySelector('#recall_button').addEventListener('click', function () {
    div2.style.display = 'flex';
})
document.querySelector('#recall_button2').addEventListener('click', function () {
    div2.style.display = 'flex';
})
document.querySelector('#recall_button3').addEventListener('click', function () {
    div2.style.display = 'flex';
})
document.querySelector('#recall_close').addEventListener('click', function () {
    div2.style.display = 'none';
})
if (document.querySelectorAll('.data_sent_content')[0]) {
    document.querySelectorAll('.data_sent_close')[0].addEventListener('click', function () {
        console.log("кнопка нажата")
        document.querySelectorAll('.data_sent_content')[0].style.display = 'none';
    })
}


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

// Выбор услуг в миниокне
const diagnostika_mini = document.getElementById('diagnostika_mini')
const consultation_mini = document.getElementById('consultation_mini')
const surgeon_mini = document.getElementById('surgeon_mini')
const help_clients_mini = document.getElementById('help_clients_mini')
const stationary_mini = document.getElementById('stationary_mini')
const emergency_help_mini = document.getElementById('emergency_help_mini')
const another_clients_mini = document.getElementById('another_clients_mini')
const paid_services_mini = document.getElementById('paid_services_mini')

document.querySelector('#diagnostika_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'flex';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#consultation_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'flex';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#surgeon_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'flex';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#surgeon_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'flex';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#help_clients_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'flex';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#stationary_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'flex';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#emergency_help_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'flex';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#another_clients_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'flex';
    paid_services_mini.style.display = 'none';
})
document.querySelector('#paid_services_mini_button').addEventListener('click', function () {
    diagnostika_mini.style.display = 'none';
    consultation_mini.style.display = 'none';
    surgeon_mini.style.display = 'none';
    help_clients_mini.style.display = 'none';
    stationary_mini.style.display = 'none';
    emergency_help_mini.style.display = 'none';
    another_clients_mini.style.display = 'none';
    paid_services_mini.style.display = 'flex';
})
