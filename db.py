import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1gERuF6n1si0Lnh0AMC6hNywKXBxC8avlM8MTUGkw3kY')
worksheet = sh.sheet1

fallback = worksheet.acell('E2').value

perguntas = 
[worksheet.acell('A2').value,
worksheet.acell('A3').value,
worksheet.acell('A4').value,
worksheet.acell('A5').value,
worksheet.acell('A6').value,
worksheet.acell('A7').value,
worksheet.acell('A8').value,
worksheet.acell('A9').value,
worksheet.acell('A10').value]

respostas = 
[worksheet.acell('B2').value,
worksheet.acell('B3').value,
worksheet.acell('B4').value,
worksheet.acell('B5').value,
worksheet.acell('B6').value,
worksheet.acell('B7').value,
worksheet.acell('B8').value,
worksheet.acell('B9').value,
worksheet.acell('B10').value]

disparidades = 
[worksheet.acell('C2').value,
worksheet.acell('C3').value,
worksheet.acell('C4').value,
worksheet.acell('C5').value,
worksheet.acell('C6').value,
worksheet.acell('C7').value,
worksheet.acell('C8').value,
worksheet.acell('C9').value,
worksheet.acell('C10').value,
worksheet.acell('C11').value,
worksheet.acell('C12').value,
worksheet.acell('C13').value,
worksheet.acell('C14').value,
worksheet.acell('C15').value,
worksheet.acell('C16').value,
worksheet.acell('C17').value,
worksheet.acell('C18').value,
worksheet.acell('C19').value,
worksheet.acell('C20').value,
worksheet.acell('C21').value,
worksheet.acell('C22').value,
worksheet.acell('C23').value,
worksheet.acell('C24').value,
worksheet.acell('C25').value,
worksheet.acell('C26').value,
worksheet.acell('C27').value,
worksheet.acell('C28').value,
worksheet.acell('C29').value,
worksheet.acell('C30').value,
worksheet.acell('C31').value,
worksheet.acell('C32').value,
worksheet.acell('C33').value,
worksheet.acell('C34').value,
worksheet.acell('C35').value,
worksheet.acell('C36').value,
worksheet.acell('C37').value,
worksheet.acell('C38').value,
worksheet.acell('C39').value,
worksheet.acell('C40').value,
worksheet.acell('C41').value,
worksheet.acell('C42').value,
worksheet.acell('C43').value,
worksheet.acell('C44').value,
worksheet.acell('C45').value,
worksheet.acell('C46').value]

respostasd = 
[worksheet.acell('D2').value,
worksheet.acell('D3').value,
worksheet.acell('D4').value,
worksheet.acell('D5').value,
worksheet.acell('D6').value,
worksheet.acell('D7').value,
worksheet.acell('D8').value,
worksheet.acell('D9').value,
worksheet.acell('D10').value,
worksheet.acell('D11').value,
worksheet.acell('D12').value,
worksheet.acell('D13').value,
worksheet.acell('D14').value,
worksheet.acell('D15').value,
worksheet.acell('D16').value,
worksheet.acell('D17').value,
worksheet.acell('D18').value,
worksheet.acell('D19').value,
worksheet.acell('D20').value,
worksheet.acell('D21').value,
worksheet.acell('D22').value,
worksheet.acell('D23').value,
worksheet.acell('D24').value,
worksheet.acell('D25').value,
worksheet.acell('D26').value,
worksheet.acell('D27').value,
worksheet.acell('D28').value,
worksheet.acell('D29').value,
worksheet.acell('D30').value,
worksheet.acell('D31').value,
worksheet.acell('D32').value,
worksheet.acell('D33').value,
worksheet.acell('D34').value,
worksheet.acell('D35').value,
worksheet.acell('D36').value,
worksheet.acell('D37').value,
worksheet.acell('D38').value,
worksheet.acell('D39').value,
worksheet.acell('D40').value,
worksheet.acell('D41').value,
worksheet.acell('D42').value,
worksheet.acell('D43').value,
worksheet.acell('D44').value,
worksheet.acell('D45').value,
worksheet.acell('D46').value]