const express = require("express");
const router = express.Router();
const { getStats, getChartData } = require("../controllers/dashboardController");

router.get("/stats", getStats);
router.get("/chart", getChartData);

module.exports = router;
