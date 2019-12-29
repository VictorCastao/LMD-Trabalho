def Busca_em_Profundidade (vertice):
    Visitados = {
        "Acre" : 0,
        "Alagoas" : 0,
        "Amapá" : 0,
        "Amazonas" : 0,
        "Bahia" : 0,
        "Ceará" : 0,
        "Espírito Santo" : 0,
        "Goiás" : 0,
        "Maranhão" : 0,
        "Mato Grosso" : 0,
        "Mato Grosso do Sul" : 0,
        "Minas Gerais" : 0,
        "Pará" : 0,
        "Paraíba" : 0,
        "Paraná" : 0,
        "Pernambuco" : 0,
        "Piauí" : 0,
        "Rio de Janeiro" : 0,
        "Rio Grande do Norte" : 0,
        "Rio Grande do Sul" : 0,
        "Rondônia" : 0,
        "Roraima" : 0,
        "Santa Catarina" : 0,
        "São Paulo" : 0,
        "Sergipe" : 0,
        "Tocantins" : 0,
        
        
    }

    Lista_Adjacência = {
        "Acre" : ["Amazonas","Rondônia"],
        "Alagoas" : ["Bahia","Pernambuco","Sergipe"],
        "Amapá" : ["Pará"],
        "Amazonas" : ["Acre","Pará","Mato Grosso","Rondônia","Roraima"],
        "Bahia" : ["Alagoas","Espírito Santo","Goiás","Minas Gerais","Pernambuco","Piauí","Sergipe","Tocantins"],
        "Ceará" : ["Paraíba","Pernambuco","Piauí","Rio Grande do Norte"],
        "Espírito Santo" : ["Bahia","Minas Gerais","Rio de Janeiro"],
        "Goiás" : ["Bahia","Mato Grosso","Mato Grosso do Sul","Minas Gerais","Tocantins"],
        "Maranhão" : ["Pará","Piauí","Tocantins"],
        "Mato Grosso" : ["Amazonas","Goiás","Pará","Mato Grosso do Sul","Rondônia","Tocantins"],
        "Mato Grosso do Sul" : ["Goiás","Mato Grosso","Minas Gerais","Paraná","São Paulo"],
        "Minas Gerais" : ["Bahia","Espírito Santo","Goiás","Mato Grosso do Sul","Rio de Janeiro","São Paulo"],
        "Pará" : ["Amapá","Amazonas","Maranhão","Mato Grosso","Roraima","Tocantins"],
        "Paraíba" : ["Ceará","Pernambuco","Rio Grande do Norte"],
        "Paraná" : ["Mato Grosso do Sul","Santa Catarina","São Paulo"],
        "Pernambuco" : ["Alagoas","Bahia","Ceará","Paraíba","Piauí"],
        "Piauí" : ["Bahia","Ceará","Maranhão","Pernambuco","Tocantins"],
        "Rio de Janeiro" : ["Espírito Santo","Minas Gerais","São Paulo"],
        "Rio Grande do Norte" : ["Ceará","Paraíba"],
        "Rio Grande do Sul" : ["Santa Catarina"],
        "Rondônia" : ["Acre","Amazonas","Mato Grosso"],
        "Roraima" : ["Amazonas","Pará"],
        "Santa Catarina" : ["Paraná","Rio Grande do Sul"],
        "São Paulo" : ["Mato Grosso do Sul","Minas Gerais","Paraná","Rio de Janeiro"],
        "Sergipe" : ["Alagoas","Bahia"],
        "Tocantins" : ["Bahia","Goiás","Maranhão","Mato Grosso","Pará","Piauí"],
        
    }
    Resultado_Busca1 = []
    def auxiliar(v):
        Visitados[v] = 1
        Resultado_Busca1.append(v)
        for i in Lista_Adjacência[v]:
            if Visitados[i] == 0:
                auxiliar(i)
    auxiliar(vertice)

    return Resultado_Busca1
        

def Busca_em_Largura (vertice):
    Visitados = {
        "Acre" : 0,
        "Alagoas" : 0,
        "Amapá" : 0,
        "Amazonas" : 0,
        "Bahia" : 0,
        "Ceará" : 0,
        "Espírito Santo" : 0,
        "Goiás" : 0,
        "Maranhão" : 0,
        "Mato Grosso" : 0,
        "Mato Grosso do Sul" : 0,
        "Minas Gerais" : 0,
        "Pará" : 0,
        "Paraíba" : 0,
        "Paraná" : 0,
        "Pernambuco" : 0,
        "Piauí" : 0,
        "Rio de Janeiro" : 0,
        "Rio Grande do Norte" : 0,
        "Rio Grande do Sul" : 0,
        "Rondônia" : 0,
        "Roraima" : 0,
        "Santa Catarina" : 0,
        "São Paulo" : 0,
        "Sergipe" : 0,
        "Tocantins" : 0,
        
        
    }

    Lista_Adjacência = {
        "Acre" : ["Amazonas","Rondônia"],
        "Alagoas" : ["Bahia","Pernambuco","Sergipe"],
        "Amapá" : ["Pará"],
        "Amazonas" : ["Acre","Pará","Mato Grosso","Rondônia","Roraima"],
        "Bahia" : ["Alagoas","Espírito Santo","Goiás","Minas Gerais","Pernambuco","Piauí","Sergipe","Tocantins"],
        "Ceará" : ["Paraíba","Pernambuco","Piauí","Rio Grande do Norte"],
        "Espírito Santo" : ["Bahia","Minas Gerais","Rio de Janeiro"],
        "Goiás" : ["Bahia","Mato Grosso","Mato Grosso do Sul","Minas Gerais","Tocantins"],
        "Maranhão" : ["Pará","Piauí","Tocantins"],
        "Mato Grosso" : ["Amazonas","Goiás","Pará","Mato Grosso do Sul","Rondônia","Tocantins"],
        "Mato Grosso do Sul" : ["Goiás","Mato Grosso","Minas Gerais","Paraná","São Paulo"],
        "Minas Gerais" : ["Bahia","Espírito Santo","Goiás","Mato Grosso do Sul","Rio de Janeiro","São Paulo"],
        "Pará" : ["Amapá","Amazonas","Maranhão","Mato Grosso","Roraima","Tocantins"],
        "Paraíba" : ["Ceará","Pernambuco","Rio Grande do Norte"],
        "Paraná" : ["Mato Grosso do Sul","Santa Catarina","São Paulo"],
        "Pernambuco" : ["Alagoas","Bahia","Ceará","Paraíba","Piauí"],
        "Piauí" : ["Bahia","Ceará","Maranhão","Pernambuco","Tocantins"],
        "Rio de Janeiro" : ["Espírito Santo","Minas Gerais","São Paulo"],
        "Rio Grande do Norte" : ["Ceará","Paraíba"],
        "Rio Grande do Sul" : ["Santa Catarina"],
        "Rondônia" : ["Acre","Amazonas","Mato Grosso"],
        "Roraima" : ["Amazonas","Pará"],
        "Santa Catarina" : ["Paraná","Rio Grande do Sul"],
        "São Paulo" : ["Mato Grosso do Sul","Minas Gerais","Paraná","Rio de Janeiro"],
        "Sergipe" : ["Alagoas","Bahia"],
        "Tocantins" : ["Bahia","Goiás","Maranhão","Mato Grosso","Pará","Piauí"],
        
    }
    Resultado_Busca = []
    Fila = []
    Visitados[vertice] = 1
    Resultado_Busca.append(vertice)
    Fila.append(vertice)
    while (len(Fila)) > 0:
        for i in Lista_Adjacência[Fila[0]]:
            if Visitados[i] == 0:
                Visitados[i] = 1
                Resultado_Busca.append(i)
                Fila.append(i)
        Fila.pop(0)
    return Resultado_Busca
      
    
