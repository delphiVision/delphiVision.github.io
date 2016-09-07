$( document ).ready(function() {
$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
$('#login').click(function() {
  authenticateUser($('#email').val(), $('#password').val())
  //TODO MAKE A SWITCH STATEMENT AND DIFFERENT AUTH FUNCTIONS FOR PATENT WRITERS COMPANIES AND Employees
})
});

function authenticateUser(email, password) {
  switch($('#acctTypeSelecter').val()) {
    case 'employee':
        var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/authenticateEmployee"
        break;
    case 'company':
        var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/authenticateCompany"
        break;
    case 'patentWriter':
        var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/authenticatePatentWriter"
        break;
    default:
        alert("Selector not working");
    }
  var formData = new FormData();
  var xmlhttp = new XMLHttpRequest();
  formData.append("email", email);
  formData.append("password", password);
  xmlhttp.onreadystatechange = function () {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
          if (xmlhttp.responseText == "False") {
            $('#incorrectPassword').text("Invalid Credentials");
            $("#incorrectPassword").addClass('badPasswordStyling')
          } else {
            $('#incorrectPassword').text("Authenticated");
            switch($('#acctTypeSelecter').val()) {
              case 'employee':
                  var employeeDict = JSON.parse(xmlhttp.responseText)
                  // for ((key, value) in employeeDict) {
                  //   sessionStorage.setItem(key, value)
                  // }
                  window.location.href = "employeeDashboard.html";
                  break;
              case 'company':
                  sessionStorage.setItem("companyID", xmlhttp.responseText)
                  window.location.href = "companyDashboard.html";
                  break;
              case 'patentWriter':
                  window.location.href = "patentWriterDashboard.html";
                  break;
              default:
                  alert("Selector not working");
              }
                 }
      }
  }
  xmlhttp.open("POST", serverURL);
  xmlhttp.send(formData);
}
