def open_or_senior(data):
  result = []
  for dupla in data:
    if dupla[0] >= 55 and dupla[1] > 7:
      result.append("Senior")
    else:
      result.append("Open")
  
  return result