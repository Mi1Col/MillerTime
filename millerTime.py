import datetime as dt

def millerTime(bornDate, returnType='return'):
    currentDate = dt.date.today()
    bornDate = dt.datetime.strptime(bornDate, "%d/%m/%Y").date()

    differenceD = currentDate - bornDate # Esta en dias
    differenceYears = differenceD.days / 365 # Esta en años

    differenceMillerH = differenceYears / 7

    totalSeconds = differenceMillerH * 3600 # Esta en segundos

    totalHours = totalSeconds / 3600
    hours = int(totalSeconds // 3600) # Horas

    totalMinutes = (totalSeconds % 3600) / 60 
    minutes = int((totalSeconds % 3600) // 60) # Minutos

    seconds = int(totalSeconds % 60) # Segundos

    result = f"Han pasado: {hours} horas, {minutes} minutos y {seconds} segundos."
    
    if returnType == 'totalSeconds':
        return totalSeconds
    elif returnType == 'totalHours':
        return totalHours
    elif returnType == 'hours':
        return hours
    elif returnType == 'totalMinutes':
        return totalMinutes
    elif returnType == 'minutes':
        return minutes
    elif returnType == 'seconds':
        return seconds
    elif returnType == 'result':
        return result
    else:
        raise ValueError("Tipo de retorno no válido. Use 'totalSeconds', 'hours', 'minutes', 'seconds' o 'result'.")

