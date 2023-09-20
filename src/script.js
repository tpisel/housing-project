// Initialize Leaflet map.
let myMap = L.map("map", {
  center: [-37.840935, 144.946457],
  zoom: 10,
});

// Create the base layers.
let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors <a href="https://data.gov.au/dataset/ds-dga-bdf92691-c6fe-42b9-a0e2-a4cd716fa811/details">VIC Local Government Areas - Geoscape Administrative Boundaries</a>'
}).addTo(myMap);

// Load the GeoJSON data for the LGA mapping area.
let link = "https://data.gov.au/geoserver/vic-local-government-areas-psma-administrative-boundaries/wfs?request=GetFeature&typeName=ckan_bdf92691_c6fe_42b9_a0e2_a4cd716fa811&outputFormat=json";

// Generate a random RGB color
function getRandomColor() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r},${g},${b})`;
}

// Function to generate a random RGB color array for charts
function getRandomColorArray(numColors) {
  const colors = [];
  for (let i = 0; i < numColors; i++) {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      colors.push(`rgb(${r},${g},${b},0.9)`);
  }
  return colors;
}
// Get random colors array
const randomColors = getRandomColorArray(6);

// Get the data from geojson js file.
//const data = geoJSON[0];

// Get the data with d3.
d3.json(link).then(function(data) {
// Add GeoJSON data to the map
L.geoJson(data, {
    style: function(feature) {
      return {
        color: "white",
        fillColor: getRandomColor(),
        fillOpacity: 0.5,
        weight: 1.5
      };
    },
    // Set the mouse click event to refresh the charts.
    onEachFeature: function(feature, layer) {
        layer.on({
            click: function(event){
                const name = feature.properties.vic_lga__3;
                updateChart(name);
            }
        });
        layer.bindPopup("<h3>" + feature.properties.lga_pid + "</h3> <hr> <h5>" + feature.properties.vic_lga__2 + "</h5>");
    }
}).addTo(myMap);
});

// Initialize the charts
const chart1 = Highcharts.chart('highChart1', {
  chart: {type: 'column'},
  title: {text: 'Total Number of Planning Applications by Dwelling Type'},
  yAxis: {title: {text: 'Total Number of Planning Applications'}},
  plotOptions: {
    column: {
        colorByPoint: true,
        colors: randomColors // Add more colors if needed
    }
  },
  series: [{name: 'Dwellings',data: []}]
});
const chart2 = Highcharts.chart('highChart2', {
  chart: {type: 'column'},
  title: {text: 'Total Number of Current Dwellings by Dwelling Type'},
  yAxis: {title: {text: 'Total Number of Current Dwellings'}},
  plotOptions: {
    column: {
        colorByPoint: true,
        colors: randomColors // Add more colors if needed
    }
  },
  series: [{name: 'Dwellings',data: []}]
});

// Set the api url to get the charting data
const application_api = 'http://127.0.0.1:5000/api/nstories';
const dwelling_api = 'http://127.0.0.1:5000/api/dwellings';

// Create the arrays
let categories = [];
let values = [];

// Function to update the chart
function updateChart(areaName) {
  // Create random colors array
  const randomColors1 = getRandomColorArray(6);
  // Get the data from api, read it and create the categories and values list
  d3.json(application_api).then(function(data) {
    categories = [];
    values = [];
    data.forEach(element => {
      // Transform the census name for correct mapping for some of the LGA's
      let censusName = element.census_name_2021;
      if(censusName === 'Bayside (Vic.)'){
        censusName = 'Bayside';
      }else if(censusName === 'Kingston (Vic.)'){
        censusName = 'Kingston';
      }else if(censusName === 'Latrobe (Vic.)'){
        censusName = 'Latrobe';
      }
      let censusNameUpper = censusName.toUpperCase();
      if(areaName === censusNameUpper){
        categories.push(element.storey.toString()+' Storey');
        values.push(element.applications);
      }
    });
    // Update the chart with categories and values array
    chart1.update({
      xAxis: {categories:categories,
        title: {
          text: 'Original Data From: https://www.planningalerts.org.au'
        }
      },
      plotOptions: {
        column: {
            colorByPoint: true,
            colors: randomColors1
        }
      },
      series: [{data: values}],
      tooltip: {
        formatter: function() {
            return '<b>' + "Total Applications" + '</b>: ' + this.y;
        }
      }
    });
  });

  // Create random colors array
  const randomColors2 = getRandomColorArray(6);
  // Get the data from api, read it and create the categories and values list
  d3.json(dwelling_api).then(function(data) {
    categories = ['Single Storey','Two Storey','Three Storey','Four and Above Storey'];
    values = [];
    data.forEach(element => {
      // Transform the census name for correct mapping for some of the LGA's
      let censusName = element.census_name_2021;
      if(censusName === 'Bayside (Vic.)'){
        censusName = 'Bayside';
      }else if(censusName === 'Kingston (Vic.)'){
        censusName = 'Kingston';
      }else if(censusName === 'Latrobe (Vic.)'){
        censusName = 'Latrobe';
      }
      let censusNameUpper = censusName.toUpperCase();
      if(areaName === censusNameUpper){
        values = [element['Single Storey Total'], element['Two Storey Total'], element['Three Storey Total'], element['Four Storey and Above Storey Total']]
      }
    });
    // Update the chart with categories and values array
    chart2.update({
      xAxis: {categories:categories,
        title: {
          text: 'Original Data From: 2021 Census'
        }
      },
      plotOptions: {
        column: {
            colorByPoint: true,
            colors: randomColors2
        }
      },
      series: [{data: values}],
      tooltip: {
        formatter: function() {
            return '<b>' + "Total Dwellings" + '</b>: ' + this.y;
        }
      }
    });
  });
}
