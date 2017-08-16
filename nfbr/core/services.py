import http.client
import base64


def consulta_notas():
    conn = http.client.HTTPSConnection("managersaashom.tecnospeed.com.br:7071")

    headers = {
        'authorization': "Basic " + base64.b64encode(bytes('admin:123mudar', 'utf8')).decode('utf8'),
        'cache-control': "no-cache",
    }

    conn.request("GET",
                 "/ManagerAPIWeb/nfce/consulta?Campos=chave%2Csituacao%2Cnnf&Filtro=situacao%3D'REJEITADA'&Ordem=handle%20desc&grupo=edoc&cnpj=08187168000160",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    notas = [({
        "chave": line.split(",")[0],
        "situacao": line.split(",")[1],
        "numero": line.split(",")[2],
    }) for line in data.decode("utf-8").splitlines()]

    return notas
