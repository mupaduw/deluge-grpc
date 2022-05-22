var PROTO_PATH = __dirname + './../deluge_gprc/deluge_dfs.proto';

var parseArgs = require('minimist');
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

var dfs_proto = grpc.loadPackageDefinition(packageDefinition).deluge_dfs;

// node demo_client.js "/Users/chrisbc/Music/DELUGE"
function main() {
  var argv = parseArgs(process.argv.slice(2), {
    string: 'target'
  });
  var target;
  if (argv.target) {
    target = argv.target;
  } else {
    target = 'localhost:50057';
  }
  var client = new dfs_proto.DelugeFolderSystem(target,
                                       grpc.credentials.createInsecure());
  var card_path;
  if (argv._.length > 0) {
    card_path = argv._[0];
  } else {
    card_path = '/';
  }

  client.listFolderSystems({path: card_path}, function(err, response) {
    console.log('listFolderSystems:', response.folder_names);
  });
}

main();
