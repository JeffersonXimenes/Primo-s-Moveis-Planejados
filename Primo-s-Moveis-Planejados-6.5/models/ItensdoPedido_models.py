from infraestrutura.sql_alchemy import banco


class ItemPedidoModel(banco.Model):
    __tablename__ = 'tItensDoPedido'

    cItem = banco.Column(banco.Integer, primary_key=True)
    cPedido = banco.Column(banco.Integer, banco.ForeignKey('tVendas.cPedido'), nullable = False)
    iDescricao = banco.Column(banco.String(255), nullable = False)


    def __init__(self, cItem, cPedido,iDescricao):
        self.cItem = cItem
        self.cPedido = cPedido
        self.iDescricao = iDescricao


    def json(self):
        return {
            'cItem': self.cItem,
            'cPedido': self.cPedido,
            'iDescricao': self.iDescricao,

        }

    @classmethod
    def find_Item(cls, cItem):
        item = cls.query.filter_by(cItem=cItem).first()
        if item:
            return item
        return None

    def save_Item(self):
        banco.session.add(self)
        banco.session.commit()

    def update_Item(self, cPedido,iDescricao):
        self.cPedido = cPedido
        self.iDescricao = iDescricao


    def delete_Item(self):
        banco.session.delete(self)
        banco.session.commit()
