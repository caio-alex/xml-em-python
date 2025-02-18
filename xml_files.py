import os
import xml.etree.ElementTree as Et
from datetime import date


class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        """ Lista todos os arquivos XML no diretório """
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory)
                if arq.lower().endswith(".xml")]

    def remove_namespace(self, tree):
        """ Remove namespaces do XML para facilitar a busca """
        for elem in tree.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]  # Remove namespace
        return tree

    def nfe_data(self, xml):
        tree = Et.parse(xml)
        root = self.remove_namespace(tree).getroot()  # Remove namespace

        # DADOS DA NFE
        NFe = self.check_none(root.find("./infNFe/ide/nNF"))
        serie = self.check_none(root.find("./infNFe/ide/serie"))
        data_emissao = self.check_none(root.find("./infNFe/ide/dhEmi"))

        if data_emissao:
            data_emissao = f"{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[:4]}"

        # DADOS EMITENTES
        chave = self.check_none(root.find("./protNFe/infProt/chNFe"))
        cnpj_emitente = self.check_none(root.find("./infNFe/emit/CNPJ"))
        nome_emitente = self.check_none(root.find("./infNFe/emit/xNome"))

        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        valorNfe = self.check_none(root.find("./infNFe/total/ICMSTot/vNF"))
        data_importacao = date.today().strftime('%d/%m/%Y')

        usuario = ''
        data_saida = ''

        itemNota = 1
        notas = []

        for item in root.findall("./infNFe/det"):
            cod = self.check_none(item.find("./prod/cProd"))
            qntd = self.check_none(item.find("./prod/qCom"))
            descricao = self.check_none(item.find("./prod/xProd"))
            unidade_medida = self.check_none(item.find("./prod/uCom"))
            valorProd = self.check_none(item.find("./prod/vProd"))

            dados = [NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
                     valorNfe, itemNota, cod, qntd, descricao, unidade_medida, valorProd,
                     data_importacao, usuario, data_saida]

            notas.append(dados)
            itemNota += 1

        return notas

    def check_none(self, var):
        return "" if var is None else var.text.replace('.', ',')

    def format_cnpj(self, cnpj):
        if cnpj and len(cnpj) == 14:
            return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
        return ""

if __name__ == "__main__":
    xml = Read_xml("C:\\Users\\caio6\\OneDrive\\Área de Trabalho\\Cursos\\sistema_gerenciador")
    all_files = xml.all_files()

    for file in all_files:
        result = xml.nfe_data(file)
        print(result)

