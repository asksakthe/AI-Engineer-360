# calculate totals, averages, and identify extremes from a dataset

data = [1200, 3400, 560, 4500, 2100]

class Calculate_totals_and_averages:
    def __init__(self, data):
        self.data = data    

    def total_sales(self):
        self.total = sum(self.data)
        return self.total
    
    def average_sales(self):
        self.no_of_sales =len(self.data)
        self.average = sum(self.data) / self.no_of_sales
        return self.average
    
    def higest_saleData(self):
        self.high_value = max(self.data)
        return self.high_value
    
    def low_saleData(self):
        self.min_sale = min(self.data)
        return self.min_sale
    

day_wise_sales = Calculate_totals_and_averages(data)

print(f"Total Sales: {day_wise_sales.total_sales()}")
print(f"Average Sales on day: {day_wise_sales.average_sales()}")
print(f"Total Sales: {day_wise_sales.higest_saleData()}")
print(f"Total Sales: {day_wise_sales.low_saleData()}")