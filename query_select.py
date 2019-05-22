from models_db import database, Service, Customer
from models_db import Discount as DIS
from models_db import LinkCustomerService as LCS

database.connect()


service_customer = Service.select(Service.id, Service.name).where(Service.id << (97, 59, 58, 47, 50, 48, 46, 153, 49, 137))

ktv_service = Service.select(Service.id, Service.name).where(Service.id << (99, 100))


def count_dis(begin, end, id):
    dis = []
    count_discount = (DIS.select(DIS.link_customer_service).where((DIS.discount_time > begin) 
                      & (DIS.discount_time < end) 
                      & (DIS.link_customer_service << (LCS.select(LCS.id).where((LCS.service == id) 
                         & (LCS.link_time < end) & (LCS.unlink_time >> None) 
                       & (LCS.is_deleted >> None))))).distinct())
    
    for i in count_discount:
        dis.append(i)
    return len(dis)


def ktv_customer(service_id):
    count_id_ktv = []

    ktv_count_customer = (Customer.select(Customer.id).join(LCS)
                          .where((Customer.id == LCS.customer) & (Customer.is_locked >> None) 
                          & (Customer.is_deleted >> None) 
                          & (LCS.is_deleted >> None) 
                          & (LCS.service == service_id) & (LCS.unlink_time >> None)).distinct())

    for i in ktv_count_customer:
        count_id_ktv.append(i)
    return(len(count_id_ktv))