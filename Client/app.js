function getBathValue() {
  let bathrooms = document.querySelector('input[name="uiBathrooms"]:checked');
  return bathrooms ? parseInt(bathrooms.value) : -1;
}

function getBHKValue() {
  let bhk = document.querySelector('input[name="uiBHK"]:checked');
  return bhk ? parseInt(bhk.value) : -1;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  let sqft = document.getElementById("uiSqft");
  let bhk = getBHKValue();
  let bathrooms = getBathValue();
  let location = document.getElementById("uiLocations");
  let estPrice = document.getElementById("uiEstimatedPrice");

  if (!sqft || bhk === -1 || bathrooms === -1 || !location) {
      estPrice.innerHTML = "<h2>Please enter all details</h2>";
      return;
  }

  let url = window.location.origin + "/predict_home_price";
  console.log("Making API call to:", url);

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value
  }, function(data, status) {
      console.log("API Response:", data);
      // Divide the estimated price by 10 to convert to Lakh
      let formattedPrice = (data.estimated_price / 10).toFixed(1);
      estPrice.innerHTML = "<h2>" + formattedPrice + " Lakh</h2>";
      console.log("API Status:", status);
  }).fail(function(jqXHR, textStatus, errorThrown) {
      console.error("API Error:", textStatus, errorThrown);
      estPrice.innerHTML = "<h2>Error fetching price</h2>";
  });
}

function onPageLoad() {
  console.log("Document loaded");
  let url = window.location.origin + "/get_location_names";
  console.log("Fetching locations from:", url);
  
  $.get(url, function(data, status) {
      console.log("Received location data:", data);
      if (data && data.locations) {
          let uiLocations = document.getElementById("uiLocations");
          uiLocations.innerHTML = '<option value="" disabled selected>Choose a Location</option>';
          data.locations.forEach(location => {
              let opt = new Option(location, location);
              uiLocations.add(opt);
          });
          console.log("Loaded", data.locations.length, "locations");
      } else {
          console.error("Invalid data format received:", data);
      }
  }).fail(function(jqXHR, textStatus, errorThrown) {
      console.error("Failed to load locations:", textStatus, errorThrown);
      let uiLocations = document.getElementById("uiLocations");
      uiLocations.innerHTML = '<option value="" disabled selected>Error loading locations</option>';
  });
}

window.onload = onPageLoad;
