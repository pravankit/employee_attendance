
  

    $(document).ready(function () {
        $('.input-daterange').datepicker({
            todayBtn: 'linked',
            format: "yyyy-mm-dd",
            autoclose: true
        });
    });




    window.onload = function () {
        const a1 = MyGlobal1.label_names;
        const a2 = MyGlobal1.days_graph;
        const tbody = document.querySelector('tbody');
    
        for (let i = 0; i <  MyGlobal1.label_names.length; i++) {
            const tr = tbody.insertRow();
            tr.insertCell().innerHTML = a1[i] ? a1[i] : ''
            tr.insertCell().innerHTML = a2[i] ? a2[i] : ''
        }


    var ctx = document.getElementById("chartjs_bar").getContext('2d');  //getting canvas of webpage by its id =chartjs_bar
    var myChart = new Chart(ctx, {
        type: 'bar',                                                    //providing the type of required chart
        data: {labels: MyGlobal1.label_names,
               datasets: [{backgroundColor: MyGlobal1.backgroundcolor,
                           data: MyGlobal1.days_graph }]},
    options: {legend: {display: false},
        scales: { yAxes: [{ticks: {beginAtZero: true},scaleLabel: {display: true,labelString: 'Working_Days' } }],
                  xAxes: [{scaleLabel: {display: true,labelString: 'Months'}}]}
}
});}