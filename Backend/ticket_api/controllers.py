from flask import request, jsonify
from models import db, Ticket
from datetime import datetime

def create_ticket():
    data = request.get_json()
    new_ticket = Ticket(
        title=data['title'],
        description=data['description'],
        user_info=data['user_info'],
        status=data['status'],
        created_at=datetime.now(),
        updated_at=None
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify(new_ticket.to_dict()), 201

def get_tickets():
    # Sort tickets by creation time (assuming the column is named 'created_at')
    tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()  # Change 'created_at' if needed
    return jsonify([ticket.to_dict() for ticket in tickets])

def get_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket:
        return jsonify(ticket.to_dict())
    else:
        return jsonify({"error": "Ticket not found"}), 404

def update_ticket(ticket_id):
    data = request.get_json()
    ticket = Ticket.query.get(ticket_id)
    
    if ticket:
        ticket.title = data.get('title', ticket.title)
        ticket.description = data.get('description', ticket.description)
        ticket.user_info = data.get('user_info', ticket.user_info)
        ticket.status = data.get('status', ticket.status)
        ticket.updated_at = datetime.now()
        
        db.session.commit()
        return jsonify(ticket.to_dict())
    else:
        return jsonify({"error": "Ticket not found"}), 404
