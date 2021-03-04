if ($("#spline_area").length) {
    options = {
        chart: {
            height: 250,
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
        colors: ["#050452"],
        xaxis: {
            type: 'datetime',
            categories: datajsonin.data
        },
        tooltip: {
            shared: true,
            intersect: false,
            y: {
                formatter: function (y) {
                    if (typeof y !== "undefined") {
                        return y.toFixed(2) + " $";
                    }
                    return y;

                }
            }
        },
        grid: {
            borderColor: "#f1f1f1"
        },
    };
    (chart = new ApexCharts(document.querySelector("#spline_area"), options)).render()
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
        colors: ['#050452'],
        series: [{
            name: 'Доход',
            type: 'column',
            data: datajsonin.value
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
        labels: datajsonin.data,
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
                        return y.toFixed(2) + " $";
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