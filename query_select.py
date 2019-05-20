from models_db import Service


service_customer = Service.select(Service.id, Service.name).where(Service.id << (97, 59, 58, 47, 50, 48, 46, 153, 49, 137))
