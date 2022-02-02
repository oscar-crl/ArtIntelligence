
exports.create = (req, res) => {
    res.send({okay: req.body.key});
}

exports.get = (req, res) => {
    res.send({okay: req.query.key});
}