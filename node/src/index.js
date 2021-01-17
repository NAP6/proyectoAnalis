const express = require("express");
const app = express();

//Se crea un servidor http a partir de la libreria express
const http = require("http").Server(app);

//Para generar la comunicacion se utiliza socker.io
const io = require("socket.io")(http);
require("socketio-auth")(io, {
  authenticate: authenticate,
});

function authenticate(socket, data, callback) {
  var username = data.username;
  var password = data.password;

  if (false) return callback(new Error("El usuario no existe"));
  return callback(null, "1234" == password);
}

io.on("connection", (socket) => {
  socket.on("pythonServer", (data) => {
    socket.broadcast.emit("pythonServer", data);
  });
  socket.on("client", (data) => {
    socket.broadcast.emit(data.username, data);
  });
});

// Rutas del servidor
app.get("/", (req, res) => {
  res.sendfile(__dirname + "\\public\\web\\demo\\index.html");
  //res.redirect("index.html");
});

//Donde se van a cargar los html del servidor
app.use(express.static(__dirname + "/public"));

http.listen(80, () => {
  console.log("Servidor corriendo en el puerto 80");
});
