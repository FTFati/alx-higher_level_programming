#!/usr/bin/node
// JS script to define a class, extends to another class

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
