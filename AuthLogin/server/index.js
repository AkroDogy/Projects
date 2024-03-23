require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connection = require('./db')
const userRoutes = require('./routes/users');
const authRoutes = require('./routes/auth');
const app = express();

//middleware
connection();

app.use(express.json());
app.use(cors());


app.use('/api/users', userRoutes);
app.use('/api/auth', authRoutes);

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
  console.log(`http://localhost:${port}`);
  console.log("--------------------------")
});
