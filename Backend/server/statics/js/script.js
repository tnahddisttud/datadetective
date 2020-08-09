google.charts.load('current', {
  'packages': ['map'],
  // Note: you will need to get a mapsApiKey for your project.
  // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
  'mapsApiKey': 'AIzaSyCxsRnCirkHBYyzorMHsWstJCVobEvBJH4'
});
google.charts.setOnLoadCallback(drawMap);



function drawMap() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Address');
  data.addColumn('string', 'Location');

  data.addRows([
    ['Lake Buena Vista, FL 32830, United States', 'Walt Disney World'],
    ['6000 Universal Boulevard, Orlando, FL 32819, United States', 'Universal Studios'],
    ['7007 Sea World Drive, Orlando, FL 32821, United States', 'Seaworld Orlando']
  ]);

  var options = {
    mapType: 'styledMap',
    zoomLevel: 12,
    showTooltip: true,
    showInfoWindow: true,
    useMapTypeControl: true,
    maps: {
      // Your custom mapTypeId holding custom map styles.
      styledMap: {
        name: 'Styled Map', // This name will be displayed in the map type control.
        styles: [{
            featureType: 'poi.attraction',
            stylers: [{
              color: '#fce8b2'
            }]
          },
          {
            featureType: 'road.highway',
            stylers: [{
              hue: '#0277bd'
            }, {
              saturation: -50
            }]
          },
          {
            featureType: 'road.highway',
            elementType: 'labels.icon',
            stylers: [{
              hue: '#000'
            }, {
              saturation: 100
            }, {
              lightness: 50
            }]
          },
          {
            featureType: 'landscape',
            stylers: [{
              hue: '#259b24'
            }, {
              saturation: 10
            }, {
              lightness: -22
            }]
          }
        ]
      }
    }
  };

  var map = new google.visualization.Map(document.getElementById('map_div'));

  map.draw(data, options);
}

 