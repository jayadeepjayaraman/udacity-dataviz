d3.csv("data/year_agg.csv", function(d) {
  var format = d3.time.format("%Y");
  return {
    'Year': format.parse(d.year),
    'Carrier Name': d.carrier_name,
    'Delay Cause': d.delay_cause,
    'Delay Mins': +d.delay_mins,
    'Delay Percentage': +d.percentage_delay
  };
}, function(data) {
  'use strict';

  // append title
  d3.select('#pie')
    .append('h2')
    .attr('id', 'title')
    .text('Delay Cause Percentages by Year, 2003-2014');

  // set svg
  var width = 960,
      height = 640;
  var svg = dimple.newSvg('#pie', width, height);
  var myChart = new dimple.chart(svg, data);

  // set y axis
  var minY = 0,
      maxY = 1;
  var y = myChart.addMeasureAxis('y', 'Delay Percentage');
  y.tickFormat = '%';
  y.overrideMin = minY;
  y.overrideMax = maxY;
  y.title = 'Percentage Delay';

  // set x axis
  var x = myChart.addTimeAxis('x', 'Year');
  x.tickFormat = '%Y';
  x.title = 'Year';

  // set series and legend
  var s = myChart.addSeries('Delay Cause', dimple.plot.scatter);
  var p = myChart.addSeries('Delay Cause', dimple.plot.line);
  var legend = myChart.addLegend(140, 10, 800, 20, "left");

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
	var filterValues = dimple.getUniqueValues(data, "Delay Cause");

	console.log(filterValues);

	//Capturing the "Click" event of all rectangular shapes in the legend
	legend.shapes.select("rect")
		.on("click", function (e) {
			var hide = false;
            		var newFilters = [];

			//Check what value of handedness to hide based on what's clicked
            		filterValues.forEach(function (f) {
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
            		filterValues = newFilters;
            		myChart.data = dimple.filterData(data, "Delay Cause", filterValues);

			//re-draw charts based on filtered data
            		myChart.draw(700);
          	});

});