function getAllParks() {
    if (serverSettings.nestParks) {
        $.getJSON('static/data/parks/' + serverSettings.nestParksFileName + '.json').done(function (response) {
            if (!response || !('parks' in response)) {
                return
            }

            mapData.nestParks = response.parks.map(parkPoints => parkPoints.map(point => L.latLng(point[0], point[1])))

            if (settings.showNestParks) {
                updateNestParks()
            }
        }).fail(function () {
            console.error("Couldn't load nest parks JSON file.")
        })
    }
    
    if (serverSettings.pokemonNests) {
        console.log();   
    }

    if (serverSettings.exParks) {
        $.getJSON('static/data/parks/' + serverSettings.exParksFileName + '.json').done(function (response) {
            if (!response || !('parks' in response)) {
                return
            }

            mapData.exParks = response.parks.map(parkPoints => parkPoints.map(point => L.latLng(point[0], point[1])))

            if (settings.showExParks) {
                updateExParks()
            }
        }).fail(function () {
            console.error("Couldn't load ex parks JSON file.")
        })
    }
}

function updateNestParks() {
    
    if (settings.showNestParks) {
        const bounds = map.getBounds()
        const inBoundParks = mapData.nestParks.filter(parkPoints => {
            return parkPoints.some(point => {
                return bounds.contains(point)
            })
        })

        nestParksLayerGroup.clearLayers()

        inBoundParks.forEach(function (park) {
            L.polygon(park, {color: 'limegreen', interactive: false}).addTo(nestParksLayerGroup)
        })
    }
}

function getNestData(pokemonNestData) {
    
    mapData.pokemoneNests = pokemonNestData;
    //updatePokemonNests()
        
    return true
}

function updatePokemonNests() {
    
    console.log(mapData.pokemonNestData);
    
    var i;
    var iconSize = 32 * (settings.pokemonIconSizeModifier / 100) ;
    var smallIcon = iconSize ; 
    
    pokemonNestsLayerGroup.clearLayers()
    
    data.forEach(function (index, arr) {

        var myIcon = L.icon({
            //iconUrl: 'pkm_img?pkm='+data[i].pokemon_id,
            shadowUrl: 'https://i.imgur.com/46zb5y8.png',
            iconUrl: 'pkm_img?pkm='+data[index].pokemon_id,
            shadowSize: [iconSize, iconSize],
            iconSize: [smallIcon, smallIcon], // size of the shadow
        });
        var inarea = map.getBounds().contains([data[index].lat,data[index].lon]);
        
        var lastUpdated = timeConverter(data[index].updated);
        
        var popup = L.popup({ autoClose: false })
            .setContent(`
                        <div>
                          <div id='pokemon-container'>
                            <div id='pokemon-container-left'>
                              <div id='types'>
                                <strong>` + data[i].pokemonName + `</strong>
                              </div>
                              <div id='pokemon-image'>
                                <img src='pkm_img?pkm=`+data[index].pokemon_id+`' width='64'>
                              </div>
                            </div>
                            <div id='pokemon-container-right'>
                              <div class="parkname"><span style="text-decoration: underline;"><strong>`+data[index].name+`</strong></span></div>
                              <div class='street'>
                                <br><strong>Street :</strong> `+ data[index].street +` <br>
                                <strong>Suburb :</strong> `+ data[index].suburb +`<br>
                              </div>
                              <div class='average'>
                                <br><strong>Average Per Hour :</strong> `+ data[index].pokemon_avg +`
                              </div>
                              <div class='lastupdated'>
                                <br><strong>Last Updated :</strong> `+ lastUpdated +`
                              </div>
                            <div>
                          </div>
                        </div>`)
            
        if (inarea = true) {
            L.marker([data[index].lat, data[index].lon], {icon: myIcon}).bindPopup(popup).openPopup().addTo(pokemonNestsLayerGroup);
        }
    })
    
}

function timeConverter(UNIX_timestamp){
  var ampm;
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
    if (min < 10 && min >= 0) {
        min = '0' + min
    }
    if (hour <12 && hour >= 0) {
        var ampm = 'AM';
    }
    else {
        var ampm = 'PM';
    }
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ' ' + ampm;
  return time;
}

function updateExParks() {
    if (settings.showExParks) {
        const bounds = map.getBounds()
        const inBoundParks = mapData.exParks.filter(parkPoints => {
            return parkPoints.some(point => {
                return bounds.contains(point)
            })
        })

        exParksLayerGroup.clearLayers()

        inBoundParks.forEach(function (park) {
            L.polygon(park, {color: 'black', interactive: false}).addTo(exParksLayerGroup)
        })
    }
}

function updateAllParks() {
    updateNestParks()
    updateExParks()
}
