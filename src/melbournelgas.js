  // Creating our initial map object:
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

// function to set the colors of the LGAs ( from https://colorbrewer2.org/#type=qualitative&scheme=Set3&n=10)
function chooseColor(vic_lga__3) {
  if (vic_lga__3 == "GLEN EIRA") return "yellow";
  else if (vic_lga__3 == "BAYSIDE") return "blue";
  else if (vic_lga__3 == "MELBOURNE") return "red";
  else if (vic_lga__3 == "PORT PHILLIP") return "purple";
  else if (vic_lga__3 == "GREATER DANDENONG") return "#ff7f00";
  else if (vic_lga__3 == "KINGSTON") return "orange";
  else if (vic_lga__3 == "BOROONDARA") return "#a6cee3";
  else if (vic_lga__3 == "CASEY") return "#33a02c";
  else if (vic_lga__3 == "FRANKSTON") return "#33a04b";
  else if (vic_lga__3 == "STONNINGTON") return "#1f78b4";
  else if (vic_lga__3 == "DAREBIN") return "#ff7f00";
  else if (vic_lga__3 == "HUME") return "#fb9a99";
  else if (vic_lga__3 == "HOBSONS BAY") return "#fb9a92";
  else if (vic_lga__3 == "KNOX") return "#6a3d9a";
  else if (vic_lga__3 == "MANNINGHAM") return "#e31a1c";
  else if (vic_lga__3 == "BANYULE") return "#fb9a99";
  else if (vic_lga__3 == "CARDINIA") return "#b2df8a";
  else if (vic_lga__3 == "BRIMBANK") return "#fdbf6f";
  else if (vic_lga__3 == "MARIBYRNONG") return "#ffffb3";
  else if (vic_lga__3 == "MAROONDAH") return "#b3de69";
  else if (vic_lga__3 == "MORELAND") return "#9dcde8";
  else if (vic_lga__3 == "MELTON") return "#8dd3c7";
  else if (vic_lga__3 == "MONASH") return "#b3de69";
  else if (vic_lga__3 == "MOONEE VALLEY") return "#ff7f00";
  else if (vic_lga__3 == "MORNINGTON PENINSULA") return "#ff7f50";
  else if (vic_lga__3 == "WHITTLESEA") return "#fb9222";
  else if (vic_lga__3 == "WHITEHORSE") return "#fb8702";
  else if (vic_lga__3 == "WYNDHAM") return "#fb8072";
  else if (vic_lga__3 == "YARRA") return "#fccde5";
  else if (vic_lga__3 == "YARRA RANGES") return "";
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
