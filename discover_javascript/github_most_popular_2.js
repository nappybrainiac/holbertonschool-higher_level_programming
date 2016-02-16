var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
        'User-Agent': 'Nappybrainiac',
        'Authorization': 'token 1ab58e09acd3842b931cdac369651f59fbc83f43' //token taken from GitHub for authentication.
    }
};

var req = https.request(options, function(res) {
	streamToString(res, longString);                                 //Obtains the response of the callback res and passes res and longstring in 
    });                                                                  //the function streamToString.


req.end();                                                               //Ends request.

req.on('error', function(e) {                                            //Error message.
        console.error(e);
    });

function streamToString(stream, cb) {                                   //Function that turns the Stream into a string
    const chunks = [];
    stream.on('data', (chunk) => {
	    chunks.push(chunk);
	});
    stream.on('end', () => {
	    cb(chunks.join(''));
	});
}

var longString = function(jsonString){                                  //The closure longstring is assigned the function jsonString.                                  
    console.log(typeof jsonString);
    console.log(jsonString);
}

