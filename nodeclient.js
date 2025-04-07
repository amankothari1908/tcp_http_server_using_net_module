const net = require("net");

const client = net.createConnection({ port: 8080 }, () => {
  console.log("client connected");
  client.write("hello from node client");
});

client.on("data", (serverData) => {
  console.log("server data", serverData.toString());
});
