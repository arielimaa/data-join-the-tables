# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/ecommerce.sqlite')

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    db = conn.cursor()
    query= """SELECT o.OrderID , c.ContactName , e.FirstName
    FROM Orders o
    JOIN Customers c ON o.CustomerID = c.CustomerID
    JOIN Employees e  ON o.EmployeeID  = e.EmployeeID
    """
    call= db.execute( query)
    result = call.fetchall()
    return result


def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    db = conn.cursor()
    query= """SELECT c.ContactName ,
    SUM((od.UnitPrice * od.Quantity)) as total
    FROM OrderDetails od
    JOIN Orders o  ON od.OrderID = o.OrderID
    JOIN Customers c ON o.CustomerID  = c.CustomerID
        GROUP BY c.ContactName
    ORDER BY total
    """
    call= db.execute( query)
    result = call.fetchall()
    return result


def best_employee(db):
    '''Implement the best_employee method to determine who's the best employee!
    By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like:
    ('FirstName', 'LastName', 6000 (the sum of all purchase)).
    The order of the information is irrelevant'''
    db = conn.cursor()
    query= """SELECT e.FirstName, e.LastName,
    SUM((od.UnitPrice * od.Quantity)) as total_sold
    FROM OrderDetails od
    JOIN Orders o  ON od.OrderID = o.OrderID
    JOIN Employees e  ON o.EmployeeID  = e.EmployeeID
    GROUP BY e.EmployeeID
    ORDER BY total_sold DESC
    """
    call= db.execute( query)
    result = call.fetchall()
    return result[0]


def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    db = conn.cursor()
    query=  """SELECT
    Customers.ContactName,
    COUNT(Orders.OrderID) AS order_amount
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    GROUP BY Customers.CustomerID
    ORDER BY order_amount ASC
    """
    call= db.execute( query)
    result = call.fetchall()
    return result
