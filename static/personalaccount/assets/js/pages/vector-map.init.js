! function(o) {
	"use strict";

	function r() {}
	r.prototype.init = function() {
		o("#world-map-markers").vectorMap({
			map: "world_en",
			normalizeFunction: "polynomial",
			hoverOpacity: .7,
			hoverColor: !1,
			backgroundColor: "#transparent",
			color: "#f2f5f7",
			borderColor: "#bcbfc7",
			colors: { in : "#3051d3", au: "#3051d3", gl: "#3051d3", us: "#3051d3", sa: "#3051d3"
			},
			borderColors: { in : "#3051d3", au: "#3051d3", gl: "#3051d3", us: "#3051d3", sa: "#3051d3"
			}
		}), o("#usa").vectorMap({
			map: "usa_en",
			enableZoom: !0,
			showTooltip: !0,
			selectedColor: null,
			hoverColor: "#4865d8",
			backgroundColor: "transparent",
			color: "#3051d3",
			borderColor: "#bcbfc7",
			colors: {
				ca: "#4865d8",
				tx: "#4865d8",
				mt: "#4865d8",
				ny: "#4865d8"
			},
			onRegionClick: function(o, r, a) {
				o.preventDefault()
			}
		}), o("#canada").vectorMap({
			map: "canada_en",
			backgroundColor: "transparent",
			color: "#3051d3",
			hoverColor: "#4865d8",
			borderColor: "#bcbfc7",
			enableZoom: !0,
			showTooltip: !0
		}), o("#france").vectorMap({
			map: "france_fr",
			backgroundColor: "transparent",
			color: "#3051d3",
			borderColor: "#bcbfc7",
			hoverColor: "#4865d8",
			enableZoom: !0,
			showTooltip: !0
		}), o("#germany").vectorMap({
			map: "germany_en",
			backgroundColor: "transparent",
			color: "#3051d3",
			borderColor: "#bcbfc7",
			hoverColor: "#4865d8",
			enableZoom: !0,
			showTooltip: !0
		}), o("#brazil").vectorMap({
			map: "brazil_br",
			backgroundColor: "transparent",
			color: "#3051d3",
			borderColor: "#bcbfc7",
			hoverColor: "#4865d8",
			enableZoom: !0,
			showTooltip: !0
		})
	}, o.VectorMap = new r, o.VectorMap.Constructor = r
}(window.jQuery),
function() {
	"use strict";
	window.jQuery.VectorMap.init()
}();