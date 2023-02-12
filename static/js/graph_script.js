
my_label = MyGlobal.data_labels1;
window.onload = function () {
    data_1 = MyGlobal.data_first_last_month;
backgroundcolors1 = [];     //initialising backgraoungcolors1 array
for (i = 0; i < data_1.length; i++) {       //traverse throung data_1 array
    if (data_1[i] > 20) {               //check if at any index in e_working days value is greater than 20 or not
        backgroundcolors1.push('green');    //if value is greater than 20 push green in background array
    } else {
        backgroundcolors1.push('red');      //if value in e_workingdays is less or equal to 20 push red in background array 
    }
    console.log(backgroundcolors1)
}

data_2 = MyGlobal.data_second_last_month;
backgroundcolors2 = [];
for (i = 0; i < data_2.length; i++) {
    if (data_2[i] > 20) {
        backgroundcolors2.push('green');
    } else {
        backgroundcolors2.push('red');
    }
    console.log(backgroundcolors2)
}

data_3 = MyGlobal.data_third_last_month;
backgroundcolors3 = [];
for (i = 0; i < data_3.length; i++) {
    if (data_3[i] > 20) {
        backgroundcolors3.push('green');
    } else {
        backgroundcolors3.push('red');
    }
    console.log(backgroundcolors3)
}

console.log(123);
var chartData = {
    labels: MyGlobal.data_labels ,
datasets: [{
    label: my_label[0],
    backgroundColor: backgroundcolors1,
    data: MyGlobal.data_first_last_month
     },
{
    label: my_label[1],
    backgroundColor: backgroundcolors2,
    data: MyGlobal.data_second_last_month
     },
{
    label: my_label[2],
    backgroundColor: backgroundcolors3,
    data: MyGlobal.data_third_last_month
     }
]
  };
var canvas = document.getElementById("canvas");         //getting html canvas by id "canvas"
var myBarChart = new Chart(canvas, {
    type: "bar",                                         //giving type of graph
    data: chartData,
    options: {                                           //giving features of graph
        legend: {
            display: false,

        },
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    beginAtZero: true
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Working Days'
                }
            }],
            xAxes: [{

                scaleLabel: {
                    display: true,
                    labelString: 'Employees'
                }
            }]
        }
    }
});
      }  
