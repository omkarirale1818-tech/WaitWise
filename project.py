import json
from datetime import datetime
from statistics import mean

DATA_FILE = "customers.json"

#=======================================
# PART 1 : CUSTOMER AND TOKEN MANAGEMENT
#=======================================
customers = []

def add_customer(customers, name, token, service):

    customer = {
        "token":token,
        "name":name,
        "service":service,
        "date":datetime.now().isoformat(),
        "status":"waiting"
    }

    customers.append(customer)

    return customer

def get_next_token(customers):

    if not customers:
        return 1

    return max(customer["token"] for customer in customers)+1

#==========================
# PART 2 : QUEUE MANAGEMENT
#==========================

def view_queue(customers):
    waiting_customer = []

    for customer in customers:
        if customer["status"] == "waiting":
            waiting_customer.append(customer)


    if not waiting_customer:
        print("\n The Queue is Empty")
        return

    print("======= CURRENT QUEUE =======")
    print(f"{'Token':<10}{'Name':<20}{'Service':<20}")
    print("-"*50)
    for customer in waiting_customer:
        print(
            f"{customer['token']:<10}"
            f"{customer['name']:<20}"
            f"{customer['service']:<20}"
        )

def serve_next_customer(customers):
    waiting_customer = []

    for customer in customers:
        if customer["status"] == "waiting":

             waiting_customer.append(customer)
             break

    if not waiting_customer:
        return None

    customer = waiting_customer[0]
    print("\n==================== NOW SERVING =======================")
    print(f"Token   :  {customer['token']}")
    print(f"Name    :  {customer['name']}")
    print(f"Service :  {customer['service']}")

    start_time = datetime.now()
    input("\n Press enter when service is completed")
    end_time = datetime.now()
    service_time = (end_time - start_time).total_seconds() / 60
    customer["status"] = "served"
    customer["service_time"] = round(service_time, 2)
    customer["served_time"] = end_time.isoformat()

    print("\n Service Completed")
    print(f"Service Time: {customer['service_time']} minutes")

    return customer

#==================================
# PART 3 : WAITING TIME ESTIMATION
#==================================

def calculate_average_service_time(customers, service=None):

    service_time = []


    for customer in customers:
        if customer["status"] == "served":
            if service is None or customer["service"] == service:
                if "service_time" in customer:
                    service_time.append(customer["service_time"])


    if service_time:
        return round(mean(service_time), 2)



    all_service_time = []

    for customer in customers:
        if customer["status"] == "served":
            if "service_time" in customer:
                all_service_time.append(customer["service_time"])


    if not all_service_time:
        return 5.0

    return round(mean(all_service_time), 2)

def estimate_waiting_time(customers, token):

    waiting_customer = []

    for customer in customers:
        if customer["status"] == "waiting":
            waiting_customer.append(customer)


    target_customer = None

    for customer in waiting_customer:
        if customer["token"] == token:
            target_customer = customer
            break

    if target_customer is None:
        return None

    position = waiting_customer.index(target_customer)

    total_waiting_time = 0

    for customer in waiting_customer[:position]:
        average_time = calculate_average_service_time(customers, customer["service"])
        total_waiting_time += average_time

    return round(total_waiting_time, 2)


#=============================================
# PART 4 : SEARCH,STATISTICS AND DATA STORAGE
#=============================================

def search_customer(customers, search_term):

    results = []

    for customer in customers:
        if (
            search_term.lower() in customer["name"].lower()
            or search_term == str(customer["token"])
        ):
            results.append(customer)

    return results

def show_customer_detail(customers, search_term):

    results = search_customer(customers, search_term)

    if not results:
        print("Customer not found")
        return

    customer = results[0]

    print("\nCustomer deails")
    print("--------------------------")
    print(f"Token   :  {customer['token']}")
    print(f"Name    :  {customer['name']}")
    print(f"Service :  {customer['service']}")
    print(f"Status  :  {customer['status']}")

def show_statistics(customers):

    total = len(customers)

    waiting = 0
    served = 0


    for customer in customers:
        if customer["status"] == "waiting":
            waiting += 1
        elif customer["status"] == "served":
            served += 1


    print("\nWaitWise Statistics")
    print("------------------------")
    print(f"Total Customer      :  {total}")
    print(f"Waiting Customers   :  {waiting}")
    print(f"Served Customers   :  {served}")


def save_data(customers):
    with open(DATA_FILE, "w") as file:
        json.dump(customers, file, indent=4)



def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def handle_add_customer(customers):

    name = input("\n Enter the name : ").strip()

    if not name :
        print("\n Name can't be empty, please enter the name " )
        return

    service = input("\n Enter the service : ")

    if not service :
        print("\n service can't be empty, please enter the service")
        return

    token = get_next_token(customers)

    customer = add_customer(
        customers,
        name,
        token,
        service
    )
    save_data(customers)

    print("\nCustomer added succesfully! ")
    print(f"Token: {customer['token']}")
    print(f"Name: {customer['name']}")
    print(f"Service: {customer['service']}")

    waiting_time = estimate_waiting_time(customers, token)
    print(f"Estimated Waiting Time: {waiting_time} minutes")

def handle_search(customers):

    search_term = input("\n Enter customer name or token: ")

    results = search_customer(customers, search_term)

    if not results:
        print(" Customer not found")
        return

    print("============ Search Result =============" )
    for customer in results:

        print(f"Token: {customer['token']}")
        print(f"Name: {customer['name']}")
        print(f"Service: {customer['service']}")
        print(f"Status: {customer['status']}")

        if customer["status"] == "waiting":
            waiting_time = estimate_waiting_time(customers, customer["token"])
            print(f"Estimated Waiting time: {waiting_time} minutes")

def handle_estimate(customers):

    try:
        token = int(input("\nEnter token number: "))
    except ValueError:
        print("Please enter valid token number")
        return

    waiting_time = estimate_waiting_time(customers, token)

    if waiting_time is None:
        print("Waiting customer is not found")
        return

    print(f"Estimated waiting time: {waiting_time} minutes")


#=======================
# PART 5 : MAIN PROGRAME
#=======================

def main():

    customers = load_data()

    while True :



        print("\n")
        print("=" * 40)
        print("              WAITWISE")
        print("   Queue & Waiting-Time Management")
        print("=" * 40)

        print("\n1. Add Customer")
        print("2. View Current Queue")
        print("3. Serve Next Customer")
        print("4. Estimate Waiting Time")
        print("5. Search Customer")
        print("6. View Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            handle_add_customer(customers)

        elif choice == "2":
            view_queue(customers)

        elif choice == "3":
            customer = serve_next_customer(customers)

            if customer is not None:
                save_data(customers)

        elif choice == "4":
            handle_estimate(customers)

        elif choice == "5":
            handle_search(customers)

        elif choice == "6":
            show_statistics(customers)

        elif choice == "7":
            save_data(customers)
            print("\nThank you for using WaitWise!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()

