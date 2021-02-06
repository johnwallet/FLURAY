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