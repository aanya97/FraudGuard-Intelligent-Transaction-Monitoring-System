const axios = require("axios");

async function getPrediction(data) {
  const response = await axios.post("http://localhost:8000/predict", data);
  return response.data;
}

module.exports = { getPrediction };
