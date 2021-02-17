if(status_data) {
	if ($("#spline_area").length) {
		options = {
			chart: {
				height: 300,
				type: "area"
			},
			dataLabels: {
				enabled: !1
			},
			stroke: {
				curve: "smooth",
				width: 3
			},
			series: [{
				name: "Прибыль",
				data: datajsonin.value
			}],
			colors: ["#010181"],
			xaxis: {
				type: 'datetime',
				categories: datajsonin.data
			},
			grid: {
				borderColor: "#f1f1f1"
			},
		};
		(chart = new ApexCharts(document.querySelector("#spline_area"), options)).render()
	}
}

if ($('#mixed_chart').length) {
    var options = {
        chart: {
            height: 200,
            type: 'line',
            stacked: false,
            toolbar: {
                show: false
            }
        },
        stroke: {
            width: [0, 0, 4],
            curve: 'smooth'
        },
        plotOptions: {
            bar: {
                columnWidth: '70%'
            }
        },
        colors: ['#010181'],
        series: [{
            name: 'Team A',
            type: 'column',
            data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30]
        }],
        fill: {
            opacity: [0.90, 0.25, 1],
            gradient: {
                inverseColors: false,
                shade: 'light',
                type: "vertical",
                opacityFrom: 0.85,
                opacityTo: 0.55,
                stops: [0, 100, 100, 100]
            }
        },
        labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
        markers: {
            size: 0
        },
        legend: {
            offsetY: -10,
        },
        xaxis: {
            type: 'datetime'
        },
        tooltip: {
            shared: true,
            intersect: false,
            y: {
                formatter: function (y) {
                    if (typeof y !== "undefined") {
                        return y.toFixed(0) + " points";
                    }
                    return y;

                }
            }
        },
        grid: {
            borderColor: '#f1f1f1'
        }
    }

    var chart = new ApexCharts(
        document.querySelector("#mixed_chart"),
        options
    );

    chart.render();
}