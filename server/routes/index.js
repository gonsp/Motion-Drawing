var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/point', function(req, res, next) {
  console.log("DATAPOINT");
  res.send("")
});

module.exports = router;
