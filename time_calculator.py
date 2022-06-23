def add_time(start, duration, day=False):
  '''
  '''
  print(start, duration, day)

  shours, smins = start.split(':')
  durhours, durmins = duration.split(':')
  smins, meridiem = smins.split(' ')

  hrs = int(shours)
  mins = int(smins)
  dhrs = int(durhours)
  dmins = int(durmins)
  mrdm = meridiem.lower().strip()

  sumhrs = hrs + dhrs + int((mins + dmins) / 60)
  summins = int((mins + dmins) % 60)
  #if there is a time delta ensure that days get calculated 
  adddays = 0
  if dhrs or dmins:
    if mrdm == 'pm' and sumhrs > 12:
      if sumhrs % 24 >= 1.0:
        adddays +=1

    if sumhrs >= 12:
      remhours = sumhrs / 24
      adddays += int(remhours)

    thrs = sumhrs

    # decrease total hours, flipping between am/pm until find last meridiem
    while True:
      if thrs < 12:
        break
      if thrs >= 12:
        if mrdm == 'am':
          mrdm = 'pm'
        elif mrdm == 'pm':
          mrdm = 'am'
        thrs -= 12
    
  endhrs = int(sumhrs % 12) or hrs + 1 
  endmins = int(summins % 60)

  results = f'{endhrs}:{endmins:02} {mrdm.upper()}'
  
  
  daysofweek = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday']

  if day:
    day = day.strip().lower()
    selected_day = int((daysofweek.index(day) + adddays) % 7)
    current_day = daysofweek[selected_day]
    results += f', {current_day.title()} {dayslater(adddays)}'
  else: # add days later
    results = " ".join((results, dayslater(adddays)))
  # print(results.strip())
  return results.strip()
  
  

def dayslater(ndays):
  '''
  Function to determine the in parenthesis portion of the answer
  '''
  if ndays == 1:
    return '(next day)'
  elif ndays > 1:
    return '({} days later)'.format(ndays)
  return''
