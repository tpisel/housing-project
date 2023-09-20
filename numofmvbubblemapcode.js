// Create a map object.
let myMap = L.map("map", {
  center: [-37.8136, 144.9631],
  zoom: 10
});

// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

import data from './data.json';
console.log(data);


for (let i = 0; i < Num_MVs_per_dweling_Tot.length; i++) {
  // Conditionals for Number of motor vehicles per dwelling
  let color = "";
  if (Num_MVs_per_dweling_0_MVs[i].LGA_CODE_2021 = 0) {
    var randomColor = require('randomcolor');
  }
  else if (Num_MVs_per_dweling_1_MVs[i].LGA_CODE_2021 = 1) {
    var randomColor = require('randomcolor');
  }
  else if (Num_MVs_per_dweling_2_MVs[i].LGA_CODE_2021 = 2) {
    var randomColor = require('randomcolor');
  }
  else if (Num_MVs_per_dweling_3_MVs[i].LGA_CODE_2021 =3) {
    var randomColor = require('randomcolor');
  }
  else if (Num_MVs_per_dweling_4mo_MVs[i].LGA_CODE_2021 <= 4) {
    var randomColor = require('randomcolor');
  }
  else{
    var randomColor = require('randomcolor');
  }

return colors;
}

    // Define a markerSize() function that will give each city a different radius based on its population.
    function markerSize(Num_MVs_per_dweling) {
      return Math.sqrt(population) * 50;
    }

  // Add circles to the map.
  L.circle(Victoria[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: color,

    // Adjust the radius.
    radius: Math.sqrt(Num_MVs_per_dweling[i].LGA_CODE_2021) * 5
  }).bindPopup(`<h1>${Num_MVs_per_dweling[i].LGA_CODE_2021}</h1> <hr> <h3> Num_MVs_per_dweling</h3>`
  )

