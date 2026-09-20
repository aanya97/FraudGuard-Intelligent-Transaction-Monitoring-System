const Transaction = require("../models/transactionModel");

async function getStats(req, res) {
  const total = await Transaction.countDocuments();
  const fraud = await Transaction.countDocuments({ prediction: "Fraud" });
  const normal = total - fraud;

  res.json({
    total,
    fraud,
    normal,
    fraudPercentage: total > 0 ? ((fraud / total) * 100).toFixed(2) : 0
  });
}

async function getChartData(req, res) {
  const transactions = await Transaction.find().sort({ createdAt: -1 }).limit(30);
  res.json(transactions.reverse());
}

module.exports = { getStats, getChartData };
