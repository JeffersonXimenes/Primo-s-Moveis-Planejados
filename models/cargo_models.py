from infraestrutura.sql_alchemy import banco


class CargoModel(banco.Model):
    __tablename__ = 'tCargos'

    cCargos = banco.Column(banco.Integer, primary_key=True)
    iCargos = banco.Column(banco.String(255), nullable = False)



    def __init__(self, cCargos, iCargos):
        self.cCargos = cCargos
        self.iCargos = iCargos


    def json(self):
        return {
            'cCargos': self.cCargos,
            'iCargos': self.iCargos,

        }

    @classmethod
    def find_cargo(cls, cCargos):
        cargo = cls.query.filter_by(cCargos=cCargos).first()
        if cargo:
            return cargo
        return None

    def save_cargo(self):
        banco.session.add(self)
        banco.session.commit()

    def update_cargo(self,  iCargos):
        self.iCargos = iCargos


    def delete_cargo(self):
        banco.session.delete(self)
        banco.session.commit()
