#!/usr/bin/node
// To read file

const filesys = require('fs');
filesys.reaFile(process.argv[2],
'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
