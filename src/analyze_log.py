import csv
from typing import Dict, List, Set


path = "data/orders_1.csv"

def analyze_log(path_to_file: str):
    logs: List[list]
        
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")         

    try:
        with open(path_to_file, "r") as file:
            logs = list(csv.reader(file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    clients_data: Dict = {}

    days_of_week: Set = set()

    orders: Set = set()

    for log in logs:
        
        days_of_week.add(log[2])
        orders.add(log[1])

        if log[0] in clients_data:
            if log[1] in clients_data[log[0]]["orders"]:
                clients_data[log[0]]["orders"][log[1]] += 1
            else:
                clients_data[log[0]]["orders"][log[1]] = 1

            if log[2] in clients_data[log[0]]["days"]:
                pass
            else:
                clients_data[log[0]]["days"][log[2]] = True
        else:
            clients_data[log[0]] = {
                "orders": { log[1]: 1 },
                "days": { log[2]: True }
            }

    maria_more_ordered = max(clients_data["maria"]["orders"], key=clients_data["maria"]["orders"].get)

    arnaldo_hamburguer_order_qtd = clients_data["arnaldo"]["orders"]["hamburguer"]
    
    joao_orders = set(clients_data["joao"]["orders"])
    
    joao_days_go_to_cafeteria = set(clients_data["joao"]["days"])

    orders_joao_never_ordered = orders.difference(joao_orders)
    
    days_joao_never_go_to_cafeteria = days_of_week.difference(joao_days_go_to_cafeteria)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{maria_more_ordered}\n"
            f"{arnaldo_hamburguer_order_qtd}\n"
            f"{orders_joao_never_ordered}\n"
            f"{days_joao_never_go_to_cafeteria}"
        )

