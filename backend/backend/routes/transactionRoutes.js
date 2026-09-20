const express = require("express");
const router = express.Router();
const { predictTransaction, listTransactions } = require("../controllers/transactionController");

router.post("/predict", predictTransaction);
router.get("/", listTransactions);

module.exports = router;
