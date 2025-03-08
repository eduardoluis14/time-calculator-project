def tratamento_horas_e_minutos(start, duration):
    hora = start.split()
    tempo = hora[1].lower()
    minuto = int(hora[0].split(':')[1])
    hora = int(hora[0].split(':')[0])

    if tempo == 'am' and hora == 12:
        hora = 0
    elif tempo == 'pm' and hora != 12:
        hora = hora+12

    duration_tratado = duration.split(':')
    duracao_final = [int(duration_tratado[0]),int(duration_tratado[1])]
    hora_final = [hora,minuto]
    
    return (hora_final,duracao_final)

def soma_hora_e_tempo_corrido(tupla):
    somar_hora = tupla[1][0]
    dias_passados = 0
    if somar_hora >= 24:
        somar_hora = tupla[1][0] % 24
        dias_passados = tupla[1][0]//24
        
    minuto_somado = tupla[0][1]+tupla[1][1]
    minuto_final = minuto_somado%60
        
    hora_final = tupla[0][0] + somar_hora
    
    if minuto_somado >= 60:
        hora_final = hora_final + minuto_somado//60
    
    if hora_final >= 24:
        hora_final = hora_final%24
        dias_passados += 1 
    return hora_final, minuto_final,dias_passados

def verifica_dia_da_semana(dia, dias_corridos):
    lista = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    cont = 1
    for i in lista:
        if i.lower() == dia.lower():
            break
        else:
            cont += 1

    if dias_corridos%7 == 0 or dias_corridos == 0:
        return lista[cont-1]
    
    dia_da_semana_atual = cont + dias_corridos
    
    if dia_da_semana_atual > 6:
        dia_da_semana_atual %= 7

    return lista[dia_da_semana_atual-1]

def trata_hora_padrao_us(tupla_hora_e_tempo_corrido, mostrar_dia=None):
    hora = tupla_hora_e_tempo_corrido[0]
    minuto = tupla_hora_e_tempo_corrido[1]
    dias = tupla_hora_e_tempo_corrido[2]
    hora_final = ''
    
    if minuto < 10:
        minuto = '0'+str(minuto)
    else:
        minuto = str(minuto)
        
    if hora == 0:
        hora_final += '12'+':'+minuto+' AM'
    elif hora == 12:
        hora_final += '12'+':'+minuto+' PM'
    elif hora > 12 and hora != 0:
        hora_final += str(hora%12)+':'+minuto+' PM'
    else:
        hora_final += str(hora)+':'+minuto+' AM'

    if mostrar_dia != None:
        dia_atual = verifica_dia_da_semana(mostrar_dia, dias)
        hora_final += ', '+dia_atual
        

    if dias == 1:
        hora_final += ' (next day)'
    elif dias > 1:
        hora_final += ' ('+str(dias)+' days later)'
    else:
        pass

    return hora_final

def add_time(start, duration, day_of_the_week=None):
    hora_tratada = tratamento_horas_e_minutos(start, duration)
    hora_tratada_padrao_24 = soma_hora_e_tempo_corrido(hora_tratada)
    new_time = trata_hora_padrao_us(hora_tratada_padrao_24,mostrar_dia=day_of_the_week)

    return new_time
