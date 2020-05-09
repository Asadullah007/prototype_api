let submit = document.getElementById('submit');
let form = document.getElementById('myForm');

submit.addEventListener('click', submission);

async function submission(e) {
  e.preventDefault();

  var fd = new FormData(form);

  await fetch('http:localhost:5000/api/predict', {
    method: 'POST',
    body: fd
  }).then(res => {
    res = res.json();
    return res;
  }).then(jsonData => {
    swal({
      title: 'Result',
      text: 'Prediction is ' + jsonData.data,
      button: "ok"
    });
  }).catch(err => {
    console.log(err);
  });
}