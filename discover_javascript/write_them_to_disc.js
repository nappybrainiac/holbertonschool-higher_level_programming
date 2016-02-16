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
        streamToString(res, discWrite);                                 //Obtains the response of the callback res and passes res and discWrite in                         
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

var discWrite = function(jsonString){                                  //Assigning the jsonString a variable called discWrite
    var fs = require('fs');
    fs.writeFile('/tmp/30', jsonString, function (err) {             //using writeFile with 3 variables.
	    if (err) 
		return console.log(err);                               //error message.
	    console.log('The file was saved!');                        //success message.
	});
};