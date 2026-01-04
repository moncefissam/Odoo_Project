from odoo import models, fields

class GestionAnnonce(models.Model):
    _name = "gestion.annonce"
    _description = "Gestion des Annonces"

    name = fields.Char(string="Titre", required=True)
    auteur = fields.Char(string="Auteur")
    date_annonce = fields.Date(string="Date de l'annonce", default=fields.Date.today)
    type = fields.Selection([
        ("info", "Information"),
        ("alerte", "Alerte"),
        ("event", "Événement"),
    ], string="Type", default="info")
    description = fields.Text(string="Contenu")
