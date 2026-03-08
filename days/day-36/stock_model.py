

class StockInfo:
    def __init__(self, current_price:float, previous_pricce:float, change_percentage:float):
        self.current_price = current_price
        self.previous_price = previous_pricce
        self.change_percentage = change_percentage

class CompanyNews:
    def __init__(self, source:str, author:str, title:str, description:str):
        self.source = source
        self.author = author
        self.title = title
        self.description = description

    def print_for_message(self):
        return f"From:{self.source} ({self.source})\nTitle:{self.title}\nDescription:{self.description}\n"

    def __str__(self):
        return f"{self.source} {self.author} {self.title} {self.description}"

    def __repr__(self):
        return self.__str__()