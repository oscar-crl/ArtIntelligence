var express = require('express');
var router = express.Router();
const generator = require('../generator/generator.controller');

/* GET home page. */
router.post('/', generator.create);
router.get('/id', generator.get);

module.exports = router;
