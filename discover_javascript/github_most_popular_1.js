var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Nappybrainiac',
	'Authorization': 'token 1ab58e09acd3842b931cdac369651f59fbc83f43'
    }
};

var req = https.request(options, function(res) {
	//console.log(res.statusCode);
	res.on('data', function(d) {
		process.stdout.write(d);
		});
	});

req.end();

req.on('error', function(e) {
	console.error(e);
    });