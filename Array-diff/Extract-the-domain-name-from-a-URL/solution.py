def extract_domain(url):
  url = url.replace("www.", "") # replace() remove partes fixas da URL. ficando algo como github.com/carbonfive/raygun
  url = url.replace("http://", "")
  url = url.replace("https://", "") 

  return url.split(".")[0] # ["github", "com/carbonfive/raygun"] [0] pega apenas "github".