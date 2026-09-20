const mongoose = require("mongoose");

function connectDB() {
  mongoose.connect(process.env.MONGODB_URI || "mongodb://localhost:27017/fraud_detection")
    .then(() => console.log("MongoDB Connected"))
    .catch((err) => console.log("MongoDB Connection Error:", err.message));
}

module.exports = connectDB;
