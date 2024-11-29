from flask import Blueprint
from controllers import create_ticket, get_tickets, get_ticket, update_ticket

ticket_blueprint = Blueprint('ticket', __name__)

ticket_blueprint.route('/tickets', methods=['POST'])(create_ticket)
ticket_blueprint.route('/tickets', methods=['GET'])(get_tickets)
ticket_blueprint.route('/tickets/<int:ticket_id>', methods=['GET'])(get_ticket)
ticket_blueprint.route('/tickets/<int:ticket_id>', methods=['PUT'])(update_ticket)
