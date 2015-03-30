from osv import orm, fields


class ix_doc_step(orm.Model)
    _name = 'ix.doc.step'
    _columns = {
        'name': fields.char('Name'),
        'prev_id': fields.many2one('ix.doc.step', 'Previous'),
        'next_id': fields.many2one('ix.doc.step', 'Next'),
        'content':  fields.text('Content'),
        'page_id': fields.many2one('document.page', 'Page ID'),
    }
