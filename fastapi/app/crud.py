from fastapi import types
from sqlalchemy.orm import Session
import hashlib
from .schemas import *
from .models import *

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: new_user):
    hashed_password = hashlib.sha256(user.password.encode())
    user.password = hashed_password.hexdigest()

    db_user = User(
        user_fname=user.user_fname,
        user_lname=user.user_lname,
        login_id=user.login_id,
        password=user.password,
        email=user.email,
        contact_no=user.contact_no)
    db.add(db_user)
    db.commit()
    return db_user


def update_user(db: Session,user_id:int,user: new_user):
    db_user =  db.query(User).filter(User.user_id==user_id).first()

    hashed_password = hashlib.sha256(user.password.encode())
    user.password = hashed_password.hexdigest()

    db_user.user_fname=user.user_fname,
    db_user.user_lname=user.user_lname,
    db_user.login_id=user.login_id,
    db_user.password=user.password,
    db_user.email=user.email,
    db_user.contact_no=user.contact_no
    db.commit()
    db.refresh(db_user)
    return db_user

def remove_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {}


#CONTRACT

def get_contract(db: Session, ticker: str):
    return db.query(Contract).filter(Contract.ticker == ticker).first()

def get_contracts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contract).offset(skip).limit(limit).all()

def create_contract(db: Session, user: new_contract):
    db_contract = Contract(
        ticker=user.ticker,
        contract_name=user.contract_name,
        market_name=user.market_name,
        currency=user.currency)
    db.add(db_contract)
    db.commit()
    return db_contract


def update_contract(db: Session,ticker:str,user: new_contract):
    db_contract =  db.query(Contract).filter(Contract.ticker==ticker).first()
    db_contract.contract_name=user.contract_name,
    db_contract.market_name=user.market_name,
    db_contract.currency=user.currency
    db.commit()
    db.refresh(db_contract)
    return db_contract


def remove_contract(db: Session, ticker: str):
    db_contract = db.query(Contract).filter(Contract.ticker == ticker).first()
    db.delete(db_contract)
    db.commit()

    return {}







#SCANNER

def get_scanner(db: Session, scanner_id: int):
    return db.query(Scanner).filter(Scanner.scanner_id == scanner_id).first()


def get_scanners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Scanner).offset(skip).limit(limit).all()


def create_scanner(db: Session, user: new_scanner):
    db_scanner = Scanner(
        scanner_name=user.scanner_name,
        platform_name=user.platform_name)
    db.add(db_scanner)
    db.commit()
    return db_scanner


def update_scanner(db: Session,scanner_id:int,user: new_scanner):
    db_scanner =  db.query(Scanner).filter(Scanner.scanner_id==scanner_id).first()
    db_scanner.scanner_name=user.scanner_name,
    db_scanner.platform_name=user.platform_name
    db.commit()
    db.refresh(db_scanner)
    return db_scanner


def remove_scanner(db: Session, scanner_id: int):
    db_scanner = db.query(Scanner).filter(Scanner.scanner_id == scanner_id).first()
    db.delete(db_scanner)
    db.commit()
    return {}



#WATCHLIST

def get_watchlist(db: Session, watchlist_id: int):
    return db.query(Watchlist).filter(Watchlist.watchlist_id == watchlist_id).first()


def get_watchlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Watchlist).offset(skip).limit(limit).all()


def create_watchlist(db: Session, user: new_watchlist):
    db_watchlist = Watchlist(
        watchlist_name=user.watchlist_name)
    db.add(db_watchlist)
    db.commit()
    return db_watchlist


def update_watchlist(db: Session,watchlist_id:int,user: new_watchlist):
    db_watchlist =  db.query(Watchlist).filter(Watchlist.watchlist_id==watchlist_id).first()
    db_watchlist.watchlist_name=user.watchlist_name
    db.commit()
    db.refresh(db_watchlist)
    return db_watchlist


def remove_watchlist(db: Session, watchlist_id: int):
    db_watchlist = db.query(Watchlist).filter(Watchlist.watchlist_id == watchlist_id).first()
    db.delete(db_watchlist)
    db.commit()
    return {}



#TEMPLATE

def get_template(db: Session, template_id: int):
    return db.query(Templates).filter(Templates.template_id == template_id).first()


def get_templates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Templates).offset(skip).limit(limit).all()


def create_template(db: Session, user: new_template):
    db_template = Templates(
        template_title=user.template_title,
        description=user.description,
        types=user.types,
        content=user.content,
        created_at=user.created_at,
        updated_at=user.updated_at)
    db.add(db_template)
    db.commit()
    return db_template


def update_template(db: Session,template_id:int,user:new_template):
    db_template =  db.query(Templates).filter(Templates.template_id==template_id).first()
    db_template.template_title=user.template_title,
    db_template.description=user.description,
    db_template.types=user.types,
    db_template.content=user.content,
    db_template.created_at=user.created_at,
    db_template.updated_at=user.updated_at
    db.commit()
    db.refresh(db_template)
    return db_template


def remove_template(db: Session, template_id: int):
    db_template = db.query(Templates).filter(Templates.template_id == template_id).first()
    db.delete(db_template)
    db.commit()
    return {}





#NOTIFICATION

def get_notification(db: Session, notification_id: int):
    return db.query(Notifications).filter(Notifications.notification_id == notification_id).first()


def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notifications).offset(skip).limit(limit).all()


def create_notification(db: Session, user: new_notification):
    db_notification = Notifications(
        template_id=user.template_id,
        types=user.types,
        content=user.content,
        created_at=user.created_at,
        updated_at=user.updated_at)
    db.add(db_notification)
    db.commit()
    return db_notification


def update_notification(db: Session,notification_id:int,user: new_notification):
    db_notification =  db.query(Notifications).filter(Notifications.notification_id==notification_id).first()
    db_notification.template_id=user.template_id,
    db_notification.types=user.types,
    db_notification.content=user.content,
    db_notification.created_at=user.created_at,
    db_notification.updated_at=user.updated_at,
    db.commit()
    db.refresh(db_notification)
    return db_notification


def remove_notification(db: Session, notification_id: int):
    db_notification = db.query(Notifications).filter(Notifications.notification_id == notification_id).first()
    db.delete(db_notification)
    db.commit()
    return {}



# USER_CONDITIONS


def get_condition(db: Session, condition_id: int):
    return db.query(User_Conditions).filter(User_Conditions.condition_id == condition_id).first()

def get_conditions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User_Conditions).offset(skip).limit(limit).all()


def create_conditions(db: Session, user: new_user_condition):
    db_conditions = User_Conditions(
        user_id= user.user_id,
        watchlist_id= user.watchlist_id,
        scanner_id= user.scanner_id,
        notification_id= user.notification_id,
        conditions= user.conditions)
    db.add(db_conditions)
    db.commit()
    return db_conditions

def update_conditions(db: Session, condition_id: int ,user: new_user_condition):
    db_conditions= db.query(User_Conditions).filter(User_Conditions.condition_id == condition_id).first()
    db_conditions.user_id= user.user_id,
    db_conditions.watchlist_id= user.watchlist_id,
    db_conditions.scanner_id= user.scanner_id,
    db_conditions.notification_id= user.notification_id,
    db_conditions.conditions= user.conditions,
    db.commit()
    db.refresh(db_conditions)
    return db_conditions

def remove_conditions(db: Session, condition_id: int):
    db_conditions= db.query(User_Conditions).filter(User_Conditions.condition_id == condition_id).first()
    db.delete(db_conditions)
    db.commit()
    return {}







#RAW_DATA

def get_rawdata(db: Session, ticker : str):
    return db.query(RawData).filter(RawData.ticker == ticker).first()

def get_rawdatas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RawData).offset(skip).limit(limit).all()


def create_rawdata(db: Session, user: RawDataBase):
    db_rawdata = RawData(
        curr_date= user.curr_date,
        ticker = user.ticker,
        open = user.open,
        high = user.high,
        low = user.low,
        close = user.close,
        volume= user.volume)
    db.add(db_rawdata)
    db.commit()
    return db_rawdata



def update_rawdata(db: Session,ticker:str,user: new_rawdata):
    db_rawdata =  db.query(RawData).filter(RawData.ticker==ticker).first()
    
    db_rawdata.curr_date=user.curr_date,
    db_rawdata.ticker=user.ticker,
    db_rawdata.open=user.open,
    db_rawdata.high=user.high,
    db_rawdata.low=user.low,
    db_rawdata.close=user.close,
    db_rawdata.volume=user.volume
    db.commit()
    db.refresh(db_rawdata)
    return db_rawdata



def remove_rawdata(db: Session, ticker : str):
    db_rawdata = db.query(RawData).filter(RawData.ticker == ticker).first()
    db.delete(db_rawdata)
    db.commit()
    return {}
