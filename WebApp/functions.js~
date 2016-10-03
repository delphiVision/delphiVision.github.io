$( document ).ready(function() {
    $( "#findRevs" ).click(function( event ) {
            getMediaWikiReviews($('#wikiTitle').val())
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
    $('#revisionAtIndex').click(function( event) {
        alert(event.currentTarget.value)
    })
    });
    var contentArray = []
    function getMediaWikiReviews(wikiName) {
        var formName = wikiName;
        var xmlhttp = new XMLHttpRequest();
        var url = "https://ec2-54-218-78-162.us-west-2.compute.amazonaws.com/mediaWikiRevisions?title=" + wikiName;
        // var url = "http://127.0.0.1:5000/mediaWikiRevisions?title=" + wikiName;

        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                parseResponse(xmlhttp.responseText)
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
        return false
    }
    function parseResponse(response) {
    var longstring = ""
    var arr = JSON.parse(response);
        $('#id01').append("<tr> <th><input type=checkbox id=selectall/></th> <th>Revision Date</th> <th>Revision Comment</th> <th>View Revision</th> </tr>")
    for (i = 0; i < arr.revisions.length; i++) {
        var content = arr.revisions[i]['*']
        contentArray.push(content)
        var timestamp = arr.revisions[i].timestamp
        var comment = arr.revisions[i]['comment']
        var beautified = new Date('2015-10-16T19:50:53Z')
        $('#id01').append("<tr> <td align=center><input type=checkbox class=case name=case value=" + i + "/></td> <td>" + timestamp + "</td> <td>" + comment +  "</td> <td> <button id=revisionAtIndex value=" + i + ">View Revision</button></td> </tr>");

        // longstring += timestamp + "<br>" + "<br>" + content + "<br>" + "<br>";
    }
        $("#id01").addClass('wellBehavedContainer')

    // document.getElementById("id01").innerHTML = longstring;
}
