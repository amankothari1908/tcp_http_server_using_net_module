const net = require("net");

const server = net.createServer((socket) => {
  socket.on("data", (clientData) => {
    console.log("data received from client", clientData.toString());
  });
  socket.write("Data received by server");
});

server.listen(8080, () => {
  console.log("new server up on port 8080");
});
