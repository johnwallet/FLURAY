$(".slider-for").slick({
	slidesToShow: 1,
	slidesToScroll: 1,
	arrows: !1,
	asNavFor: ".slider-nav"
}), $(".slider-nav").slick({
	slidesToShow: 3,
	slidesToScroll: 1,
	asNavFor: ".slider-for",
	dots: !1,
	centerMode: !0,
	focusOnSelect: !0,
	responsive: [{
		breakpoint: 600,
		settings: {
			slidesToShow: 2,
			slidesToScroll: 2
		}
	}, {
		breakpoint: 480,
		settings: {
			slidesToShow: 1,
			slidesToScroll: 1
		}
	}]
});