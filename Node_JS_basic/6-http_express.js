const express = require('express');

const app = express();
const PORT = 1245;

// Responde con 'Hello Holberton School!' en la ruta raíz
app.get('/', (_, res) => {
  res.send('Hello Holberton School!');
});

// Iniciar el servidor en el puerto especificado
app.listen(PORT, () => {
  console.log(`Server listening at http://localhost:${PORT}`);
});

module.exports = app;
