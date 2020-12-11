/*
es: Función para hacer GET requests
en: Function to do GET requests
ref: https://www.codegrepper.com/code-examples/javascript/get+request+with+pure+javascript
*/
function makeRequest (method, url, data) {
  return new Promise(function (resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.onload = function () {
      if (this.status >= 200 && this.status < 300) {
        resolve(xhr.response);
      } else {
        reject({
          status: this.status,
          statusText: xhr.statusText
        });
      }
    };
    xhr.onerror = function () {
      reject({
        status: this.status,
        statusText: xhr.statusText
      });
    };
    if(method=="POST" && data){
        xhr.send(data);
    }else{
        xhr.send();
    }
  });
}
/*
es: función que se ejecuta cuando carga el "body" del html
en: function triggered after body is loaded
*/
function funcOnLoad() {
  console.log("Loaded!");
}
/*
es: función que se ejecuta cuando se hace clic en el botón
en: function triggered on click
*/
function funcOnClick() {
  document.getElementById("resultado").innerHTML = "Cargando...";
  let param1 = document.getElementById("param1").value;
  let param2 = document.getElementById("param2").value;
  let url = "http://localhost:5000/calcula/" + param1 + "/" + param2;
  makeRequest("GET", url).then(function (data) {
    let resultado = JSON.parse(data);
    document.getElementById("resultado").innerHTML = resultado.resultado
      ? resultado.resultado
      : resultado.error;
  });
}
