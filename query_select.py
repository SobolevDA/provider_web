from models_db import database, Service
from models_db import Discount as DIS
from models_db import LinkCustomerService as LCS

database.connect()

service_customer = Service.select(Service.id, Service.name).where(Service.id << (97, 59, 58, 47, 50, 48, 46, 153, 49, 137))


def count(begin_date, end_date, service_id):
    count = []
    count_discount = (DIS.select(DIS.link_customer_service).where((DIS.discount_time > begin_date) 
                  & (DIS.discount_time < end_date) 
                 & (DIS.link_customer_service << (LCS.select(LCS.id).where((LCS.service == service_customer) 
                  & (LCS.link_time < end_date) & (LCS.unlink_time >> None) 
                   & (LCS.is_deleted >> None))))))
    
    for i in count_discount:
        count.append(i)
    return len(count)