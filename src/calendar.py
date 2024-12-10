import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=8,
    border=1,
)

qr.add_data('''
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:Lunchtime meeting
DTSTART;TZID=America/New_York:20230420T120000
DURATION:PT1H
LOCATION:Meeting Room 1
END:VEVENT
END:VCALENDAR
''')

img = qr.make_image(fill_color="black", back_color="white")
img.save("output/cal.png")
