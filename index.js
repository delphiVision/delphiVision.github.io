$( document ).ready(function() {
$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
$('#login').click(function() {
  authenticateUser($('#email').val(), $('#password').val())
})
});

function authenticateUser(email, password) {
  var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/authenticateCompany"
  var formData = new FormData();
  var xmlhttp = new XMLHttpRequest();
  formData.append("email", email);
  formData.append("password", password);
  xmlhttp.onreadystatechange = function () {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
          if (xmlhttp.responseText == "False") {
            $('#incorrectPassword').text("Incorrect Password");
          } else {
            $('#incorrectPassword').text("Authenticated");
            window.location.replace("mwikitest.html");          }
      }
  }
  xmlhttp.open("POST", serverURL);
  xmlhttp.send(formData);
}
