import datetime as dt

class MillerTime:
    
    def __init__(self, bornDate):
        self.bornDate = dt.datetime.strptime(bornDate, "%d/%m/%Y").date()
        self.operations()

    def operations(self):
        currentDate = dt.date.today()

        differenceDays = currentDate - self.bornDate  # Está en días
        differenceYears = differenceDays.days / 365  # Está en años

        differenceMillerH = differenceYears / 7

        self.totalSeconds = differenceMillerH * 3600  # Está en segundos

        self.totalHours = self.totalSeconds / 3600
        self.hours = int(self.totalSeconds // 3600)  # Horas

        self.totalMinutes = (self.totalSeconds % 3600) / 60 
        self.minutes = int((self.totalSeconds % 3600) // 60)  # Minutos

        self.seconds = int(self.totalSeconds % 60)  # Segundos

        self.result = f"Have passed: {self.hours} hours, {self.minutes} minutes and {self.seconds} seconds."

    def get_total_seconds(self):
        return self.totalSeconds
    
    def get_total_minutes(self):
        return self.totalMinutes

    def get_total_hours(self):
        return self.totalHours
    
    def get_hours(self):
        return self.hours
    
    def get_minutes(self):
        return self.minutes
    
    def get_seconds(self):
        return self.seconds
    
    def get_result(self):
        return self.result

