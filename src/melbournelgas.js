  // Creating our initial map object:
  let myMap = L.map("map", {
    center: [-37.840935, 144.946457],
    zoom: 10,
  });

 // Create the base layers.
 let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors <a href="https://data.gov.au/dataset/ds-dga-bdf92691-c6fe-42b9-a0e2-a4cd716fa811/details">VIC Local Government Areas - Geoscape Administrative Boundaries</a> <a href="https://github.com/davidmerfield/randomColor">RandomColours generated the colours on the map</a>'
}).addTo(myMap);


// Load the GeoJSON data for the LGA mapping area.
let link = "https://data.gov.au/geoserver/vic-local-government-areas-psma-administrative-boundaries/wfs?request=GetFeature&typeName=ckan_bdf92691_c6fe_42b9_a0e2_a4cd716fa811&outputFormat=json";

// function to set the colors of the LGAs (using randomColour js library)
var randomColor = require('randomcolor');

function chooseColor(vic_lga__3) {
  if (vic_lga__3 == "GLEN EIRA") return "return randomColor()";
  else if (vic_lga__3 == "BAYSIDE") return "return randomColor()";
  else if (vic_lga__3 == "MELBOURNE") return "return randomColor()";
  else if (vic_lga__3 == "PORT PHILLIP") return "return randomColor()";
  else if (vic_lga__3 == "GREATER DANDENONG") return "#return randomColor()";
  else if (vic_lga__3 == "KINGSTON") return "return randomColor()";
  else if (vic_lga__3 == "BOROONDARA") return "#return randomColor()";
  else if (vic_lga__3 == "CASEY") return "#return randomColor()";
  else if (vic_lga__3 == "FRANKSTON") return "#return randomColor()";
  else if (vic_lga__3 == "STONNINGTON") return "#return randomColor()";
  else if (vic_lga__3 == "DAREBIN") return "#return randomColor()";
  else if (vic_lga__3 == "HUME") return "#return randomColor()";
  else if (vic_lga__3 == "HOBSONS BAY") return "#return randomColor()";
  else if (vic_lga__3 == "KNOX") return "#return randomColor()";
  else if (vic_lga__3 == "MANNINGHAM") return "#return randomColor()";
  else if (vic_lga__3 == "BANYULE") return "#return randomColor()";
  else if (vic_lga__3 == "CARDINIA") return "#return randomColor()";
  else if (vic_lga__3 == "BRIMBANK") return "#return randomColor()";
  else if (vic_lga__3 == "MARIBYRNONG") return "#return randomColor()";
  else if (vic_lga__3 == "MAROONDAH") return "#return randomColor()";
  else if (vic_lga__3 == "MORELAND") return "#return randomColor()";
  else if (vic_lga__3 == "MELTON") return "#return randomColor()";
  else if (vic_lga__3 == "MONASH") return "#return randomColor()";
  else if (vic_lga__3 == "MOONEE VALLEY") return "#return randomColor()";
  else if (vic_lga__3 == "MORNINGTON PENINSULA") return "#return randomColor()";
  else if (vic_lga__3 == "WHITTLESEA") return "#return randomColor()";
  else if (vic_lga__3 == "WHITEHORSE") return "#return randomColor()";
  else if (vic_lga__3 == "WYNDHAM") return "#return randomColor()";
  else if (vic_lga__3 == "YARRA") return "#return randomColor()";
  else if (vic_lga__3 == "YARRA RANGES") return "return randomColor()";
  else return "black";
}

// Get the data with d3.
d3.json(link).then(function(data) {

  // Create a new layer.
 L.geoJson(data, {
  style: function(feature) {
    return {
      color: "white",
      fillColor: chooseColor(feature.properties.vic_lga__3),
      fillOpacity: 0.5,
      weight: 1.5
    };
  }
}).addTo(myMap);
});
