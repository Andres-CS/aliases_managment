# from alias import aliasObject
from prettytable import PrettyTable

def printAll(aliasObjs):
    pTable = PrettyTable()
    headers = ["Name","Location","Description","Lines"]
    
    pTable.field_names = headers
    [pTable.add_row([ao.name, ao.location, ao.description, ao.quantity]) for ao in aliasObjs]

    print(pTable)
