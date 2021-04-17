(function($){
"use strict";
	// barchart

	var chart1 = new CanvasJS.Chart("barchart", {
		animationEnabled: true,
		theme: "light2", // "light1", "light2", "dark1", "dark2"
		axisY: {
			title: "Reserves(MMbbl)"
		},
		data: [{        
			type: "column",  
			showInLegend: true, 
			legendMarkerColor: "grey",
			legendText: "MMbbl = one million barrels",
			dataPoints: [      
				{ y: 300878, label: "Venezuela" },
				{ y: 266455,  label: "Saudi" },
				{ y: 169709,  label: "Canada" },
				{ y: 158400,  label: "Iran" },
				{ y: 142503,  label: "Iraq" },
				{ y: 101500, label: "Kuwait" },
				{ y: 97800,  label: "UAE" },
				{ y: 80000,  label: "Russia" }
			]
		}]
	});
	chart1.render();

	// piechart

	var chart4 = new CanvasJS.Chart("piechart", {
		animationEnabled: true,
		data: [{
			type: "pie",
			startAngle: 240,
			yValueFormatString: "##0.00\"%\"",
			indexLabel: "{label} {y}",
			dataPoints: [
				{y: 79.45, label: "Google"},
				{y: 7.31, label: "Bing"},
				{y: 7.06, label: "Baidu"},
				{y: 4.91, label: "Yahoo"},
				{y: 1.26, label: "Others"}
			]
		}]
	});
	chart4.render();

	// Line chart
	var chart2 = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false
	},
		data: [{        
			type: "line",       
			dataPoints: [
				{ y: 450 },
				{ y: 414},
				{ y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle" },
				{ y: 460 },
				{ y: 450 },
				{ y: 500 },
				{ y: 480 },
				{ y: 480 },
				{ y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
				{ y: 500 },
				{ y: 480 },
				{ y: 510 }
			]
		}]
	});
	chart2.render();



})(this.jQuery);