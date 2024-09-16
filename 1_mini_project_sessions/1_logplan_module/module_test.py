"""
The following will test the logplan module formulas
"""

# Import the logplan module
import logplan as lp

# Series of tests(or examples)

# 1. Determine the logistics cost of a packaging specification
print(lp.log_cost(12, 34))
print(lp.log_cost(56, 0))
print(lp.log_cost(7.89, 10))


# 2. Determine the logistsics cost per part

print(lp.log_cost_per_part(12, 34, 5))
print(lp.log_cost_per_part(67, 89, 1))
print(lp.log_cost_per_part(0, 11, 4))


# 3. Calculate the daily demand of a part
print(lp.daily_demand(123))
print(lp.daily_demand(365 * 5))
print(lp.daily_demand(0))


# 4. Calculate the total cost of the rental bin in the pipeline
print(lp.rental_bin_pipeline_cost(34.5, 3, 1, 29.34, 6, 1, 2))
print(lp.rental_bin_pipeline_cost(0, 4, 1, 0, 4, 2, 2))
print(lp.rental_bin_pipeline_cost(0, 0, 0, 0, 0, 0, 0))

# 5. Determine the the cost of using the lcl freight method to transport 12 units of cargo
print(lp.lcl_cost(1.00, 1.00, 1.00, 12, 25, 134.5))
print(lp.lcl_cost(1.00, 1.00, 1.00, 12, 0, 134.5))
print(lp.lcl_cost(1.00, 1.00, 1.00, 12, 10000, 134.5))


# 6. Determine the total number of boxes that fit into the container
print(lp.tot_boxes_in_container(1000, 1000, 1000, "20ft"))
print(lp.tot_boxes_in_container(1000, 1000, 1000, "40ft"))
print(lp.tot_boxes_in_container(1000, 1000, 1000, "40hc"))


# 7. Determine the total number of inserts that are being used per day
print(lp.tot_inserts_per_day(123000, 35, 3))
print(lp.tot_inserts_per_day(345000, 30, 2, total_production_days = 256))
print(lp.tot_inserts_per_day(345000, 30, 2, 256))

# 8. Determine the inventory turnover ratio
print(lp.inventory_turnover_ratio(230000, 10000, 30000))
print(lp.inventory_turnover_ratio(50000, 10000, 2000))


# 9. Calculate the days of inventory on hand
print(lp.days_of_inventory_on_hand(350, 205))
print(lp.days_of_inventory_on_hand(10, 100))


# 10. Calculate the reorder point
print(lp.reorder_point(25, 5))
print(lp.reorder_point(35, 5))

# 11. Determine the service level
print(lp.service_level_percentage(0.45))
print(lp.service_level_percentage(0.11))


# 12. Calculate the total cost of ownership
print(lp.tot_cost_ownership(235, 345, 445))
print(lp.tot_cost_ownership(34, 500, 678))


# 13. Supply Chain cost-to-sales Ratio
print(lp.sc_cost_to_sales_ratio(56_000, 100_000))
print(lp.sc_cost_to_sales_ratio(78_000, 150_000))


# 14. Determine the lead time variability
print(lp.lead_time_var(0.34, 21))
print(lp.lead_time_var(0.54, 86))


# 15. Determine the perfect order rate
print(lp.perfect_order_rate(25, 30))
print(lp.perfect_order_rate(10, 87))
print(lp.perfect_order_rate(120, 120))


# 16. Determine the supplier performance score
print(lp.supp_performance_score(12, 20, 19, 75))
print(lp.supp_performance_score(20, 23, 24, 75))
print(lp.supp_performance_score(1, 0, 2, 75))


# 17. Determine the freight cost per unit
print(lp.freight_cost_per_unit(235_000, 48))
print(lp.freight_cost_per_unit(789_134, 67))


# 18. Determine the container utilization
print(lp.container_utilization(1000, 1000, 1000, 20, "20ft"))        
print(lp.container_utilization(1000, 1000, 1000, 38, "40ft"))
print(lp.container_utilization(1000, 1000, 1000, 40, "40hc"))
print(lp.container_utilization(1000, 1000, 1000, 23, "20hc"))


# 19. Generate a box code
print("Returnable Crate: ", lp.box_code_gen(True, 0.45, "wood"))
print("Disposable Box: ", lp.box_code_gen(False, 0.78, "car"))
print("Rental Bin: ", lp.box_code_gen(True, 0.5, "pla"))


# 20. Calculate the expected savings for packaging optimization
print(lp.pack_opt(365000, 94.5, 1, 1, 2, 40, 1, 1, 2, 60))
print(lp.pack_opt(365000, 94.5, 1,1, 2, 40, 1, 1, 2, 60, truck_length = 10, truck_width = 1, truck_height = 2))


# 21. Calculate the box optimization savings in kilograms
print(lp.box_opt_savings_kg(800_000, 22, 56, 24, 56))
print(lp.box_opt_savings_kg(70_000, 88, 125, 90, 125))


# 22. Calculate the weight of a flat plastic bag
print(lp.pb_weight(100, 50, 0.25, 0.74))
print(lp.pb_weight(200, 100, 0.5, 0.98))


# 23. Do a payload test for the following
print("Test 1: \n", lp.container_payload_test(1000, 1000, 1000, 100, "20ft"))
print("Test 2: \n", lp.container_payload_test(1000, 1000, 1000, 650, "40ft"))
print("Test 3: \n", lp.container_payload_test(1000, 1000, 1000, 200, "40hc"))

# 24. Calculate the future packaging cost
print(lp.future_packaging_cost(3500, 0.027, 5))
print(lp.future_packaging_cost(5000, 0.095, 6))


# 25. Calculate the net weight of a package
print(lp.net_weight(456.7, 67.8))
print(lp.net_weight(500, 500))