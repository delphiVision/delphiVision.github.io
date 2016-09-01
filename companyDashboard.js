$( document ).ready(function() {
    /* Get all rows from your 'table' but not the first one
     * that includes headers. */
    var companyID = sessionStorage.getItem("companyID")
    getCompanyName(companyID)
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
