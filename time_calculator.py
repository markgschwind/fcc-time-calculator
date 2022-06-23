def add_time(start, duration, day=False):
  '''
  Code seems to be working properly although I am 
  having some trouble with the printing for self 
  confirmation with the unittest feature where periods 
  are added before every printout
  '''

  adddays = 0
  shours, smins = start.split(':')
  durhours, durmins = duration.split(':')
  smins, meridiem = smins.split(' ')

  hrs = int(shours)
  mins = int(smins)
  dhrs = int(durhours)
  dmins = int(durmins)
  mrdm = meridiem.lower().strip()

  summins = mins + dmins
  sumhrs = hrs + dhrs

  #convert total minutes into hrs
  if summins >= 60:
    sumhrs = sumhrs + int(summins / 60)
    summins = int(summins % 60)

  #if there is a time delta
  if dhrs or dmins:
    if mrdm == 'pm' and sumhrs > 12:
      if sumhrs % 24 >= 1.0:
        adddays +=1

    if sumhrs >= 12:
      remhours = sumhrs / 24
      adddays += int(remhours)

    thrs = sumhrs

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
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday']

  if day:
    day = day.strip().title()
    selected_day = int((daysofweek.index(day) + adddays) % 7)
    current_day = daysofweek[selected_day]
    results += f', {current_day} {dayslater(adddays)}'
  else: # add days later
    results = " ".join((results, dayslater(adddays)))
  return results.strip()
  
  

def dayslater(ndays):
  '''
  Function to determine the in parenthesis portion of the answer
  '''
  if ndays == 1:
    return '(next day)'
  elif ndays > 1:
    return '({} days later)'.format(ndays)
  return ''
