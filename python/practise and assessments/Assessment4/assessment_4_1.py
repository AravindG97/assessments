import mysql.connector
import logging
logging.basicConfig (filename='assessment_4_1.log',format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO)
db=mysql.connector.connect(host="localhost",username="root",passwd="root",database="practise")
cursor=db.cursor()
cursor.execute("create table if not exists product(id int,product_name text,product_code text,price int)")
cursor.execute("create table if not exists sale(id int,bill_Date date,product_id int,product_quantity int)")

""" decorator works in some cases""
# def my_logger(func):
#     # import logging
#     logging.basicConfig (filename='{}.log'.format (func.__name__),format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO)
#     print(func.__name__)
#     def wrapper():
#         # logging.info("it ran")
#         return func()
#     return wrapper


file=open(r"C:\Users\aravind.gnanasekar\Documents\product.csv")
a=file.read().splitlines()
for x in a:
    b=x.split(",")
    # print(b)
    cursor.execute("insert into product(id ,product_name ,product_code ,price)values(%s,%s,%s,%s)",b)
file.close()
filee=open(r"C:\Users\aravind.gnanasekar\Documents\sale.csv")
b=filee.read().splitlines()
for x in b:
    c=x.split(",")
    # print(c)
    cursor.execute("insert into sale(id ,bill_Date ,product_id ,product_quantity)values(%s,%s,%s,%s)",c)
filee.close()
class assessment:
    # @my_logger
    def max_sold(self):
        logging.info ("selecting from table for max_sold")
        cursor.execute("select product_name,product_code,price from (select product_name,product_code,price,dense_rank()over(order by product_quantity)as rankk from product p join sale s on p.id=s.product_id)as temp where rankk=1")
        a=cursor.fetchall()
        print(a)
        logging.info ("fetching from cursor for max_sold")
        logging.info (a)


    # @my_logger
    def min_sold(self):
        logging.info ("selecting from table for min_sold")
        cursor.execute("select product_name,product_code,price from (select product_name,product_code,price,dense_rank()over(order by product_quantity desc)as rankk from product p join sale s on p.id=s.product_id)as temp where rankk=1")
        a = cursor.fetchall ()
        print (a)
        logging.info ("fetching from cursor for min_sold")
        logging.info (a)

    # @my_logger
    def date_check(self):
        try:
            flag=1
            datee=input("enter the billing date: ")
            cursor.execute("select bill_date from sale")
            dates=cursor.fetchall()
            for x in dates:
                if datee==x:
                    flag=0
            if flag==1:
                raise Exception
            logging.info ("getting date from user for date_check")
            logging.info (datee)
            logging.info ("selecting from table for date_check")
            cursor.execute("select product_name,product_code,price,count(*)as no_of_rows from product p join sale s on p.id=s.product_id where bill_date=%s",(datee,))
            a = cursor.fetchall ()
            print (a)
            logging.info ("fetching from cursor for date_check")
            logging.info (a)
        except Exception:
            logging.info ("exception handeled")
            print("the date does not match with the file")

    # @my_logger
    def prod_code(self):
        prod_code=input("enter the product_code: ")
        logging.info ("getting the user input for prod_code")
        logging.info (prod_code)
        logging.info ("selecting from table for prod_code")
        cursor.execute("select product_name,product_code,price from product p join sale s on p.id=s.product_id where product_code=%s",(prod_code,))
        a=cursor.fetchall()
        logging.info ("fetching from cursor for prod_code")
        if(len(a))==0:
            print("the product does not exist for prod_code")
            logging.info ("empty list")
        else:
            print(a)
            logging.info (" product exists")
            logging.info (a)


    # @my_logger
    def insertion(self):
        try:
            insertion=[4,"bosch speakers","bch-123",12000]
            if(len(insertion))!=4:
                raise IOError
            cursor.execute("insert into product(id ,product_name ,product_code ,price)values(%s,%s,%s,%s)",insertion)

            # logging.basicConfig (filename='{}.log'.format (insertion), format='%(asctime)s %(levelname)-8s %(message)s',
            #                      level=logging.INFO)
            cursor.execute("select * from product")
            logging.info("selecting everything from product for insertion")
            # print(cursor.fetchall())
            a=cursor.fetchall()
            logging.info("fetching from cursor for insertion")
            print(a)
            logging.info(a)
            # logging.basicConfig(filename='{}.log'.format())
        except IOError:
            logging.info ("exception handled")
            print("the table has 4 columns so enter a list with fout record")
obj1=assessment()
obj1.insertion()
obj1.date_check()
obj1.min_sold()
obj1.max_sold()
obj1.prod_code()


db.commit()
db.close()

"""output"""
""" [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000)]
enter the billing date: 2019-05-10
the date does not match with the file
[('JBL Speakers', 'JBL-100', 18600)]
[('YAMAHA Speakers', 'YHT-1840', 26500)]
enter the product_code: jbl-100
[('JBL Speakers', 'JBL-100', 18600)]"""

#log-file
# 2020-02-21 12:53:45,851 INFO     selecting from table
# 2020-02-21 12:53:45,852 INFO     fetching from cursor
# 2020-02-21 12:55:05,436 INFO     selecting everything from product
# 2020-02-21 12:55:05,437 INFO     fetching from cursor
# 2020-02-21 12:55:05,437 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'bosch speakers', 'bch-123', 12000)]
# 2020-02-21 12:55:34,926 INFO     selecting everything from product
# 2020-02-21 12:55:34,927 INFO     fetching from cursor
# 2020-02-21 12:55:34,927 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'bosch speakers', 'bch-123', 12000)]
# 2020-02-21 12:55:41,544 INFO     exception handeled
# 2020-02-21 12:55:41,544 INFO     selecting from table
# 2020-02-21 12:55:41,545 INFO     fetching from cursor
# 2020-02-21 12:55:41,545 INFO     selecting from table
# 2020-02-21 12:55:41,546 INFO     fetching from cursor
# 2020-02-21 12:58:10,335 INFO     selecting everything from product
# 2020-02-21 12:58:10,336 INFO     fetching from cursor
# 2020-02-21 12:58:10,336 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000)]
# 2020-02-21 12:58:15,028 INFO     exception handeled
# 2020-02-21 12:58:15,028 INFO     selecting from table
# 2020-02-21 12:58:15,030 INFO     fetching from cursor
# 2020-02-21 12:58:15,030 INFO     [('JBL Speakers', 'JBL-100', 18600)]
# 2020-02-21 12:58:15,030 INFO     selecting from table
# 2020-02-21 12:58:15,031 INFO     fetching from cursor
# 2020-02-21 12:58:15,031 INFO     [('YAMAHA Speakers', 'YHT-1840', 26500)]
# 2020-02-21 13:00:45,837 INFO     selecting everything from product for insertion
# 2020-02-21 13:00:45,839 INFO     fetching from cursor for insertion
# 2020-02-21 13:00:45,839 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000)]
# 2020-02-21 13:00:51,757 INFO     exception handeled
# 2020-02-21 13:00:51,757 INFO     selecting from table for min_sold
# 2020-02-21 13:00:51,759 INFO     fetching from cursor for min_sold
# 2020-02-21 13:00:51,759 INFO     [('JBL Speakers', 'JBL-100', 18600)]
# 2020-02-21 13:00:51,759 INFO     selecting from table for max_sold
# 2020-02-21 13:00:51,761 INFO     fetching from cursor for max_sold
# 2020-02-21 13:00:51,761 INFO     [('YAMAHA Speakers', 'YHT-1840', 26500)]
# 2020-02-21 17:12:02,872 INFO     selecting everything from product for insertion
# 2020-02-21 17:12:02,893 INFO     fetching from cursor for insertion
# 2020-02-21 17:12:02,894 INFO     [(1, 'SONY LED TV', 'SONY-LED-S43', 58300), (2, 'YAMAHA Speakers', 'YHT-1840', 26500), (3, 'JBL Speakers', 'JBL-100', 18600), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000), (4, 'bosch speakers', 'bch-123', 12000)]
# 2020-02-21 17:12:20,062 INFO     exception handeled
# 2020-02-21 17:12:20,062 INFO     selecting from table for min_sold
# 2020-02-21 17:12:20,064 INFO     fetching from cursor for min_sold
# 2020-02-21 17:12:20,064 INFO     [('JBL Speakers', 'JBL-100', 18600)]
# 2020-02-21 17:12:20,064 INFO     selecting from table for max_sold
# 2020-02-21 17:12:20,065 INFO     fetching from cursor for max_sold
# 2020-02-21 17:12:20,065 INFO     [('YAMAHA Speakers', 'YHT-1840', 26500)]
# 2020-02-21 17:12:27,919 INFO     getting the user input for prod_code
# 2020-02-21 17:12:27,919 INFO     jbl-100
# 2020-02-21 17:12:27,919 INFO     selecting from table for prod_code
# 2020-02-21 17:12:27,920 INFO     fetching from cursor for prod_code
# 2020-02-21 17:12:27,920 INFO      product exists
# 2020-02-21 17:12:27,920 INFO     [('JBL Speakers', 'JBL-100', 18600)]


