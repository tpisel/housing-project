// Create a map object.
let myMap = L.map("map", {
    center: [-37.8136, 144.9631],
    zoom: 10
  });
  
  // Add a tile layer.
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  
  import data from './data1.json';
  console.log(data1);
  
  
  for (let i = 0; i < Medianhousehold.length; i++) {
 
    let color = "";
    if (Median_tot_fam_inc_weekly[i].LGA_CODE_2021 = 0) {
      var randomColor = require('randomcolor');
    }
    else if (Average_num_psns_per_bedroom[i].LGA_CODE_2021 = 1) {
      var randomColor = require('randomcolor');
    }
    else if (Average_household_size[i].LGA_CODE_2021 = 2) {
      var randomColor = require('randomcolor');
    }

  return colors;
  }
  
      // Define a markerSize() function that will give each city a different radius based on its population.
      function markerSize(Medianhousehold) {
        return Math.sqrt(population) * 50;
      }
  
    // Add circles to the map.
    L.circle(Victoria[i].location, {
      fillOpacity: 0.75,
      color: "white",
      fillColor: color,
  
      // Adjust the radius.
      radius: Math.sqrt(Medianhousehold[i].LGA_CODE_2021) * 5
    }).bindPopup(`<h1>${Medianhousehold[i].LGA_CODE_2021}</h1> <hr> <h3> Medianhousehold</h3>`
    )
  
  