const mongoose = require("mongoose");

const transactionSchema = new mongoose.Schema({
  amount: Number,
  merchant: String,
  location: String,
  device: String,
  prediction: String,
  score: Number
}, { timestamps: true });

module.exports = mongoose.model("Transaction", transactionSchema);
