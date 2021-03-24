times = (
    'Flamengo', 'Internacional', 'Atletico-MG', 'Sao Paulo',
    'Fluminense', 'Gremio','Palmeiras', 'Santos','Atlettico',
    'Bragantino', 'Ceara', 'Corinthians', 'Atletico-GO',
    'Bahia','Sport Recife', 'Fortaleza', 'Vasco da Gama', 
    'Goias', 'Coritiba', 'Botafogo'
)

print('* Os cinco primeiros times sao: ', times[0:5])
print('* Os ultimos 4 times sao: ', times[-4:])
print('* Todos os times em ordem alfabetica: ',sorted(times),end='')
print('* O time do Gremio se encontra na posico: ',times.index('Gremio') +1)
