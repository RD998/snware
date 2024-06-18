function admin_login(){

    
}
  function user_login() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '127.0.0.1:5500/snware/clientRC', true);
    xhr.send();
    window.location ='/snware/clientRC';
  }
