function validate() {
    var remember = document.getElementById("time_recall_check");
    if (remember.checked) {
        document.getElementById('recall_time').setAttribute('disabled', '');
        document.getElementById('recall_time').setAttribute('required', 'false');
        document.getElementById('recall_time').setAttribute('style', "background-color: gray; opacity: 0.35; border: 0;");     
    }
    else {
        document.getElementById('recall_time').removeAttribute('disabled');
        document.getElementById('recall_time').setAttribute('style', "background-color: white");   
        document.getElementById('recall_time').setAttribute('required', 'true');
    }
    }

document.querySelector('#time_recall_check').addEventListener('click', function () {
    validate()
})

