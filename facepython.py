import unirest




response = unirest.post('https://insta-profile.p.rapidapi.com/{instagram-schoolboykeyww}',
  headers={
    "X-RapidAPI-Key": '32be3c67femsh24a041bcf349d60p1a11d7jsnef5ae0c2c519',
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params={
    "image_url": "https://www.instagram.com/schoolboykeyww/"
  }
)

response.code # The HTTP status code
response.headers # The HTTP headers
response.body # The parsed response
response.raw_body # The unparsed response


print(response.raw_body)