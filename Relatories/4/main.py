from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer


product_analyzer = ProductAnalyzer()

total_sales_per_day = product_analyzer.total_sales_per_day()
writeAJson(total_sales_per_day, "total_sales_per_day")

most_sold_product = product_analyzer.most_sold_product()
writeAJson(most_sold_product, "best_selling_product")

customer_highest_spending = product_analyzer.customer_highest_spending()
writeAJson(customer_highest_spending, "customer_with_the_highest_spending_in_a_single_purchase")

products_sold_above_quantity = product_analyzer.products_sold_above_quantity()
writeAJson(products_sold_above_quantity, "products_sold_in_quantities_above_one")
