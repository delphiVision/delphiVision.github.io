$( document ).ready(function() {
    $( "#findRevs" ).click(function( event ) {
            getMediaWikiReviews($('#wikiTitle').val(), $('#wikiBase').val())
        });
    $('#example').DataTable( {
        columnDefs: [ {
            orderable: false,
            className: 'select-checkbox',
            targets:   0
        } ],
        select: {
            style:    'os',
            selector: 'td:first-child'
        },
        order: [[ 1, 'asc' ]]
    } );
    });
    var contentArray = []
    function getMediaWikiReviews(wikiName, wikiBase) {
        var formName = wikiName;
        var xmlhttp = new XMLHttpRequest();
        var url = "http://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/mediaWikiRevisions?title=" + wikiName + "&base=" + wikiBase;
        // var url = "http://127.0.0.1:5000/mediaWikiRevisions?title=" + wikiName + "&base=" + wikiBase;
// http://127.0.0.1:5000/
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                parseResponse(xmlhttp.responseText)
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
        return false
    }
    function closePopup() {
      var popup = document.getElementById('myPopup');
      if (popup.classList.toggle('show') == true) {
        popup.classList.toggle('show');
      }
    }
    function activatePopup(content) {
        var popup = document.getElementById('myPopup');
        popup.textContent = content
        if (popup.classList.toggle('show') == false) {
          popup.classList.toggle('show');
        }

    }
    function parseResponse(response) {
    var longstring = ""
    var arr = JSON.parse(response);
        $('#id01').append("<tr> <th><input type=checkbox id=selectall/></th> <th>Revision Date</th> <th>Revision Comment</th> <th>View Revision</th> </tr>")
    for (i = 0; i < arr.revisions.length; i++) {
        var content = arr.revisions[i]['*']
        var newFilteredString = content.replace(/['"{}]|<\/?blockquote>/g, '')
        // var filteredContentOne = content.split("{").join(" ")
        // var filteredContentTwo = filteredContentOne.split("}").join(" ")

        contentArray.push(content)
        var timestamp = arr.revisions[i].timestamp
        var comment = arr.revisions[i]['comment']
        var beautified = new Date('2015-10-16T19:50:53Z')

var newCommitThingy = $(`
      <tr>
           <td align=center>
               <input type=checkbox class=case name=case/>
           </td>
           <td></td>
           <td></td>
           <td>
               <button id=revisionAtIndex>
                   View Revision
               </button>
           </td>
      </tr>
`);

newCommitThingy[0].querySelector('td input').value = i;
newCommitThingy[0].querySelectorAll('td')[1].innerText = timestamp;
newCommitThingy[0].querySelectorAll('td')[2].innerText = comment;
var buttonThingy = newCommitThingy[0].querySelector('td button');
buttonThingy.value = i;
buttonThingy.onclick = function(){activatePopup(content)};

$('#id01').append(newCommitThingy)

        // $('#id01').append("<tr> <td align=center><input type=checkbox class=case name=case value=" + i + "/></td> <td>" + timestamp + "</td> <td>" + comment +  "</td> <td> <button id=revisionAtIndex value=" + i + " onclick=alert("+ newFilteredString + ")>View Revision</button></td> </tr>");

        // longstring += timestamp + "<br>" + "<br>" + content + "<br>" + "<br>";
    }

        $("#id01").addClass('wellBehavedContainer')
        // document.getElementById("revisionAtIndex").addEventListener("click", function(event){
        //   alert(event.currentTarget.value)
        // });
        // $('#revisionAtIndex').click(function( event) {
        //     alert(event.currentTarget.value)
        // })

    // document.getElementById("id01").innerHTML = longstring;
}
