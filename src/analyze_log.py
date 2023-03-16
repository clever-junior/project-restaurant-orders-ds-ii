import csv
from typing import List


path = "data/orders_1.csv"


def read_csv(path_to_csv):
    if not path_to_csv.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_csv}'")

    try:
        with open(path_to_csv) as csv_file:
            return list(csv.reader(csv_file, delimiter=","))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_csv}")


def write_txt_file(path_to_file, data_to_write: List):
    with open(path_to_file, "w") as txt_file:
        txt_file.write(
            f"{data_to_write[0]}\n"
            f"{data_to_write[1]}\n"
            f"{data_to_write[2]}\n"
            f"{data_to_write[3]}"
        )


def analyze_log(path_to_file: str):
    logs = read_csv(path_to_file)

    days = set()
    orders = set()

    customers_data = dict()

    for customer, order, day in logs:
        days.add(day)
        orders.add(order)

        if customer in customers_data:
            if (
                order in customers_data[customer]["orders"]
                and day in customers_data[customer]["frequency"]
            ):
                customers_data[customer]["orders"][order] += 1
                customers_data[customer]["frequency"][day] += 1
            else:
                customers_data[customer]["orders"][order] = 1
                customers_data[customer]["frequency"][day] = 1
        else:
            customers_data[customer] = {
                "orders": {order: 1},
                "frequency": {day: 1},
            }

    maria_most_ordered_dish = max(
        customers_data["maria"]["orders"],
        key=customers_data["maria"]["orders"].get,
    )

    arnaldo_hamburguer_ordered_quantity = customers_data["arnaldo"]["orders"][
        "hamburguer"
    ]

    joao_never_dished_orders = orders.difference(
        set(customers_data["joao"]["orders"])
    )

    joao_never_visited_days = days.difference(
        set(customers_data["joao"]["frequency"])
    )

    data_to_write = list(
        [
            maria_most_ordered_dish,
            arnaldo_hamburguer_ordered_quantity,
            joao_never_dished_orders,
            joao_never_visited_days,
        ]
    )

    write_path = "data/mkt_campaign.txt"

    write_txt_file(write_path, data_to_write)
