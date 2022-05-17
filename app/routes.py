import json

from app import app
from app.models import ContactBodyModel, Contact
from flask_pydantic import validate
from flask import request, Blueprint
from app import db
from app.utils import response_handler


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route("/contacts", methods=["POST"])
@validate()
def add_contact(body: ContactBodyModel):
    if Contact.query.filter(Contact.email == body.email).first():
        return response_handler(f"Contact with email {body.email} already exists", 400)

    c = Contact(
        email=body.email,
        first_name=body.first_name,
        last_name=body.last_name,
        phone=body.phone,
        country=body.country,
        city=body.city,
        address=body.address,
    )
    db.session.add(c)
    db.session.commit()
    return response_handler(f"Contact with email {body.email} sucessfully added to contacts", 200)


@bp.route("/contacts", methods=["GET"])
def list_contacts():
    contact_list = []

    contacts = Contact.query.all()
    for contact in contacts:
        c = ContactBodyModel(
            id=contact.id,
            email=contact.email,
            first_name=contact.first_name,
            last_name=contact.last_name,
            phone=contact.phone,
            country=contact.country,
            city=contact.city,
            address=contact.address,
        )
        contact_list.append(c.dict())
    return json.dumps(contact_list)


@bp.route("/contacts/<contact_id>", methods=["GET"])
def get_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)

    c = ContactBodyModel(
            id=contact.id,
            email=contact.email,
            first_name=contact.first_name,
            last_name=contact.last_name,
            phone=contact.phone,
            country=contact.country,
            city=contact.city,
            address=contact.address,
        )
    return c.dict()


@bp.route("/contacts/<contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    if not Contact.query.filter(Contact.id == contact_id).first():
        return response_handler(f"Contact with id {contact_id} not found", 404)

    Contact.query.filter(Contact.id == contact_id).delete()
    db.session.commit()
    return response_handler(f"Contact with id {contact_id} succesfully deleted", 200)


@bp.route("/contacts/<contact_id>", methods=["PUT"])
def update_contact(contact_id):
    contact = Contact.query.filter(Contact.id == contact_id).first()

    data = request.json
    params_for_update = {}

    for col_name in data.keys():
        if col_name in Contact.__table__.columns.keys():
            params_for_update[col_name] = data[col_name]

    contact.update(**params_for_update)
    db.session.commit()
    return response_handler("Contact succesfully updated", 200)


@bp.route("/contacts/delete_all", methods=["DELETE"])
def delete_all():
    """
    Метод вне требований, предназначен для упрощения отладки
    """
    try:
        db.session.query(Contact).delete()
        db.session.commit()
    except:
        db.session.rollback()
        return response_handler("Unexcpected error, session has been rollbacked", 400)
    return response_handler("All contacts has been deleted", 200)
