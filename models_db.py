from peewee import *

database = MySQLDatabase('provider', **{'charset': 'utf8', 'password': 'qwerty', 'use_unicode': True, 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class City(BaseModel):
    account_code = CharField(index=True, null=True)
    name = CharField(unique=True)

    class Meta:
        table_name = 'city'

class StreetType(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'street_type'

class Street(BaseModel):
    account_code = CharField(index=True, null=True)
    city = ForeignKeyField(column_name='city_id', field='id', model=City)
    name = CharField()
    street_type = ForeignKeyField(column_name='street_type_id', field='id', model=StreetType)

    class Meta:
        table_name = 'street'
        indexes = (
            (('name', 'city', 'street_type'), True),
        )

class District(BaseModel):
    city = ForeignKeyField(column_name='city_id', field='id', model=City)
    name = CharField()

    class Meta:
        table_name = 'district'
        indexes = (
            (('city', 'name'), True),
        )

class Address(BaseModel):
    appart = IntegerField(index=True, null=True)
    appart_letter = CharField(index=True, null=True)
    district = ForeignKeyField(column_name='district_id', field='id', model=District, null=True)
    entrance = CharField(null=True)
    floor = CharField(null=True)
    house = IntegerField(index=True, null=True)
    house_letter = CharField(index=True, null=True)
    links_count = IntegerField(null=True)
    remark = TextField(null=True)
    street = ForeignKeyField(column_name='street_id', field='id', model=Street)

    class Meta:
        table_name = 'address'

class User(BaseModel):
    is_active = IntegerField(index=True, null=True)
    is_admin = IntegerField(index=True, null=True)
    login = CharField(unique=True)
    name = CharField(null=True)
    passwd = CharField()

    class Meta:
        table_name = 'user'

class Customer(BaseModel):
    address = ForeignKeyField(column_name='address_id', field='id', model=Address, null=True)
    balance = DecimalField(index=True, null=True)
    create_time = IntegerField(null=True)
    creator = ForeignKeyField(column_name='creator_id', field='id', model=User, null=True)
    credit = DecimalField(index=True, null=True)
    credit_expire = IntegerField(null=True)
    is_deleted = IntegerField(index=True, null=True)
    is_jurical = IntegerField(index=True, null=True)
    is_locked = IntegerField(index=True, null=True)
    is_online = IntegerField(index=True, null=True)
    lock_expire = IntegerField(index=True, null=True)
    lock_start = IntegerField(index=True, null=True)
    login = CharField(index=True)
    name = CharField()
    need_passwd_auth = IntegerField(index=True, null=True)
    no_report = IntegerField(index=True, null=True)
    passwd = CharField()
    phone = CharField(index=True, null=True)
    remark = TextField(null=True)
    update_time = IntegerField(null=True)
    updater = ForeignKeyField(backref='user_updater_set', column_name='updater_id', field='id', model=User, null=True)

    class Meta:
        table_name = 'customer'

class Service(BaseModel):
    action_connect_from = IntegerField(null=True)
    action_cost = DecimalField(null=True)
    action_expire = IntegerField(null=True)
    can_user_connect = IntegerField(index=True, null=True)
    can_user_disconnect = IntegerField(index=True, null=True)
    cost = DecimalField(null=True)
    is_connect = IntegerField(index=True, null=True)
    is_debitor = IntegerField(null=True)
    is_deleted = IntegerField(index=True, null=True)
    is_like_periodic = IntegerField(index=True, null=True)
    is_once = IntegerField(null=True)
    is_pre_connect = IntegerField(null=True)
    is_special = IntegerField(index=True, null=True)
    name = CharField(unique=True)
    period_type = IntegerField(null=True)
    provider_id = IntegerField(index=True, null=True)
    sort = IntegerField(index=True, null=True)
    speed = IntegerField(null=True)
    traffic_limit = BigIntegerField(null=True)
    traffic_overquote_speed = IntegerField(null=True)
    tx_speed = IntegerField(null=True)

    class Meta:
        table_name = 'service'

class Tech(BaseModel):
    classname = CharField(null=True, unique=True)
    is_active = IntegerField(index=True, null=True)
    name = CharField(unique=True)
    provider_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'tech'

class LinkCustomerService(BaseModel):
    current_traffic = BigIntegerField(null=True)
    custom_cost = DecimalField(null=True)
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer)
    is_deleted = IntegerField(index=True, null=True)
    is_discount_lock = IntegerField(index=True, null=True)
    is_service_status_locked = IntegerField(null=True)
    is_traffic_overquoted = IntegerField(index=True, null=True)
    link_time = IntegerField(null=True)
    next_discount = IntegerField(null=True)
    remark = TextField(null=True)
    service = ForeignKeyField(column_name='service_id', field='id', model=Service)
    service_status = IntegerField(index=True, null=True)
    service_status_updater = ForeignKeyField(column_name='service_status_updater_id', field='id', model=User, null=True)
    special_cost = DecimalField(null=True)
    special_cost_end = IntegerField(index=True, null=True)
    special_cost_start = IntegerField(index=True, null=True)
    tech = ForeignKeyField(column_name='tech_id', field='id', model=Tech, null=True)
    unlink_time = IntegerField(null=True)

    class Meta:
        table_name = 'link_customer_service'

class PaymentSystem(BaseModel):
    classname = CharField(null=True)
    info = TextField(null=True)
    is_active = IntegerField(index=True, null=True)
    is_allow_manual = IntegerField(null=True)
    is_deleted = IntegerField(index=True, null=True)
    logo = CharField(null=True, unique=True)
    name = CharField(null=True)
    no_report = IntegerField(index=True, null=True)
    priority = IntegerField(null=True)
    provider_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'payment_system'

class Payment(BaseModel):
    creator = ForeignKeyField(column_name='creator_id', field='id', model=User, null=True)
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer)
    enter_date = IntegerField(index=True, null=True)
    finish_time = IntegerField(null=True)
    is_finished = IntegerField(index=True, null=True)
    payment_code = CharField(null=True)
    payment_date = IntegerField(index=True, null=True)
    payment_doc = CharField(index=True, null=True)
    payment_system = ForeignKeyField(column_name='payment_system_id', field='id', model=PaymentSystem)
    payment_time = IntegerField(null=True)
    receive_date = IntegerField(index=True, null=True)
    remark = TextField(null=True)
    remark_admin = TextField(null=True)
    value = DecimalField(null=True)

    class Meta:
        table_name = 'payment'

class Discount(BaseModel):
    balance_after = DecimalField(null=True)
    balance_before = DecimalField(null=True)
    discount_time = IntegerField(index=True, null=True)
    is_fixed = IntegerField(index=True, null=True)
    link_customer_service = ForeignKeyField(column_name='link_customer_service_id', field='id', model=LinkCustomerService, null=True)
    payment = ForeignKeyField(column_name='payment_id', field='id', model=Payment, null=True)
    report_balance_after = DecimalField(null=True)
    report_balance_before = DecimalField(null=True)
    value = DecimalField()

    class Meta:
        table_name = 'discount'

class DocsisCmtsModel(BaseModel):
    name = CharField(unique=True)
    provider_id = IntegerField(index=True, null=True)
    temperature_mult = IntegerField(null=True)

    class Meta:
        table_name = 'docsis_cmts_model'

class DocsisCmts(BaseModel):
    address = ForeignKeyField(column_name='address_id', field='id', model=Address, null=True)
    docsis_cmts_model = ForeignKeyField(column_name='docsis_cmts_model_id', field='id', model=DocsisCmtsModel)
    ip = IntegerField(null=True, unique=True)
    name = CharField(null=True, unique=True)
    remark = TextField(null=True)
    snmp_read_community = CharField(null=True)
    snmp_write_community = CharField(null=True)

    class Meta:
        table_name = 'docsis_cmts'

class DocsisCmtsDownstream(BaseModel):
    docsis_cmts = ForeignKeyField(column_name='docsis_cmts_id', field='id', model=DocsisCmts)
    freq = BigIntegerField(null=True)
    name = CharField()
    number = IntegerField(null=True)
    snmp_frequency = CharField(null=True)
    snmp_power = CharField(null=True)
    snmp_utilization = CharField(null=True)

    class Meta:
        table_name = 'docsis_cmts_downstream'
        indexes = (
            (('docsis_cmts', 'name'), True),
            (('docsis_cmts', 'number'), True),
        )

class DocsisCmtsModelModemState(BaseModel):
    color = CharField(null=True)
    docsis_cmts_model = ForeignKeyField(column_name='docsis_cmts_model_id', field='id', model=DocsisCmtsModel)
    is_ready = IntegerField(null=True)
    name = CharField()
    provider_id = IntegerField(index=True, null=True)
    state = IntegerField()

    class Meta:
        table_name = 'docsis_cmts_model_modem_state'
        indexes = (
            (('docsis_cmts_model', 'name'), True),
            (('docsis_cmts_model', 'state'), True),
        )

class DocsisCmtsModelSnmp(BaseModel):
    docsis_cmts_model = ForeignKeyField(column_name='docsis_cmts_model_id', field='id', model=DocsisCmtsModel)
    name = CharField(index=True)
    oid = CharField(index=True)
    provider_id = IntegerField(index=True, null=True)
    sort = IntegerField(index=True, null=True)
    type = CharField(index=True, null=True)
    value = CharField(null=True)

    class Meta:
        table_name = 'docsis_cmts_model_snmp'
        indexes = (
            (('docsis_cmts_model', 'name', 'sort'), True),
        )

class DocsisCmtsUpstream(BaseModel):
    docsis_cmts_downstream = ForeignKeyField(column_name='docsis_cmts_downstream_id', field='id', model=DocsisCmtsDownstream)
    freq = BigIntegerField(null=True)
    name = CharField()
    number = IntegerField(null=True)
    snmp_corrected_errors = CharField(null=True)
    snmp_frequency = CharField(null=True)
    snmp_no_errors = CharField(null=True)
    snmp_power = CharField(null=True)
    snmp_snr = CharField(null=True)
    snmp_uncorrected_errors = CharField(null=True)
    snmp_utilization = CharField(null=True)

    class Meta:
        table_name = 'docsis_cmts_upstream'
        indexes = (
            (('docsis_cmts_downstream', 'name'), True),
            (('docsis_cmts_downstream', 'number'), True),
        )

class IpBlock(BaseModel):
    gateway = IntegerField(index=True)
    ip_end = IntegerField(index=True, null=True)
    ip_start = IntegerField(index=True)
    last_used = IntegerField(null=True)
    mask = IntegerField(index=True)
    name = CharField(null=True, unique=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'ip_block'

class IpCustomer(BaseModel):
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer)
    ip = IntegerField(index=True)
    link_time = IntegerField(index=True, null=True)
    mask = IntegerField(index=True)
    tech = ForeignKeyField(column_name='tech_id', field='id', model=Tech)
    unlink_time = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'ip_customer'
        indexes = (
            (('customer', 'tech'), True),
        )

class IptvChannel(BaseModel):
    is_active = IntegerField(index=True, null=True)
    name = CharField()
    provider_id = IntegerField(index=True, null=True)
    sort = IntegerField(index=True, null=True)
    url = CharField()

    class Meta:
        table_name = 'iptv_channel'

class IptvPacket(BaseModel):
    is_manage = IntegerField(index=True, null=True)
    name = CharField(unique=True)
    provider_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'iptv_packet'

class LinkDocsisCmtsIpBlock(BaseModel):
    docsis_cmts = ForeignKeyField(column_name='docsis_cmts_id', field='id', model=DocsisCmts)
    ip_block = ForeignKeyField(column_name='ip_block_id', field='id', model=IpBlock)

    class Meta:
        table_name = 'link_docsis_cmts_ip_block'
        indexes = (
            (('docsis_cmts', 'ip_block'), True),
        )

class LinkIptvChannelPacket(BaseModel):
    iptv_channel = ForeignKeyField(column_name='iptv_channel_id', field='id', model=IptvChannel)
    iptv_packet = ForeignKeyField(column_name='iptv_packet_id', field='id', model=IptvPacket)
    provider_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'link_iptv_channel_packet'

class LinkIptvPacketService(BaseModel):
    iptv_packet = ForeignKeyField(column_name='iptv_packet_id', field='id', model=IptvPacket)
    provider_id = IntegerField(index=True, null=True)
    service = ForeignKeyField(column_name='service_id', field='id', model=Service)

    class Meta:
        table_name = 'link_iptv_packet_service'
        indexes = (
            (('iptv_packet', 'service'), True),
        )

class PonOltModel(BaseModel):
    name = CharField(unique=True)
    provider_id = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pon_olt_model'

class PonOlt(BaseModel):
    address = ForeignKeyField(column_name='address_id', field='id', model=Address, null=True)
    base_vlan = IntegerField(index=True, null=True)
    ip = IntegerField(null=True, unique=True)
    name = CharField(unique=True)
    pon_olt_model = ForeignKeyField(column_name='pon_olt_model_id', field='id', model=PonOltModel)
    remark = TextField(null=True)
    snmp_read_community = CharField(null=True)
    snmp_write_community = CharField(null=True)

    class Meta:
        table_name = 'pon_olt'

class LinkPonOltIpBlock(BaseModel):
    ip_block = ForeignKeyField(column_name='ip_block_id', field='id', model=IpBlock)
    pon_olt = ForeignKeyField(column_name='pon_olt_id', field='id', model=PonOlt)

    class Meta:
        table_name = 'link_pon_olt_ip_block'
        indexes = (
            (('pon_olt', 'ip_block'), True),
        )

class LinkServiceTech(BaseModel):
    provider_id = IntegerField(index=True, null=True)
    service = ForeignKeyField(column_name='service_id', field='id', model=Service)
    tech = ForeignKeyField(column_name='tech_id', field='id', model=Tech)

    class Meta:
        table_name = 'link_service_tech'
        indexes = (
            (('service', 'tech'), True),
        )

class LinkStreetDistrict(BaseModel):
    district = ForeignKeyField(column_name='district_id', field='id', model=District)
    end_house = IntegerField(null=True)
    end_house_letter = CharField(null=True)
    start_house = IntegerField(null=True)
    start_house_letter = CharField(null=True)
    street = ForeignKeyField(column_name='street_id', field='id', model=Street)

    class Meta:
        table_name = 'link_street_district'

class SwitchModel(BaseModel):
    cfg_template = TextField(null=True)
    customer_count = IntegerField(null=True)
    customer_start = IntegerField(null=True)
    dhcp_class_template = TextField(null=True)
    name = CharField(unique=True)
    port_count = IntegerField()
    provider_id = IntegerField(index=True, null=True)
    snmp_reboot_oid = CharField(null=True)
    snmp_reboot_type = CharField(null=True)
    snmp_reboot_value = CharField(null=True)
    snmp_save_config_oid = CharField(null=True)
    snmp_save_config_type = CharField(null=True)
    snmp_save_config_value = CharField(null=True)

    class Meta:
        table_name = 'switch_model'

class Switch(BaseModel):
    address = ForeignKeyField(column_name='address_id', field='id', model=Address)
    dhcp_relay = IntegerField(null=True)
    gw = IntegerField(null=True)
    instance1_vlan_begin = IntegerField(null=True)
    instance1_vlan_end = IntegerField(null=True)
    instance2_vlan_begin = IntegerField(null=True)
    instance2_vlan_end = IntegerField(null=True)
    ip = IntegerField(index=True, null=True)
    mac = CharField(index=True, null=True)
    remark = TextField(null=True)
    snmp_read_community = CharField(null=True)
    snmp_write_community = CharField(null=True)
    switch_model = ForeignKeyField(column_name='switch_model_id', field='id', model=SwitchModel)
    vlan = IntegerField(null=True)

    class Meta:
        table_name = 'switch'

class SwitchPort(BaseModel):
    ip = IntegerField(index=True, null=True)
    is_bad = IntegerField(index=True, null=True)
    is_ring = IntegerField(index=True, null=True)
    is_stack = IntegerField(index=True, null=True)
    mask = IntegerField(index=True, null=True)
    port = IntegerField(index=True, null=True)
    switch = ForeignKeyField(column_name='switch_id', field='id', model=Switch)

    class Meta:
        table_name = 'switch_port'
        indexes = (
            (('ip', 'mask'), True),
            (('switch', 'port'), True),
        )

class LinkSwitch(BaseModel):
    switch1_port = ForeignKeyField(column_name='switch1_port_id', field='id', model=SwitchPort)
    switch2_port = ForeignKeyField(backref='switch_port_switch2_port_set', column_name='switch2_port_id', field='id', model=SwitchPort)

    class Meta:
        table_name = 'link_switch'

class LinkSwitchModelIptvPacket(BaseModel):
    iptv_packet = ForeignKeyField(column_name='iptv_packet_id', field='id', model=IptvPacket)
    profile = IntegerField(null=True)
    provider_id = IntegerField(index=True, null=True)
    switch_model = ForeignKeyField(column_name='switch_model_id', field='id', model=SwitchModel)

    class Meta:
        table_name = 'link_switch_model_iptv_packet'
        indexes = (
            (('iptv_packet', 'switch_model', 'profile'), True),
        )

class WifiStationModel(BaseModel):
    name = CharField(unique=True)
    provider_id = IntegerField(index=True, null=True)
    radius_passwd = CharField(null=True)

    class Meta:
        table_name = 'wifi_station_model'

class WifiStation(BaseModel):
    address = ForeignKeyField(column_name='address_id', field='id', model=Address, null=True)
    ip = IntegerField(index=True, null=True)
    mac = CharField(null=True)
    name = CharField(unique=True)
    radius_key = CharField(null=True)
    remark = TextField(null=True)
    snmp_read_community = CharField(null=True)
    snmp_write_community = CharField(null=True)
    wifi_station_model = ForeignKeyField(column_name='wifi_station_model_id', field='id', model=WifiStationModel)

    class Meta:
        table_name = 'wifi_station'

class LinkWifiStationIpBlock(BaseModel):
    ip_block = ForeignKeyField(column_name='ip_block_id', field='id', model=IpBlock)
    wifi_station = ForeignKeyField(column_name='wifi_station_id', field='id', model=WifiStation)

    class Meta:
        table_name = 'link_wifi_station_ip_block'

class ModuleConfig(BaseModel):
    module_name = CharField()
    name = CharField()
    provider_id = IntegerField(index=True, null=True)
    remark = TextField(null=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'module_config'
        indexes = (
            (('module_name', 'name'), True),
        )

class PaymentFuture(BaseModel):
    creator = ForeignKeyField(column_name='creator_id', field='id', model=User, null=True)
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer)
    enter_date = IntegerField(index=True, null=True)
    finish_time = IntegerField(null=True)
    in_applying = IntegerField(index=True, null=True)
    is_finished = IntegerField(index=True, null=True)
    payment_code = CharField(null=True)
    payment_date = IntegerField(index=True, null=True)
    payment_doc = CharField(index=True, null=True)
    payment_system = ForeignKeyField(column_name='payment_system_id', field='id', model=PaymentSystem)
    payment_time = IntegerField(null=True)
    receive_date = IntegerField(index=True, null=True)
    remark = TextField(null=True)
    remark_admin = TextField(null=True)
    value = DecimalField(null=True)

    class Meta:
        table_name = 'payment_future'

class PaymentSystemCard(BaseModel):
    expire = IntegerField(index=True, null=True)
    is_used = IntegerField(index=True, null=True)
    payment = ForeignKeyField(column_name='payment_id', field='id', model=Payment, null=True)
    pin = CharField(unique=True)
    use_time = IntegerField(index=True, null=True)
    value = DecimalField()

    class Meta:
        table_name = 'payment_system_card'

class PonOltModelOntState(BaseModel):
    color = CharField(null=True)
    is_ready = IntegerField(null=True)
    name = CharField()
    pon_olt_model = ForeignKeyField(column_name='pon_olt_model_id', field='id', model=PonOltModel)
    provider_id = IntegerField(index=True, null=True)
    state = IntegerField()

    class Meta:
        table_name = 'pon_olt_model_ont_state'

class PonOltModelSnmp(BaseModel):
    name = CharField(index=True)
    oid = CharField(index=True)
    pon_olt_model = ForeignKeyField(column_name='pon_olt_model_id', field='id', model=PonOltModel)
    provider_id = IntegerField(index=True, null=True)
    sort = IntegerField(index=True, null=True)
    type = CharField(null=True)
    value = CharField(null=True)

    class Meta:
        table_name = 'pon_olt_model_snmp'
        indexes = (
            (('pon_olt_model', 'name'), True),
        )

class PonOltTree(BaseModel):
    interface_name = CharField(index=True, null=True)
    max_ont_count = IntegerField(index=True, null=True)
    name = CharField(index=True)
    pon_olt = ForeignKeyField(column_name='pon_olt_id', field='id', model=PonOlt)
    snmp_corrected_errors = CharField(null=True)
    snmp_fec = CharField(null=True)
    snmp_no_errors = CharField(null=True)
    snmp_uncorrected_errors = CharField(null=True)
    snmp_utilization = CharField(null=True)
    vlan_block_number = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'pon_olt_tree'
        indexes = (
            (('pon_olt', 'interface_name'), True),
            (('pon_olt', 'name'), True),
        )

class PostponeActions(BaseModel):
    create_time = IntegerField(null=True)
    is_snmp = IntegerField(index=True, null=True)
    name = CharField(null=True)
    snmp_oid = CharField(null=True)
    snmp_type = CharField(null=True)
    snmp_value = CharField(null=True)
    switch = ForeignKeyField(column_name='switch_id', field='id', model=Switch, null=True)

    class Meta:
        table_name = 'postpone_actions'

class SwitchModelSnmp(BaseModel):
    name = CharField()
    oid = CharField(index=True)
    provider_id = IntegerField(index=True, null=True)
    sort = IntegerField(index=True)
    switch_model = ForeignKeyField(column_name='switch_model_id', field='id', model=SwitchModel)
    type = CharField(index=True)
    value = CharField(null=True)

    class Meta:
        table_name = 'switch_model_snmp'
        indexes = (
            (('switch_model', 'name', 'sort'), True),
        )

class TechDocsis(BaseModel):
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer, unique=True)
    docsis_cmts_upstream = ForeignKeyField(column_name='docsis_cmts_upstream_id', field='id', model=DocsisCmtsUpstream, null=True)
    is_inet_on = IntegerField(null=True)
    modem_ip = IntegerField(unique=True)
    modem_mac = CharField(unique=True)
    modem_model = CharField(index=True, null=True)
    user_ip = IntegerField(unique=True)
    user_mask = IntegerField()

    class Meta:
        table_name = 'tech_docsis'

class TechPon(BaseModel):
    customer_id = IntegerField()
    ont_index = IntegerField(index=True, null=True)
    ont_mac = CharField(unique=True)
    ont_model = CharField(null=True)
    pon_olt_tree_id = IntegerField(null=True)
    user_ip = IntegerField(null=True)
    user_mask = IntegerField(null=True)

    class Meta:
        table_name = 'tech_pon'
        indexes = (
            (('pon_olt_tree_id', 'ont_index'), True),
        )

class TechSwitch(BaseModel):
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer, unique=True)
    switch_port = ForeignKeyField(column_name='switch_port_id', field='id', model=SwitchPort, null=True)

    class Meta:
        table_name = 'tech_switch'
        indexes = (
            (('customer', 'switch_port'), True),
        )

class TechWifi(BaseModel):
    customer = ForeignKeyField(column_name='customer_id', field='id', model=Customer)
    ip = IntegerField(unique=True)
    is_inet_on = IntegerField(index=True, null=True)
    login = CharField(unique=True)
    mac = CharField(unique=True)
    passwd = CharField()
    wifi_station = ForeignKeyField(column_name='wifi_station_id', field='id', model=WifiStation)
    wifi_station_model = ForeignKeyField(column_name='wifi_station_model_id', field='id', model=WifiStationModel)

    class Meta:
        table_name = 'tech_wifi'
        indexes = (
            (('login', 'passwd'), True),
        )

