class GeoVictoria():

    import datetime as dt

    yesterday = dt.datetime.now().date() + dt.timedelta(days=-1)

    def GetAttendance(
        person:str = None,
        i_date:str = '20221121000000',
        f_date:str = yesterday.strftime('%Y%m%d235959'),
        includeAll:int = 1
    ):

        from requests_oauthlib import OAuth1Session
        import json

        payload = {
            'Range': person,
            'from': i_date,
            'to': f_date,
            'includeAll': includeAll
        }

        with open('connect.json', encoding='utf-8') as meu_json:
            connect = json.load(meu_json)

        oauthRequest = OAuth1Session(connect['CONSUMER_KEY'],
                        client_secret=connect['CONSUMER_SECRET'])

        link = connect['host']
        url = f'{link}/AttendanceBook/GetAttendance'

        headers = {
                'Accept': connect['Accept-Type'],
                'Accept-Encoding': connect['Accept-Encoding'],
            }

        response = oauthRequest.post(url, json=payload, headers=headers)

        return response.json()


    
    def GetUserList():
        from requests_oauthlib import OAuth1Session

        import json

        with open('connect.json', encoding='utf-8') as meu_json:
            connect = json.load(meu_json)

        oauthRequest = OAuth1Session(connect['CONSUMER_KEY'],
                            client_secret=connect['CONSUMER_SECRET'])

        link = connect['host']
        url = f'{link}/User/List'

        headers = {
                'Accept': connect['Accept-Type'],
                'Accept-Encoding': connect['Accept-Encoding'],
            }

        response = oauthRequest.post(url, headers=headers)

        return response.json()



    def GetPermissions(
        person:str = None,
        i_date:str = '20221121000000',
        f_date:str = yesterday.strftime('%Y%m%d235959'),
        includeAll:int = 1
    ):

        from requests_oauthlib import OAuth1Session
        import json

        payload = {
            'Range': person,
            'from': i_date,
            'to': f_date,
            'includeAll': includeAll
        }

        with open('connect.json', encoding='utf-8') as meu_json:
            connect = json.load(meu_json)

        oauthRequest = OAuth1Session(connect['CONSUMER_KEY'],
                        client_secret=connect['CONSUMER_SECRET'])

        link = connect['host']
        url = f'{link}/Permit/getPermissions'

        headers = {
                'Accept': connect['Accept-Type'],
                'Accept-Encoding': connect['Accept-Encoding'],
            }

        response = oauthRequest.post(url, json=payload, headers=headers)

        return response.json()



    def GetPermissionList():
        from requests_oauthlib import OAuth1Session

        import json

        with open('connect.json', encoding='utf-8') as meu_json:
            connect = json.load(meu_json)

        oauthRequest = OAuth1Session(connect['CONSUMER_KEY'],
                            client_secret=connect['CONSUMER_SECRET'])

        link = connect['host']
        url = f'{link}/Permit/List'

        headers = {
                'Accept': connect['Accept-Type'],
                'Accept-Encoding': connect['Accept-Encoding'],
            }

        response = oauthRequest.post(url, headers=headers)

        return response.json()






















class FolhaPonto():

    def hora_minuto(
        horario:str=None
    ):

        if horario != '--:--':
            if '-' in horario:
                hora = int(horario.split(':')[0].replace('-', ''))
                minuto = int(horario.split(':')[1])
                tempo = int(((hora * 60) + minuto) * -1)
            else:
                hora = int(horario.split(':')[0])
                minuto = int(horario.split(':')[1])
                tempo = int((hora * 60) + minuto)     
        else:
            hora = 0
            minuto = 0
            tempo = int((hora * 60) + minuto)

        return tempo


    def minuto_hora(
        minutos:int=None
    ):

        if minutos > 0:
            hora = int(round(minutos / 60, 2))
            minuto = int(round((round(minutos / 60, 2) - hora) * 60, 0))
            tempo = '{:0>2d}'.format(hora) + ':' + '{:0>2d}'.format(minuto)
        elif minutos < 0:
            time = minutos * -1
            hora = int(round(time / 60, 2))
            minuto = int(round((round(time / 60, 2) - hora) * 60, 0))
            tempo = '-' + '{:0>2d}'.format(hora).replace('-', '') + ':' + '{:0>2d}'.format(minuto).replace('-', '')
        else:
            hora = 0
            minuto = 0
            tempo = '{:0>2d}'.format(hora) + ':' + '{:0>2d}'.format(minuto)

        return f'{tempo}'


    def calculo(
        horarios=None
    ):
        lista_horas = []

        for h in horarios:
            lista_horas.append(FolhaPonto.hora_minuto(h))
        
        return FolhaPonto.minuto_hora(sum(lista_horas))