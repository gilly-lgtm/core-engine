const fs = require('fs');
const path = require('path');

module.exports = class Parser {
  constructor(file) {
    this.file = file;
  }

  read() {
    return new Promise((resolve, reject) => {
      fs.readFile(this.file, 'utf8', (error, data) => {
        if (error) {
          reject(error);
        } else {
          try {
            const content = JSON.parse(data);
            resolve(content);
          } catch (error) {
            reject(error);
          }
        }
      });
    });
  }

  parse(content) {
    return content;
  }
};