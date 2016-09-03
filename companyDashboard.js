$( document ).ready(function() {
    /* Get all rows from your 'table' but not the first one
     * that includes headers. */
    var companyID = sessionStorage.getItem("companyID")
    var companyName = getCompanyName(companyID)
    companyEmail = getCompanyEmail(companyID)
    //populate employee table
    populateEmployeeTable()
    populateProjectTable()
    populatePatentWriterTable()

    //populate project table


    var rows = $('tr').not(':first');
    /* Create 'click' event handler for rows */
    rows.on('click', function(e) {
        /* Get current row */
        var row = $(this);
            /* Otherwise just highlight one row and clean others */
            rows.removeClass('highlight');
            row.addClass('highlight');
    });


});
var companyEmail = ""
function postToRouteAndReturnJSON(route) {
  var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/" + route
  var formData = new FormData();
  var xmlhttp = new XMLHttpRequest();
  formData.append("companyEmail", companyEmail);
  xmlhttp.onreadystatechange = function () {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
          return xmlhttp.responseText
      }
  }
  xmlhttp.open("POST", serverURL);
  xmlhttp.send(formData);
}
function populateEmployeeTable() {
    var tableHeader = $(`
        <tr>
            <th>Employee Name</th>
            <th>Employee Email</th>
        </tr>`)
    $('#employeeTable').append(tableHeader)
    var arrayOfEmployees = postToRouteAndReturnJSON("getEmployeesFromCompanyEmail")
    for (employeeDict in arrayOfEmployees) {
      var employeeName = employeeDict['name']
      var employeeEmail = employeeDict['email']
      var tableRow = $(`
      <tr>
          <td>` + employeeName +`</td>
          <td>` + employeeEmail + `</td>
      </tr>
      `)
      $('#employeeTable').append(tableRow)
    }
}
var projectIDToProjectName = {}
function populateProjectTable() {
  var tableHeader = $(`
      <tr>
          <th>Project Name</th>
          <th>Project URL</th>
      </tr>`)
  $('#projectTable').append(tableHeader)
  var arrayOfProjects = postToRouteAndReturnJSON("getProjectsFromCompanyEmail")
  for (projectDict in arrayOfProjects) {
    var projectName = projectDict["name"]
    var projectURL = projectDict["proj_url"]
    var projectID = projectDict["proj_id"]
    projectIDToProjectName[projectID] = projectName
    var tableRow = $(`
    <tr>
        <td>` + projectName +`</td>
        <td>` + projectURL + `</td>
    </tr>
    `)
    $('#projectTable').append(tableRow)
  }
}
function populatePatentWriterTable() {
  var tableHeader = $(`
      <tr>
          <th>Patent Writer Name</th>
          <th>Patent Writer Email</th>
          <th>Project</th>
      </tr>`)
  $('#patentWriterTable').append(tableHeader)
  var arrayOfPatentWriters = postToRouteAndReturnJSON("getPatentWritersFromCompanyEmail")
  for (patentWriterDict in arrayOfPatentWriters) {
    var patentWriterName = patentWriterDict['name']
    var patentWriterEmail = patentWriterDict['email']
    var patentWriterProjectID = patentWriterDict['project_id']
    var projectNameOfPatentWriter = projectIDToProjectName[patentWriterProjectID]
    var tableRow = $(`
    <tr>
        <td>` + patentWriterName +`</td>
        <td>` + patentWriterEmail + `</td>
        <td>` + projectNameOfPatentWriter + `</td>
    </tr>
    `)
    $('#patentWriterTable').append(tableRow)
  }
}
function getCompanyName(id) {
  var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/getCompanyName"
  var formData = new FormData();
  var xmlhttp = new XMLHttpRequest();
  formData.append("companyID", id);
  xmlhttp.onreadystatechange = function () {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        $('#radio').text("Welcome " + xmlhttp.responseText)
      }
  }
  xmlhttp.open("POST", serverURL);
  xmlhttp.send(formData);
}
function getCompanyEmail(id) {
  var serverURL = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/getCompanyEmail"
  var formData = new FormData();
  var xmlhttp = new XMLHttpRequest();
  formData.append("companyID", id);
  xmlhttp.onreadystatechange = function () {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        $('#radio').text("Welcome " + xmlhttp.responseText)
      }
  }
  xmlhttp.open("POST", serverURL);
  xmlhttp.send(formData);
}
