"""
Logistics Planning Packaging Module

"""

# 1.
def log_cost(a_price, b_price):
    """
    Calculates the logistics packaging cost
    
    :param a_price: a-pricing cost(expected to be a float)
    :param b_price: b-pricing cost(expected to be a float)
    :return: the total packaging cost(expected to be a float)
    """
    pack_cost = a_price + b_price
    return pack_cost


# 2.    
def log_cost_per_part(a_price, b_price, lot_size):
    """
    Calculates the logistics cost per part for the a-price and b-price
    
    :param a_price: a-pricing cost(expected to be a float)
    :param b_price: b-pricing cost(expected to be a float)
    :param lot_size: lot size of package(expected to be an integer)
    :return: logistics cost per part(expected to be a string)
    """
    a = a_price / lot_size
    b = b_price / lot_size
    return f"A-Price: {a},\nB-Price: {b}"


# 3.
def daily_demand(annual_demand):
    """
    Calculates the daily demand required for a part
    
    :param annual_demand: the total parts required in a year(expected to be an integer)
    :return: the average demand per day(expected to be a float)
    """
    demand_per_day = annual_demand / 365
    return f"{demand_per_day:.2f}"
    
# 4.
def rental_bin_pipeline_cost(supplier_rate, days_at_supplier, in_transit, rpsp_rate, days_at_premise, in_transit_back, days_at_rpsp_depot):
    """
    Calculates the total expected cost of a rental bin in a full cycle(pipeline)
    
    :param supplier_rate: the daily rate that the supplier charges(expected to be a float)
    :param days_at_supplier: total days the bin stays at the supplier(expected to be an integer)
    :param in_transit: total days the bin took to arrive on premise(expected to be an integer)
    :param rpsp_rate: the daily rate that the rpsp charges(expected to be a float)
    :param days_at_premise: total days that the bin stays on premise(expected to be an integer)
    :param in_transit_back: total days that the bin took to arrive at rpsp depot(expected to be an integer)
    :param days_at_rpsp_depot: total days that the bin stays at rpsp depot(expected to be an integer)
    :return: the total cost and total days in the pipeline(expected to be a string)
    """
    cost = (supplier_rate *(in_transit + days_at_supplier)) + (rpsp_rate * (in_transit_back + days_at_premise))
    tot_days = days_at_supplier + in_transit + in_transit_back + days_at_premise + days_at_rpsp_depot
    return f"Cost: {cost},\nTotal Days: {tot_days}"

# 5.
def lcl_cost(box_length, box_width, box_height, num_boxes, tare_weight, freight_rate):
    """
    Calculates the expected cost of transporting cargo using LCL Method
    
     :param box_length: the box length(expected to be an integer)
     :param box_width: the box width(expected to be an integer)
     :param box_height: the box height(expected to be an integer)
     :param num_boxes: total number of boxes shipped(expected to be an integer)
     :param tare_weight: the gross weight for each box(expected to be a float)
     :param freight_rate: the rate charged by freight company(expected to be a float)
     :return: the expected cost(expected to be a string)
    """
    box_volume = box_length * box_width * box_height * num_boxes
    weight_ton = (tare_weight * num_boxes)/ 1000
    cost = max(box_volume * freight_rate, weight_ton * freight_rate)
    return f"Cost: {cost}"

# 6.
def tot_boxes_in_container(box_length, box_width, box_height, container_type):
    """
    Calculates the total no. of boxes that can fit into a container
    
    :param box_length: the box length(expected to be an integer)
    :param box_width: the box width(expected to be an integer)
    :param box_height: the box height(expected to be an integer)
    :param container_type: indicates the type of container that will be used["20ft", "40ft", "40hc"](expected to be a string)
    :return: key metrics(expected to be a string)
    """
    num_width = 2350 // box_width
    if container_type == "20ft":
        num_length = 5896 // box_length
        num_height = 2385 // box_height
        tot_boxes = num_length * num_width * num_height
        return f"Total Boxes: {tot_boxes}, \nAlong Length: {num_length}, \nAlong Width: {num_width}, \nAlong Height: {num_height}"
    elif container_type == "40ft":
        num_length = 12035 // box_length
        num_height =  2385 // box_height
        tot_boxes = num_length * num_width * num_height
        return f"Total Boxes: {tot_boxes}, \nAlong Length: {num_length}, \nAlong Width: {num_width},\nAlong Height: {num_height}"
    elif container_type == "40hc":
        num_length = 12035 // box_length
        num_height = 2697 // box_height
        tot_boxes = num_length * num_width * num_height
        return f"Total Boxes: {tot_boxes}, \nAlong Length: {num_length}, \nAlong Width: {num_width}, \nAlong Height: {num_height}"
    else:
        return "Invalid Entry"

# 7.
def tot_inserts_per_day(annual_demand, lot_size, inserts_per_bin, total_production_days = 365):
    """
    Calculates the total inserts required per day
    
    :param annual_demand: total parts needed for 1 year(expected to be an integer)
    :param lot_size: lot size of a part(expected to be an integer)
    :param inserts_per_bin: total inserts used per bin(expected to be an integer)
    :param total_production_days: total days of expected production(expected to be an integer)
    :return: the total inserts required per day(expected to be a string)
    """
    tot_bins = annual_demand / lot_size
    tot_bins_per_day = tot_bins / total_production_days
    inserts_required = tot_bins_per_day * inserts_per_bin
    return f"Inserts required per day: {inserts_required:.2f}"

# 8.
def inventory_turnover_ratio(cogs, opening_stock, closing_stock):
    """
    Calculates how quickly inventory is sold and restocked
    
    :param cogs: cost of goods sold(expected to a float)
    :param opening_stock: opening stock(expected to be an integer)
    :param closing_stock: closing stock(expected to be an integer)
    :return: ratio(expected to be a float)
    """
    ratio = cogs /((opening_stock - closing_stock) / 2)
    return ratio

# 9.
def days_of_inventory_on_hand(avg_inventory_value, cogs):
    """
    Calculates how many days it takes, on average, to sell the entire inventory.
    
    :param avg_inventory_value: the average inventory value(expected to be a float)
    :param cogs: cost of goods sold(expected to be a float)
    :return: days of inventory on hand(expected to be a float)
    """
    doh = (avg_inventory_value / cogs) * 365
    return doh


# 10.
def reorder_point(lead_time_demand, safety_stock):
    """
    Indicates when to reorder inventory to avoid stockouts -> Reorder Point
    
    :param lead_time_demand: lead time demand
    :param safety_stock:
    """
    rop = (lead_time_demand * safety_stock) + safety_stock
    return rop
    
# 11.
def service_level_percentage(stockout_rate):
    """
    Calculates the probability of not running out of stock during the lead time.
    
    :param stockout_rate: the stockout rate(expected to be a float)
    :return: the service level(expected to be a string)
    """
    service = (1 - stockout_rate) * 100
    return f"Service Level: {service:.2f}%"
    
# 12.
def tot_cost_ownership(acq_cost, own_cost, post_cost):
    """
    Calculates the total cost of ownership
    
    :param acq_cost: the acquisition cost(expected to be float)
    :param own_cost: the ownership cost(expected to be a float)
    :param post_cost: the post-ownership cost(expected to be a float)
    """
    tco = acq_cost + own_cost + post_cost
    return tco


# 13.
def sc_cost_to_sales_ratio(tot_sc_cost, tot_sales):
    """
    Evaluates the efficiency of the supply chain costs to total sales revenue.
    
    :param tot_sc_cost: total cost in supply chain(expected to be a float)
    :param tot_sales: the total sales(expected to be a float)
    :return: the supply chain cost-to-sales ratio(expected to be a string)
    """
    sc_ratio = round((tot_sc_cost / tot_sales) * 100, 2)
    return f"Supply Chain cost-to-sales Ratio: {sc_ratio}%"
    
# 14.
def lead_time_var(std_lead_time, avg_lead_time):
    """
    Calculates the lead time variability
    
    :param std_lead_time: standard deviation of lead time(exoected to be a float)
    :param avg_lead_time: the average lead time
    :return: the lead time variability
    """
    variability = std_lead_time / avg_lead_time
    return variability
    
# 15.
def perfect_order_rate(num_perfect_orders, tot_num_orders):
    """
    Assesses how well an organization meets customer requirements without errors or delays.
    
    :param num_perfect_orders: the number of perfect orders(expected to be an integer)
    :param tot_num_orders: the total number of orders(expected to be an integer)
    :return: the perfect order rate(expected to be a string)
    """
    order_rate = round((num_perfect_orders / tot_num_orders) * 100, 2)
    return f"Perfect Order Rate: {order_rate}%"


# 16.
def supp_performance_score(quality_score, on_time_delivery_score, cost_score, tot_possible_score):
    """
    Calculates a supplier's overall performance
    
    :param quality_score: the quality score(expected to be a float)
    :param on_time_delivery_score: the score for timely deliveries(expected to be a float)
    :param cost_score: the score on cost(expected to be a float)
    :param tot_possible_score: the highest possible score(expected to be an integer)
    :return: the supplier's overall performance(expected to be a float)
    """
    score = round((quality_score + on_time_delivery_score + cost_score) / tot_possible_score, 2)
    return f"Supplier Performace Score: {score}"


# 17.
def freight_cost_per_unit(tot_freight_cost, tot_units_shipped):
    """
    Calculates the freight cost per unit
    
    :param tot_freight_cost: the total freight cost charged(expected to be a float)
    :tot_units_shipped: the total number of units shipped(expected to be an integer)
    :return: the freight cost per unit(expected to be a float)
    """
    cost_per_unit = round(tot_freight_cost/tot_units_shipped, 2)
    return cost_per_unit


# 18.
def container_utilization(box_length, box_width, box_height, num_boxes, container_type):
    """
    Calculates the total space utilized in a container
    
    Dimensions are entered in millimetres(mm)
    
    :param box_length: the box length(expected to be an integer)
    :param box_width: the box width(expected to be an integer)
    :param box_height: the box height(expected to be an integer)
    :param num_boxes: the total number of boxes in the container(expected to be an integer)
    :param container_type: indicates the type of container that will be used["20ft", "40ft", "40hc"](expected to be a string)
    :return: the container utilization(expected to a string)
    """
    b_volume = box_length * box_width * box_height
    if container_type == "20ft":
        c_volume = 5896 * 2350 * 2385
        utilization = round(((b_volume * num_boxes) / c_volume) * 100, 2)
        empty_space = 100 - utilization
        return f"Container Utilization: {utilization}%, \nEmpty Space: {empty_space}%"
    elif container_type == "40ft":
        c_volume = 12035 * 2350 * 2385
        utilization = round(((b_volume * num_boxes) / c_volume) * 100, 2)
        empty_space = 100 - utilization
        return f"Container Utilization: {utilization}%, \nEmpty Space: {empty_space}%"
    elif container_type == "40hc":
        c_volume = 12035 * 2350 * 2697
        utilization = round(((b_volume * num_boxes) / c_volume) * 100, 2)
        empty_space = 100 - utilization
        return f"Container Utilization: {utilization}%, \nEmpty Space: {empty_space}%"
    else:
        return "Invalid Entry"

# 19.
from random import randint

def box_code_gen(returnable, volume, material):
    """
    Generates a code for any box
    
    Note: if material is cardboard, then returnable should equal False
    
    :param returnable: indicates if a box is returnable(expected to be a boolean)
    :param volume: the volume of a box(expected to be a float)
    :param material: indicates the type of material that will be used["ste" -> steel, "pla" -> plastic, "wood" -> wood, "car" -> cardboard](expected to be a string)
    :return: generates a box code(expected to be a string)
    """
    a = "BX"
    if returnable == True:
        b = "R"
        if volume <= 0.5:
            c = "S"
            if material == "ste":
                d = "STE"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "pla":
                d = "PLA"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "wood":
                d = "WOO"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            else:
                return "Invalid Entry"
        elif volume >= 0.5:
            c = "L"
            if material == "ste":
                d = "STE"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "pla":
                d = "PLA"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "wood":
                d = "WOO"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            else:
                return "Invalid Entry"
        else:
            return "Invalid Entry"
    elif returnable == False:
        b = "D"
        if volume <= 0.5:
            c = "S"
            if material == "car":
                d = "CAR"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "pla":
                passd = "PLA"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "wood":
                passd = "WOO"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            else:
                return "Invalid Entry"
        elif volume >= 0.5:
            c = "L"
            if material == "car":
                d = "CAR"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "pla":
                d = "PLA"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            elif material == "wood":
                d = "WOO"
                e = iter([randint(10, 99) for _ in range(91)])
                f = f"{next(e)}"
                g = "".join([a, b, c, d, f])
                return g
            else:
                return "Invalid Entry"
        else:
            return "Invalid Entry"
    else:
        return "Invalid Entry"
        
# 20.
def pack_opt(annual_demand, milk_run_rate, old_box_length, old_box_width, old_box_height, old_lot, new_box_length, new_box_width, new_box_height, new_lot, /, truck_length = 13.62, truck_width = 2.48, truck_height = 2.70):
    """
    Calculates the savings for packaging optimization
    
    :param annual_demand: the annual demand of parts(expected to be an integer)
    :param milk_run_rate: the milk run rate(expected to be a float)
    
    :param old_box_length: the current box length(expected to be a float)
    :param old_box_width: the current box width(expected to be a float)
    :param old_box_height: the current box height(expected to be a float)
    :param old_lot: the current lot size(expected to be an integer)
    
    :param new_box_length: the proposed box length(expected to be a float)
    :param new_box_width: the proposed box width(expected to be a float)
    :param new_box_height: the proposed box height(expected to be a float)
    :param new_lot: the proposed lot size(expected to be an integer)
    
    :param truck_length: the truck length(expected to be a float)
    :param truck_width: the truck width(expected to be a float)
    :param truck_height: the truck height(expected to be a float)
    
    :return: the potential savings(expected to be a string)
    """
    old_vol = old_box_length * old_box_width * old_box_height
    tot_old_cbm = (old_vol / old_lot) * annual_demand
    tot_old_boxes = annual_demand / old_lot
    old_no_trips = tot_old_boxes /((truck_length // old_box_length) * (truck_width // old_box_length) * (truck_height // old_box_height))
    old_transport_cost = old_no_trips * milk_run_rate
    new_vol = new_box_length * new_box_width * new_box_height
    tot_new_cbm = (new_vol / new_lot) * annual_demand
    tot_new_boxes = annual_demand / new_lot
    new_no_trips = tot_new_boxes /((truck_length // new_box_length) * (truck_width // new_box_length) * (truck_height // new_box_height))
    new_transport_cost = new_no_trips * milk_run_rate
    transport_savings = round(old_transport_cost - new_transport_cost, 2)
    box_savings = round(tot_old_boxes - tot_new_boxes, 2)
    trip_savings = round(old_no_trips - new_no_trips, 2)
    tot_cbm_savings = round(tot_old_cbm - tot_new_cbm, 2)
    return f"Transportation Savings: R{transport_savings},\nTrip Savings: {trip_savings} trips,\nBoxes Savings: {box_savings},\nCBM Savings: {tot_cbm_savings}cbm"

# 21.
def box_opt_savings_kg(annual_demand, old_lot, old_tare_weight, new_lot,new_tare_weight):
    """
    Calculates the total kg savings in box optimization
    
    :param annual_demand: the annual demand(expected to be an integer)
    
    :param old_lot: the current lot size(expected to be an integer)
    :param old_tare_weight: the current tare weight of the box(expected to be a float)
    
    :param new_lot: the proposed lot size(expected to be an integer)
    :param new_tare_weight: the proposed tare weight of the box(expected to be a float)
    
    :return: the calculated savings(expected to be a float)
    """
    savings = ((annual_demand / old_lot) * old_tare_weight) - ((annual_demand / new_lot) * new_tare_weight)
    return savings

# 22.
def pb_weight(length, width, thickness, density):
    """
    Calculates the Weight of a flat plastic bag
    
    :param length: length(expected to be a float)
    :param width: width(expected to be a float)
    :param thickness: thickness(expected to be a float)
    :param density: density(expected to be a float)
    :return: the weight of the flat plastic bag(expected to be a float)
    """
    weight = density * length * width * thickness * 2
    return f"Weight: {weight}g"

# 23.
def container_payload_test(box_length, box_width, box_height, gross_weight, container_type):
    """
    Calculates if the cargo passes the payload test
    
    :param box_length: the box length(expected to be an integer)
    :param box_width: the box width(expected to be an integer)
    :param box_height: the box height(expected to be an integer)
    :param gross_weight: the gross weight of the package(expected to be a float)
    :param container_type: indicates the type of container that will be used["20ft", "40ft", "40hc"](expected to be a string)
    :return: the payload(expected to be a string)
    """
    con_width = 2350
    if container_type == "20ft":
        con_length = 5896
        con_height = 2385
        payload = 29140
        tot_boxes = (con_length // box_length) * (con_width // box_width) * (con_height // box_height)
        max_weight = tot_boxes * gross_weight
        if max_weight > payload:
            return "OVER MAX CAPACITY!"
        else:
            return f"Boxes: {tot_boxes},\n Total Weight: {max_weight}kg,\n Under Maximum Capacity"
    elif container_type == "40ft":
        con_length = 12035
        con_height = 2385
        payload = 29580
        tot_boxes = (con_length // box_length) * (con_width // box_width) * (con_height // box_height)
        max_weight = tot_boxes * gross_weight
        if max_weight > payload:
            return "OVER MAX CAPACITY!"
        else:
            return f"Boxes: {tot_boxes},\n Total Weight: {max_weight}kg,\n Under Maximum Capacity"
    elif container_type == "40hc":
        con_length = 12035
        con_height = 2697
        payload = 28600
        tot_boxes = (con_length // box_length) * (con_width // box_width) * (con_height // box_height)
        max_weight = tot_boxes * gross_weight
        if max_weight > payload:
            return "OVER MAX CAPACITY!"
        else:
            return f"Boxes: {tot_boxes},\n Total Weight: {max_weight}kg,\n Under Maximum Capacity"
    else:
        return "Invalid Entry"

# 24.
def future_packaging_cost(current_value, inflation_rate, tot_years):
    """
    Calculate the future cost of the packaging
    
    :param current_value: the current cost of the packaging(expected to be a float)
    :param inflation_rate: the expected inflation rate(expected to be a float)
    :param tot_years: the total no. of years(expected to be an integer)
    :return: the future cost(expected to be a float)
    """
    future_value = current_value * (1 + inflation_rate) ** tot_years
    return f"{future_value:.2f}"

# 25.
def net_weight(gross_weight, tare_weight):
    """
    Calculates the net weight of a package
    
    :param gross_weight: the gross weight(expected to be a float)
    :param tare_weight: the tare weight(expected to be a float)
    :return: the net weight(expected to be a float)
    """
    nw = gross_weight - tare_weight
    return nw
