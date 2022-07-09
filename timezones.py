from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("La fecha y hora en Colombia es: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("La fecha y hora en Mexico es: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

venezuela_timezone = pytz.timezone("America/Caracas")
venezuela_date = datetime.now(venezuela_timezone)
print("La fecha y hora en Venezuela es: ", venezuela_date.strftime("%d/%m/%Y, %H:%M:%S"))

