import pyowm

apikey = '32be3c67femsh24a041bcf349d60p1a11d7jsnef5ae0c2c519'
owm = pyowm.OWM(apikey)
observation = owm.



unirest.post("https://faceplusplus-faceplusplus.p.rapidapi.com/facepp/v3/detect?image_url=https%3A%2F%2Fcnet3.cbsistatic.com%2Fimg%2Fgk7d6AQXuqmtPNmnZI2gMaNySyA%3D%2F970x0%2F2018%2F09%2F05%2F7274da05-85a9-4646-b41f-a4b22c597507%2Fcaptain-marvel-brie-larson-1.jpg")
.header("X-RapidAPI-Host", "faceplusplus-faceplusplus.p.rapidapi.com")
.header("X-RapidAPI-Key", "32be3c67femsh24a041bcf349d60p1a11d7jsnef5ae0c2c519")
.header("Content-Type", "application/x-www-form-urlencoded")
.end(function (result) {
  console.log(result.status, result.headers, result.body);
});