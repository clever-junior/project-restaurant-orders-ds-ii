from operator import itemgetter


class TrackOrders:
    def __init__(self):
        self._data = dict()
        self._orders = set()
        self._week_days = set()
    
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._orders.add(order)
        self._week_days.add(day)
    
        if customer in self._data:
            if order in self._data[customer]["orders"]:
                self._data[customer]["orders"][order] += 1
            else:
                self._data[customer]["orders"][order] = 1
            
            if day in self._data[customer]["days"]:
                self._data[customer]["days"][day] += 1
            else:
                self._data[customer]["days"][day] = 1
        else:
            self._data[customer] = { "orders": { order: 1 }, "days": { day: 1 } }

    def get_most_ordered_dish_per_customer(self, customer):
        return max(self._data[customer]["orders"], key=self._data[customer]["orders"].get)

    def get_never_ordered_per_customer(self, customer):
        ordered = set(self._data[customer]["orders"])
        return self._orders.difference(ordered)

    def get_days_never_visited_per_customer(self, customer):
        visited_days = self._data[customer]["days"]
        return self._week_days.difference(visited_days)

    def get_busiest_day(self):
        values = self._data.values()

        days = dict()
        
        for value in values:
            for key in value["days"].keys():
                days.update({ key: value["days"][key] })
        
        return max(days, key=days.get)  
        

    def get_least_busy_day(self):
        values = self._data.values()
            
        days = dict()
    
        for element in values:
            for key in element["days"]:
                value = element["days"][key]

                if key in days:
                    days[key] += 1
                else:
                    days[key] = value

        return min(days, key=days.get)
