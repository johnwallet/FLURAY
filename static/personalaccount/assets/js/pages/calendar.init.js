! function(i) {
	"use strict";

	function e() {}
	e.prototype.init = function() {
		if(i.isFunction(i.fn.fullCalendar)) {
			i("#external-events .fc-event").each(function() {
				var e = {
					title: i.trim(i(this).text())
				};
				i(this).data("eventObject", e), i(this).draggable({
					zIndex: 999,
					revert: !0,
					revertDuration: 0
				})
			});
			var e = new Date,
				t = e.getDate(),
				a = e.getMonth(),
				n = e.getFullYear();
			i("#calendar").fullCalendar({
				header: {
					left: "prev,next today",
					center: "title",
					right: "month,basicWeek,basicDay"
				},
				editable: !0,
				eventLimit: !0,
				droppable: !0,
				drop: function(e, t) {
					var a = i(this).data("eventObject"),
						n = i.extend({}, a);
					n.start = e, n.allDay = t, i("#calendar").fullCalendar("renderEvent", n, !0), i("#drop-remove").is(":checked") && i(this).remove()
				},
				events: [{
					title: "All Day Event",
					start: new Date(n, a, 1)
				}, {
					title: "Long Event",
					start: new Date(n, a, t - 5),
					end: new Date(n, a, t - 2)
				}, {
					id: 999,
					title: "Repeating Event",
					start: new Date(n, a, t - 3, 16, 0),
					allDay: !1
				}, {
					id: 999,
					title: "Repeating Event",
					start: new Date(n, a, t + 4, 16, 0),
					allDay: !1
				}, {
					title: "Meeting",
					start: new Date(n, a, t, 10, 30),
					allDay: !1
				}, {
					title: "Lunch",
					start: new Date(n, a, t, 12, 0),
					end: new Date(n, a, t, 14, 0),
					allDay: !1
				}, {
					title: "Birthday Party",
					start: new Date(n, a, t + 1, 19, 0),
					end: new Date(n, a, t + 1, 22, 30),
					allDay: !1
				}, {
					title: "Click for Google",
					start: new Date(n, a, 28),
					end: new Date(n, a, 29),
					url: "http://google.com/"
				}]
			}), i("#add_event_form").on("submit", function(e) {
				e.preventDefault();
				var t = i(this).find(".new-event-form"),
					a = t.val();
				if(3 <= a.length) {
					var n = "new" + Math.random().toString(36).substring(7);
					i("#external-events").append('<div id="' + n + '" class="fc-event">' + a + "</div>");
					var r = {
						title: i.trim(i("#" + n).text())
					};
					i("#" + n).data("eventObject", r), i("#" + n).draggable({
						revert: !0,
						revertDuration: 0,
						zIndex: 999
					}), t.val("").focus()
				} else t.focus()
			})
		} else alert("Calendar plugin is not installed")
	}, i.CalendarPage = new e, i.CalendarPage.Constructor = e
}(window.jQuery),
function() {
	"use strict";
	window.jQuery.CalendarPage.init()
}();