d3.csv("data/2009.csv", function(d) {
  var format = d3.time.format("%Y");
  return {
    'Year': format.parse(d.year),
    'Carrier Name': d.carrier_name,
    'On Time': +d.on_time,
    'Arrivals': +d.arrivals
  };
}, function(data) {
  'use strict';

  // append title
  d3.select('#content')
    .append('h2')
    .attr('id', 'title')
    .text('On-Time Arrival Rates for Top U.S. Domestic Airlines, 2003-2014');

  // set svg
  var width = 960,
      height = 640;
  var svg = dimple.newSvg('#content', width, height);
  var myChart = new dimple.chart(svg, data);

  // set y axis
  var minY = 0.5,
      maxY = 1;
  var y = myChart.addMeasureAxis('y', 'On Time');
  y.tickFormat = '%';
  y.overrideMin = minY;
  y.overrideMax = maxY;
  y.title = 'Percentage of Arrivals on Time (within 15 minutes)';

  // set x axis
  var x = myChart.addTimeAxis('x', 'Year');
  x.tickFormat = '%Y';
  x.title = 'Year';

  // set series and legend
  var s = myChart.addSeries('Carrier Name', dimple.plot.scatter);
  var p = myChart.addSeries('Carrier Name', dimple.plot.line);
  var first_legend = myChart.addLegend(140, 10, 700, 20, "left");

  // draw
  myChart.draw();

  // handle mouse events on gridlines
  y.gridlineShapes.selectAll('line')
    .style('opacity', 0.25)
    .on('mouseover', function(e) {
      d3.select(this)
        .style('opacity', 1);
    }).on('mouseleave', function(e) {
      d3.select(this)
        .style('opacity', 0.25);
    });

  // handle mouse events on paths
  d3.selectAll('path')
    .style('opacity', 0.25)
    .on('mouseover', function(e) {
      d3.select(this)
        .style('stroke-width', '8px')
        .style('opacity', 1)
        .attr('z-index', '1');
  }).on('mouseleave', function(e) {
      d3.select(this)
        .style('stroke-width', '2px')
        .style('opacity', 0.25)
        .attr('z-index', '0');
  });

	myChart.legends = [];

	//Creating a list of unique values for handedness of players
	var airline_filterValues = dimple.getUniqueValues(data, "Carrier Name");

	console.log(airline_filterValues);

	//Capturing the "Click" event of all rectangular shapes in the legend
	first_legend.shapes.select("rect")
		.on("click", function (e) {
			var hide = false;
            		var newFilters = [];

			//Check what value of handedness to hide based on what's clicked
            		airline_filterValues.forEach(function (f) {
				if (f === e.aggField.slice(-1)[0]) {
					hide = true;
				} else {
				                newFilters.push(f);
				       }
            		});
			//Set the opacity value based on clicked
            		if (hide) {
			              d3.select(this).style("opacity", 0.2);
			          }
			 else	{
			              newFilters.push(e.aggField.slice(-1)[0]);
			              d3.select(this).style("opacity", 0.8);
            			}

			//Filter data based on selection
            		airline_filterValues = newFilters;
            		myChart.data = dimple.filterData(data, "Carrier Name", airline_filterValues);

			//re-draw charts based on filtered data
            		myChart.draw(700);
          	});

});