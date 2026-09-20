const Transaction = require("../models/transactionModel");
const { getPrediction } = require("../services/mlService");

async function predictTransaction(req, res) {
  const data = req.body;

  const result = await getPrediction(data);

  const transaction = new Transaction({
    amount: data.Amount || 0,
    merchant: data.merchant,
    location: data.location,
    device: data.device,
    prediction: result.prediction,
    score: result.score
  });

  await transaction.save();

  res.json(result);
}

async function listTransactions(req, res) {
  const transactions = await Transaction.find().sort({ createdAt: -1 }).limit(50);
  res.json(transactions);
}

module.exports = { predictTransaction, listTransactions };
