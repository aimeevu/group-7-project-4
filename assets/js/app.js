// BUTTON EVENT HANDLING

function predictprice() 
{

    var airline = d3.select("#airline").property("value");
    var from_loc = d3.select("#from_loc").property("value");
    var to_loc = d3.select("#to_loc").property("value");
    var depart = d3.select("#depart").property("value");
    var arrive = d3.select("#arrive").property("value");
    var seatclass = d3.select("#seatclass").property("value");
    var stop = d3.select("#stop").property("value");

    data = {
        "airline": airline,
        "from_loc": from_loc,
        "to_loc": to_loc,
        "depart": depart,
        "arrive": arrive,
        "seatclass": seatclass,
        "stop": stop,
    };

    console.log('response', data)

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(d => {
            console.log('response', d)
            var ticketprice = d.ticketprice

            document.getElementById("ticketprice").innerHTML = "<strong> Ticket Price: $" + ticketprice.toFixed(2) + "</strong>";
        }
        )

}